import asyncio
import logging
import subprocess
import time
from github import Github
import os

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
            
class RateLimiter:
    """
    A simple rate limiter to control the rate of API calls.
    
    Attributes:
        rate (int): The number of calls allowed per time period.
        per (float): The time period for rate limiting in seconds.
        allowance (float): The current number of available tokens.
        last_check (float): The time of the last rate limit check.
    """
    def __init__(self, rate, per):
        """
        Initializes the RateLimiter with a specified rate and time period.
        
        Args:
            rate (int): The number of calls allowed per time period.
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

def commit_and_push(updated_files, commit_message):
    """
    Adds, commits, and pushes updated files to the git repository.

    This function configures the git user details for the commit, checks if there are any changes, stages the changes if they exist, creates a commit with the specified message, and pushes the commit to the current branch of the remote repository. If no changes are detected, it skips the commit and logs an informational message.

    Args:
        updated_files (list of str): The file paths that have been updated  and need to be committed.
        commit_message (str): The message for the git commit.

    Returns:
        bool: True if changes were committed and pushed, False otherwise.
    """
    try:
        subprocess.run(['git', 'config', 'user.name', 'KnowOps'], check=True)
        subprocess.run(['git', 'config', 'user.email', 'knowledge@outsystems.com'], check=True)

        repo_url = f"https://{os.getenv('TOOLS_PAT')}@github.com/{os.getenv('GITHUB_REPOSITORY')}.git"
        subprocess.run(['git', 'remote', 'set-url', 'origin', repo_url], check=True)
        
        status_result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if status_result.stdout:
            subprocess.run(['git', 'add'] + updated_files, check=True)
            
            commit_result = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
            if commit_result.returncode != 0:
                logging.error(f'Git commit failed: {commit_result.stderr}')
                return False
            
            subprocess.run(['git', 'push'], check=True)
            return True
        else:
            logging.info('No changes detected, skipping commit.')
            return False
    except subprocess.CalledProcessError as e:
        logging.error(f'An error occurred while processing git commands: {e}')
        return False