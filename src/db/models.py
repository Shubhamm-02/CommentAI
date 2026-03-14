from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PostHistory(Base):
    """
    Records posts that we have already processed/commented on to avoid duplicates.
    """
    __tablename__ = "post_history"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, index=True) # 'instagram' or 'linkedin'
    post_id = Column(String, unique=True, index=True)
    author_username = Column(String)
    comment_content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<PostHistory(platform={self.platform}, post_id={self.post_id}, author={self.author_username})>"

class Author(Base):
    """
    Records the last time we commented on a specific author.
    """
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    author_last_commented = Column(DateTime)
    
    def __repr__(self):
        return f"<Author(username={self.username}, last_commented={self.author_last_commented})>"
