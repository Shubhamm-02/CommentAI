import os
from loguru import logger
from instagrapi import Client
from src.config.settings import settings

class InstagramScraper:
    def __init__(self):
        self.client = Client()
        self.session_file = os.path.join(settings.BASE_DIR, "data", "ig_session.json")
        self._login()

    def _login(self):
        try:
            if os.path.exists(self.session_file):
                self.client.load_settings(self.session_file)
                self.client.login(settings.IG_USERNAME, settings.IG_PASSWORD)
                logger.info("Instagram logged in using session file.")
            else:
                self.client.login(settings.IG_USERNAME, settings.IG_PASSWORD)
                self.client.dump_settings(self.session_file)
                logger.info("Instagram logged in and new session saved.")
        except Exception as e:
            logger.error(f"Failed to login to Instagram: {e}")

    def get_recent_posts_by_hashtag(self, hashtag: str, amount: int = 5) -> list:
        """
        Fetches recent posts for a specific hashtag.
        Returns a list of dictionaries with post details.
        """
        logger.info(f"Fetching {amount} recent posts for #{hashtag}...")
        try:
            medias = self.client.hashtag_medias_top(hashtag, amount=amount)
            posts = []
            for media in medias:
                posts.append({
                    "id": str(media.pk),
                    "author": media.user.username,
                    "content": media.caption_text,
                    "url": f"https://www.instagram.com/p/{media.code}/"
                })
            return posts
        except Exception as e:
            logger.error(f"Failed to fetch posts for hashtag {hashtag}: {e}")
            return []

    def post_comment(self, post_id: str, comment_text: str) -> bool:
        """
        Executes the comment action on Instagram.
        """
        try:
            self.client.media_comment(post_id, comment_text)
            return True
        except Exception as e:
            logger.error(f"Failed to comment on IG post {post_id}: {e}")
            return False
