import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings
from src.db.models import Base

# Ensure the database directory exists
db_dir = os.path.dirname(os.path.join(settings.BASE_DIR, settings.DB_PATH))
os.makedirs(db_dir, exist_ok=True)

# Create sqlite engine
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(settings.BASE_DIR, settings.DB_PATH)}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    from src.db import models
    Base.metadata.create_all(bind=engine)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
