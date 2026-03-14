import time
import random
from datetime import datetime, date
from loguru import logger
from sqlalchemy.orm import Session
from src.db.models import PostHistory
from src.config.settings import settings

class Guardrails:
    def __init__(self, db_session: Session):
        self.db = db_session

    def is_safe_to_comment(self, platform: str, post_id: str, new_comment: str) -> bool:
        """
        Runs all safety checks before allowing a comment.
        """
        if self._is_post_already_processed(post_id):
            logger.info(f"Post {post_id} already processed. Skipping.")
            return False
            
        if self._is_daily_limit_reached():
            logger.warning(f"Daily limit of {settings.MAX_COMMENTS_PER_DAY} reached. Skipping.")
            return False
            
        if self._is_comment_too_similar(new_comment):
            logger.warning("Generated comment is too similar to recent comments. Skipping.")
            return False

        # If it passed other checks, we check our new author requirement but we need the author param
        return True

    def is_author_recently_commented(self, author: str) -> bool:
        """
        Check if we commented on this author within the last 3 days.
        """
        from src.db.models import Author
        from datetime import timedelta
        
        author_record = self.db.query(Author).filter(Author.username == author).first()
        if author_record and author_record.author_last_commented:
            days_since = (datetime.utcnow() - author_record.author_last_commented).days
            if days_since < 3:
                logger.info(f"Commented on {author} recently ({days_since} days ago). Skipping.")
                return True
        return False

    def _is_post_already_processed(self, post_id: str) -> bool:
        return self.db.query(PostHistory).filter(PostHistory.post_id == post_id).first() is not None

    def _is_daily_limit_reached(self) -> bool:
        today_start = datetime.combine(date.today(), datetime.min.time())
        count = self.db.query(PostHistory).filter(PostHistory.created_at >= today_start).count()
        return count >= settings.MAX_COMMENTS_PER_DAY

    def _is_comment_too_similar(self, new_comment: str) -> bool:
        # Simple string-level overlap check for now to avoid heavy processing
        recent_comments = self.db.query(PostHistory.comment_content).order_by(PostHistory.id.desc()).limit(5).all()
        
        words_new = set(new_comment.lower().split())
        for r in recent_comments:
            words_old = set(r[0].lower().split())
            if not words_old or not words_new:
                continue
            intersection = words_new.intersection(words_old)
            overlap_ratio = len(intersection) / len(words_new)
            if overlap_ratio > 0.6:  # If 60% of words are the same, reject
                return True
        return False
        
    def wait_random_delay(self):
        """Sleeps for a random duration to simulate human behavior."""
        delay = random.randint(settings.DELAY_MIN_SECONDS, settings.DELAY_MAX_SECONDS)
        logger.info(f"Sleeping for {delay} seconds to simulate human behavior...")
        time.sleep(delay)
