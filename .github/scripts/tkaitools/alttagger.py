import asyncio
import aiohttp
import logging
import os
import re
from tkaiutils import GitHubHandler, RateLimiter, commit_and_push

class ImageMetadataUpdater:
    """
    Handles the retrieval and updating of image metadata within markdown files.
    """
    async def get_image_metadata(self, session, markdown_content, alttag_endpoint):
        """
        Asynchronously retrieves image metadata for the given markdown content.
        
        Args:
            session (aiohttp.ClientSession): The aiohttp client session for making requests.
            markdown_content (str): The markdown content to scan for images.
            alttag_endpoint (str): The API endpoint for retrieving image metadata.
        
        Returns:
            dict or None: The image metadata if successful, otherwise None.
        """
        payload = {"text": markdown_content}
        try:
            async with session.post(alttag_endpoint, json=payload, timeout=60) as response:
                response.raise_for_status()
                try:
                    image_metadata_response = await response.json()
                    logging.info(f"Received image metadata: {image_metadata_response}")
                except Exception as e:
                    logging.error(f"Failed to parse JSON response: {e}")
                    return None

                # Validate the 'images' key in the response
                if 'images' not in image_metadata_response:
                    logging.error(f'The key "images" is missing in the JSON response.')
                    return None

                # Validate that each image metadata has the required fields
                for image_metadata in image_metadata_response['images']:
                    if not all(key in image_metadata for key in ['name', 'title', 'alt-tag']):
                        logging.error(f'Some image metadata is missing required fields.')
                        return None

                logging.info('Received image metadata successfully.')
                return image_metadata_response['images']

        except asyncio.TimeoutError:
            logging.error('Request to /alttagger endpoint timed out')
        except aiohttp.ClientResponseError as e:
            logging.error(f'HTTP Response Error: {e.status} - {e.message}')
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

    def update_image_metadata(self, markdown_content, image_metadata):
        """
        Updates the alt-text and title for each image in the markdown content based on the provided metadata.
        
        Args:
            markdown_content (str): The original markdown content containing images.
            image_metadata (list of dict): A list of metadata dictionaries for each image.
        
        Returns:
            str: The markdown content with updated image metadata.
        """
        images_not_updated = []  # List to keep track of images not updated

        def replacement(match):
            image_path = match.group(2)
            image_name = os.path.basename(image_path)
            metadata = next((img for img in image_metadata if img['name'] == image_name), None)
            if metadata and metadata.get('confidence_score', 0) >= 0.7:
                new_alt_text = metadata.get('alt-tag', '')
                new_title_text = metadata.get('title', '')
                # Ensure the title is included even if it wasn't present before
                return f'![{new_alt_text}]({image_path} "{new_title_text}")'
            else:
                images_not_updated.append(image_name)
                return match.group(0)

        pattern = re.compile(r'!\[(.*?)\]\((.*?)\s*(?:\"(.*?)\")?\)')
        updated_markdown_content = pattern.sub(replacement, markdown_content)
        return updated_markdown_content, images_not_updated

async def main():
    """
    The main asynchronous function to run the script. Handles initialization, processing, and cleanup.
    """
    github_token = os.getenv('GITHUB_TOKEN')
    repo_name = os.getenv('GITHUB_REPOSITORY')
    pr_number = int(os.getenv('PR_NUMBER'))
    alttag_endpoint = os.getenv('ALTTAG_ENDPOINT')

    github_handler = GitHubHandler(github_token, repo_name, pr_number)
    metadata_updater = ImageMetadataUpdater()
    rate_limiter = RateLimiter(20, 60)

    updated_files = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for file in github_handler.pr.get_files():
            if file.filename.endswith('.md'):
                with open(file.filename, 'r', encoding='utf-8') as md_file:
                    markdown_content = md_file.read()

                image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\s*(?:\"(.*?)\")?\)')
                images = image_pattern.findall(markdown_content)

                if not images:
                    logging.info(f"No images found in {file.filename}, skipping.")
                    continue

                if all(alt and title for alt, _, title in images):
                    logging.info(f"All images in {file.filename} have non-empty alt tags and titles, skipping.")
                    continue

                await rate_limiter.wait_for_token()
                task = asyncio.create_task(
                    metadata_updater.get_image_metadata(session, markdown_content, alttag_endpoint)
                )
                tasks.append((file, task, markdown_content))

        responses = await asyncio.gather(*[t[1] for t in tasks], return_exceptions=True)

    for (file, _, original_content), response in zip(tasks, responses):
        if isinstance(response, Exception):
            logging.error(f'An error occurred for file {file.filename}: {str(response)}')
            github_handler.post_comment(f"Failed to update image metadata for file: `{file.filename}`. Please try again later.")
            continue

        if isinstance(response, list):
            updated_content, images_not_updated = metadata_updater.update_image_metadata(
                original_content, response
            )
            if updated_content != original_content:
                with open(file.filename, 'w', encoding='utf-8') as md_file:
                    md_file.write(updated_content)
                updated_files.append(file.filename)
            for image_name in images_not_updated:
                github_handler.post_comment(
                    f"Image `{image_name}` in file `{file.filename}` was not updated due to a low confidence score."
                )
        else:
            logging.error(f'Failed to fetch image metadata for {file.filename}')
            github_handler.post_comment(f"Failed to update image metadata for file: `{file.filename}`. Please try again later.")

        if updated_files:
            commit_message = "Update image metadata in " + file.filename
            commit_and_push(updated_files, commit_message)


        else:
            logging.info("No updated files to commit.")

    pr = github_handler.repo.get_pull(github_handler.pr.number)
    commit_obj = github_handler.repo.get_commit(pr.head.sha)

    for file_path in updated_files:
        review_message = "Please check the AI-generated alt-tag(s) in this file."
        github_handler.pr.create_review_comment(
            body=review_message,
            commit=commit_obj,
            path=file_path,
            subject_type='file'
        )               

if __name__ == "__main__":
    asyncio.run(main())