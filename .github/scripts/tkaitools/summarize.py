import asyncio
import aiohttp
import logging
import os
import re
import time
from io import StringIO
from ruamel.yaml import YAML
from tkaiutils import GitHubHandler, RateLimiter, commit_and_push

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
            async with session.post(summarize_endpoint, json=payload, timeout=120) as response:
                response.raise_for_status()  # This will raise an exception for HTTP errors
                summary_data = await response.json()

                # Validate the 'summary' key in the response
                summary_key = f"Summary{summary_number}"
                if summary_key in summary_data:
                    summary = summary_data[summary_key].get("summary")
                    if summary is not None:
                        logging.info('Received summary: %s', summary)
                        return summary
                    else:
                        logging.error('Summary key found but summary text is missing')
                else:
                    logging.error(f'Expected key {summary_key} is missing in the JSON response')
                    
        except asyncio.TimeoutError:
            logging.error('Request to /summarize endpoint timed out')
        except aiohttp.ClientResponseError as e:
            logging.error(f'HTTP Response Error: {e}')
        except Exception as e:
            logging.error(f'An unexpected error occurred: {e}')

    def update_summary(self, file, summary, overwrite=False):
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

async def main():
    """
    The main asynchronous function to run the script. Handles initialization, processing, and cleanup.
    """
    github_token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('GITHUB_REPOSITORY')
    pr_number = int(os.getenv('PR_NUMBER'))
    comment_id = os.getenv('COMMENT_ID')
    comment_body = os.getenv('COMMENT_BODY', '')
    summarize_endpoint = os.getenv('SUMMARIZE_ENDPOINT')

    github_handler = GitHubHandler(github_token, repo_name, pr_number)
    summary_handler = SummaryHandler()
    rate_limiter = RateLimiter(5, 60)

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
                        message = f"Skipping summarization of file `{file.filename}` as content is less than 500 characters."
                        logging.info(message)
                        github_handler.post_comment(message)
                        continue

                    if 'summary' not in metadata:
                        message = f"Skipping summarization of file `{file.filename}` as it does not have a summary field in the frontmatter."
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

                if 'summary' not in metadata:
                    message = f"`{file.filename}` does not have a summary field in the frontmatter, skipping summary generation."
                    github_handler.post_comment(message)
                    logging.warning(message)
                elif existing_summary == generated_summary:
                    message = f"The generated summary for `{file.filename}` is the same as the existing one. No update is necessary."
                    github_handler.post_comment(message)
                    logging.info(message)
                else:
                    summary_handler.update_summary(file, summary, overwrite=overwrite_summaries)
                    updated_files.append(file.filename)
        else:
            logging.error(f'Summary not found or HTTP error for file: {file.filename}')
            github_handler.post_comment(f"Failed to generate a summary for file: `{file.filename}`. Please try again later.")

    if updated_files:
        commit_message = 'Update summary fields'
        if commit_and_push(updated_files, commit_message):
            review_message = "Please check this AI-generated summary. To regenerate, use the `/summarize` command."
            time.sleep(5) # Wait for the commit to be processed by GitHub
            for file_path in updated_files:
                github_handler.post_review_comment(file_path, review_message)

if __name__ == "__main__":
    asyncio.run(main())