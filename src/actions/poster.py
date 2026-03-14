from loguru import logger
from sqlalchemy.orm import Session
from src.db.models import PostHistory
from src.actions.guardrails import Guardrails

class ActionPoster:
    def __init__(self, db_session: Session):
        self.db = db_session
        self.guard = Guardrails(db_session)

    def execute_comment(self, platform: str, post_id: str, author: str, comment: str, api_executor_func: callable) -> bool:
        """
        Validates through guardrails and executes the comment using the provided API wrapper function.
        """
        logger.info(f"Attempting to comment on {platform} post {post_id} by {author}.")
        
        if not self.guard.is_safe_to_comment(platform, post_id, comment):
            return False
            
        if self.guard.is_author_recently_commented(author):
            return False
            
        # Simulate human delay before acting
        self.guard.wait_random_delay()
        
        # Execute platform-specific API function
        try:
            success = api_executor_func(post_id, comment)
            if success:
                self._record_success(platform, post_id, author, comment)
                logger.success(f"Successfully posted comment on {post_id}.")
                return True
            else:
                logger.error(f"Failed to post comment on {post_id}.")
                return False
        except Exception as e:
            logger.error(f"Exception during posting: {e}")
            return False

    def _record_success(self, platform: str, post_id: str, author: str, comment: str):
        from src.db.models import Author
        from datetime import datetime
        
        history = PostHistory(
            platform=platform,
            post_id=post_id,
            author_username=author,
            comment_content=comment
        )
        self.db.add(history)
        
        author_record = self.db.query(Author).filter(Author.username == author).first()
        if author_record:
            author_record.author_last_commented = datetime.utcnow()
        else:
            new_author = Author(username=author, author_last_commented=datetime.utcnow())
            self.db.add(new_author)
            
        self.db.commit()
