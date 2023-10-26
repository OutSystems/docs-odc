import aiohttp
import asyncio
import os
from github import Github
from ruamel.yaml import YAML
import re
from io import StringIO
import logging
import subprocess
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RateLimiter:
    """
    A simple rate limiter to control the rate of API calls.
    
    Attributes:
        rate (int): The number of tokens allowed per time period.
        per (float): The time period for rate limiting in seconds.
        allowance (float): The current number of available tokens.
        last_check (float): The time of the last rate limit check.
    """
    def __init__(self, rate, per):
        """
        Initializes the RateLimiter with a specified rate and time period.
        
        Args:
            rate (int): The number of tokens allowed per time period.
            per (float): The time period for rate limiting in seconds.
        """
        self.rate = rate
        self.per = per
        self.allowance = rate
        self.last_check = time.monotonic()

    async def wait_for_token(self):
        while self.allowance < 1:
            await asyncio.sleep(1)
            current_time = time.monotonic()
            time_passed = current_time - self.last_check
            self.last_check = current_time
            self.allowance += time_passed * (self.rate / self.per)
            self.allowance = min(self.allowance, self.rate)
        self.allowance -= 1

class GitHubHandler:
    """
    Handles interactions with GitHub, specifically for pull request operations.
    
    This class provides methods to post comments to a pull request, and to post review comments on specific lines of files within a pull request. It initializes with the GitHub token, repository name, and pull request number to set up the necessary GitHub API objects.
    
    Attributes:
        github_obj (Github): The PyGithub main class instance, initialized with the provided GitHub token.
        repo (Repository): The repository object, retrieved using the repository name.
        pr (PullRequest): The pull request object, retrieved using the pull request number.
    """
    def __init__(self, github_token, repo_name, pr_number):
        """
        Initializes the GitHubHandler with the necessary GitHub API objects.
        
        Args:
            github_token (str): The GitHub token for authentication.
            repo_name (str): The name of the repository containing the pull request.
            pr_number (int): The number of the pull request.
        """
        self.github_obj = Github(github_token)
        self.repo = self.github_obj.get_repo(repo_name)
        self.pr = self.repo.get_pull(pr_number)

    def post_comment(self, message):
        """
        Posts a comment to the pull request.
        
        Args:
            message (str): The message to post as a comment.
        """
        self.pr.create_issue_comment(message)

    def post_review_comment(self, file_path, review_message):
        """
        Posts a review comment to a specific file in the pull request.
        
        Args:
            file_path (str): The path of the file to comment on.
            review_message (str): The review comment message.
        """
        pr = self.repo.get_pull(self.pr.number) # Refetch pull request data
        commit_obj = self.repo.get_commit(pr.head.sha)

        files = self.pr.get_files()
        for file in files:
            if file.filename == file_path:
                file_diff = file.patch
                break
        else:
            logging.warning(f"File not found in pull request: {file_path}")
            return

        diff_lines = file_diff.split('\n')
        position = next(
            (
                i
                for i, line in enumerate(diff_lines)
                if line.startswith('+summary:')
            ),
            None,
        )
        if position is None:
            message = f"Summary line not found in the file diff for `{file_path}`. If the summary is unchanged, no update is necessary."
            logging.warning(message)
            self.post_comment(message)
            return

        self.pr.create_review_comment(review_message, commit_obj, file_path, position)

    def add_reaction_to_comment(self, comment_id, reaction_type):
        """
        Adds a reaction to a pull request comment.
        
        Args:
            comment_id (int): The ID of the comment.
            reaction_type (str): The type of reaction to add.
        """
        try:
            comment = self.github_obj.get_repo(self.repo.full_name).get_issue(self.pr.number).get_comment(comment_id)
            comment.create_reaction(reaction_type)
        except Exception as e:
            logging.error(f'Failed to add reaction to comment {comment_id}: {str(e)}')

class SummaryHandler:
    """
    Handles summarization of markdown content and updating of summary fields in markdown files.
    
    Attributes:
        yaml (YAML): The YAML parser and dumper.
    """
    def __init__(self):
        """
        Initializes the SummaryHandler with a YAML parser and dumper.
        """
        self.yaml = YAML()
        self.yaml.preserve_quotes = True
        self.yaml.width = 4096  # To avoid line wrapping in the dumped YAML

    async def get_summary(self, session, text, summary_number, summarize_endpoint):
        """
        Asynchronously retrieves a summary for the given text.
        
        Args:
            session (ClientSession): The aiohttp client session.
            text (str): The text to summarize.
            summary_number (int): The summary version to retrieve.
            
        Returns:
            str or None: The summary text if successful, otherwise None.
        """
        logging.info('Sending request to /summarize endpoint')
        
        payload = {"text": text}
        try:
            async with session.post(summarize_endpoint, json=payload, timeout=30) as response:
                response.raise_for_status()  # This will raise an exception for HTTP errors
                summary_data = await response.json()

                # Check if the expected keys are present in the JSON response
                if "summary" in summary_data and f"Summary{summary_number}" in summary_data["summary"]:
                    summary_key = f"Summary{summary_number}"
                    summary = summary_data["summary"][summary_key].get("summary")
                    if summary is not None:
                        logging.info('Received summary: %s', summary)
                        return summary
                    else:
                        logging.error('Summary key found but summary text is missing')
                else:
                    logging.error('Expected keys are missing in the JSON response')
        except asyncio.TimeoutError:
            logging.error('Request to /summarize endpoint timed out')
        except aiohttp.ClientResponseError as e:
            logging.error(f'HTTP Response Error: {e}')
        except Exception as e:
            logging.error(f'An unexpected error occurred: {e}')

    def update_file_summary(self, file, summary, overwrite=False):
        """
        Updates the summary field in a markdown file.
        
        Args:
            file (ContentFile): The GitHub content file.
            summary (str): The summary text to update the file with.
            overwrite (bool): If True, overwrite the summary even if it already exists. Defaults to False.
        """
        logging.info('Updating summary for file: %s', file.filename)
        with open(file.filename, 'r') as md_file:
            content = md_file.read()

        if match := re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL):
            frontmatter, markdown_body = match.groups()
            metadata = self.yaml.load(frontmatter)
            if overwrite or ('summary' in metadata and not metadata['summary']):
                if metadata.get('summary') == summary:
                    logging.info('The generated summary is the same as the existing one. No update needed.')
                    return False
                metadata['summary'] = summary
                yaml_stream = StringIO()
                self.yaml.dump(metadata, yaml_stream)
                updated_frontmatter = yaml_stream.getvalue()

                with open(file.filename, 'w') as md_file:
                    md_file.write(f'---\n{updated_frontmatter}---\n{markdown_body}')
                return True
        else:
            logging.error('Failed to match frontmatter and markdown body for file: %s', file.filename)
        return False

    def commit_and_review(self, updated_files, github_handler):
        """
        Commits changes to the repository and posts review comments.
        
        Args:
            updated_files (list of str): A list of file paths that were updated.
            github_handler (GitHubHandler): The GitHubHandler instance for interacting with GitHub.
        """
        logging.info('Committing changes and posting review comments.')

        subprocess.run(['git', 'config', 'user.name', 'GitHub Action'], check=True)
        subprocess.run(['git', 'config', 'user.email', 'action@github.com'], check=True)

        result = subprocess.run(['git', 'status', '--porcelain'], text=True, capture_output=True)
        if result.stdout:
            subprocess.run(['git', 'add'] + updated_files, check=True)
        else:
            logging.info('No changes to add')
            return

        commit_result = subprocess.run(['git', 'commit', '-m', 'Update summary fields'])
        if commit_result.returncode != 0:
            logging.error('Failed to commit changes')
            return 

        subprocess.run(['git', 'push'], check=True)

        time.sleep(5)
        review_message = "Please check this AI-generated summary. To regenerate, use the `/summarize` command."
        for file_path in updated_files:
            github_handler.post_review_comment(file_path, review_message)

async def main():
    """
    The main asynchronous function to run the script. Handles initialization, processing, and cleanup.
    """
    github_token = os.environ['GITHUB_TOKEN']
    repo_name = os.environ['GITHUB_REPOSITORY']
    pr_number = int(os.environ['PR_NUMBER'])
    comment_id = os.environ['COMMENT_ID']
    comment_body = os.environ.get('COMMENT_BODY', '')
    summarize_endpoint = os.environ['SUMMARIZE_ENDPOINT']

    github_handler = GitHubHandler(github_token, repo_name, pr_number)
    summary_handler = SummaryHandler()
    rate_limiter = RateLimiter(20, 60)

    if '/summarize info' in comment_body:
        help_message = (
            "### Summarization Commands Guide\n\n"
            "The `/summarize` command can be used to automatically generate and update summaries for articles in your pull request.\n\n"
            "- **`/summarize 1`**: Summarizes the article(s) in one short sentence.  This is the default option.\n"
            "- **`/summarize 2`**: Summarizes the article(s) in one very short sentence.\n"
            "- **`/summarize 3`**: Summarizes the article(s) in one short sentence, start with \"Learn\".\n"
            "- **`/summarize 4`**: Summarizes the article(s) in one short sentence, start with \"This article\".\n\n"
            "To use these commands, simply type them in a comment on your pull request. The summarization process will start automatically, and you'll be notified of any updates or changes made to the article(s)."
        )
        github_handler.post_comment(help_message)
        return

    overwrite_summaries = '/summarize' in comment_body
    if overwrite_summaries:
            comment_id = int(comment_id)
            github_handler.add_reaction_to_comment(comment_id, 'eyes')

    if summary_number_match := re.search(r'/summarize (\S+)', comment_body):
        try:
            summary_text = summary_number_match[1]
            summary_number = int(summary_text)
            if summary_number < 1 or summary_number > 4:
                raise ValueError("/summarize number must be between 1 and 4.")
        except ValueError as e:
            error_message = f"Invalid /summarize number: `{summary_text}`. Using default option."
            github_handler.post_comment(error_message)
            logging.error(error_message)
            return
    else:
        summary_number = 1

    updated_files = []
    error_occurred = False

    async with aiohttp.ClientSession() as session:
        tasks = []
        for file in github_handler.pr.get_files():
            if file.filename.endswith('.md'):
                with open(file.filename, 'r') as md_file:
                    content = md_file.read()

                if match := re.match(
                    r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL
                ):
                    frontmatter, markdown_body = match.groups()
                    metadata = summary_handler.yaml.load(frontmatter)

                    if len(markdown_body) < 500:
                        message = f"Skipping summarization of file `{file.filename}` as the content is less than 500 characters."
                        logging.info(message)
                        github_handler.post_comment(message)
                        continue

                    if 'summary' not in metadata:
                        message = f"Skipping summarization of file `{file.filename}` as it doesn't have a summary field in the frontmatter."
                        github_handler.post_comment(message)
                        logging.warning(message)
                        continue

                    if overwrite_summaries or ('summary' in metadata and not metadata['summary']):
                        await rate_limiter.wait_for_token()
                        task = asyncio.create_task(summary_handler.get_summary(session, markdown_body, summary_number, summarize_endpoint))
                        tasks.append((file, task))
        try:
            summaries = await asyncio.gather(*[task for file, task in tasks])
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            github_handler.post_comment("An unexpected error occurred while trying to generate summaries. Please try again later.")
            return

    for (file, task), summary in zip(tasks, summaries):
        if summary:
            with open(file.filename, 'r') as md_file:
                content = md_file.read()
            if match := re.match(
                r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL
            ):
                frontmatter, _ = match.groups()
                metadata = summary_handler.yaml.load(frontmatter)
                existing_summary = (metadata.get('summary') or '').strip()
                generated_summary = summary.strip()

                if existing_summary == generated_summary:
                    message = f"The generated summary for `{file.filename}` is the same as the existing one. No update is necessary."
                    github_handler.post_comment(message)
                    logging.info(message)
                else:
                    summary_handler.update_file_summary(file, summary, overwrite=overwrite_summaries)
                    updated_files.append(file.filename)
        else:
            error_occurred = True
            logging.error(f'Summary not found or HTTP error for file: {file.filename}')
            github_handler.post_comment(f"Failed to generate a summary for file: `{file.filename}`. Please try again later.")

    if updated_files:
        summary_handler.commit_and_review(updated_files, github_handler)

if __name__ == "__main__":
    asyncio.run(main())