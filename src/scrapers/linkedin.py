from loguru import logger
from linkedin_api import Linkedin
from src.config.settings import settings

class LinkedInScraper:
    def __init__(self):
        self.api = None
        self._login()

    def _login(self):
        try:
            # The python-linkedin-api library handles session caching automatically
            # internally, which is very helpful for avoiding bans.
            self.api = Linkedin(settings.LI_USERNAME, settings.LI_PASSWORD)
            logger.info("LinkedIn logged in successfully.")
        except Exception as e:
            logger.error(f"Failed to login to LinkedIn: {e}")

    def get_feed_posts(self, limit: int = 5) -> list:
        """
        Fetches posts from the user's feed.
        """
        logger.info(f"Fetching {limit} posts from LinkedIn feed...")
        try:
            feed = self.api.get_feed_posts(limit=limit)
            posts = []
            for post in feed:
                # Note: LinkedIn API structures can be complex. We are extracting the basic text payload.
                # Usually text is nested deeply inside `commentary` or `text` fields.
                # This is a simplified extraction example.
                
                post_id = post.get('id', '')
                author = post.get('actor', {}).get('name', {}).get('text', 'Unknown')
                
                # Try to extract the main text of the post
                content = ""
                commentary = post.get('commentary', {})
                if isinstance(commentary, dict):
                    content = commentary.get('text', {}).get('text', '')
                elif isinstance(commentary, str):
                    content = commentary
                    
                if not content:
                    continue  # Skip empty or non-text posts (like pure image posts)
                    
                posts.append({
                    "id": post_id,
                    "author": author,
                    "content": content,
                })
                
            return posts
        except Exception as e:
            logger.error(f"Failed to fetch LinkedIn feed: {e}")
            return []

    def post_comment(self, post_id: str, comment_text: str) -> bool:
        """
        Executes the comment action on LinkedIn.
        """
        try:
            # Note: To comment via `linkedin-api`, depending on the endpoint supported by the wrapper version.
            # Currently we need the URN of the post.
            self.api.add_post_comment(post_id, comment_text)
            return True
        except Exception as e:
            logger.error(f"Failed to comment on LI post {post_id}: {e}")
            return False
