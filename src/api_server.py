from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from src.db.database import SessionLocal, init_db
from src.db.models import PostHistory, Author
from src.config.settings import settings
import os
import uvicorn

app = FastAPI(title="CommentAI Dashboard API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB on startup
@app.on_event("startup")
def on_startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/stats")
def get_stats():
    db = SessionLocal()
    total_comments = db.query(PostHistory).count()
    total_authors = db.query(Author).count()
    db.close()
    return {
        "total_comments": total_comments,
        "unique_authors": total_authors,
        "daily_limit": settings.MAX_COMMENTS_PER_DAY
    }

@app.get("/api/history")
def get_history(limit: int = 10):
    db: Session = SessionLocal()
    history = db.query(PostHistory).order_by(PostHistory.created_at.desc()).limit(limit).all()
    db.close()
    return [
        {
            "id": h.id,
            "platform": h.platform,
            "author": h.author_username,
            "post_id": h.post_id,
            "comment": h.comment_content,
            "time": h.created_at
        } for h in history
    ]

# Serve the Vite Frontend Build
dashboard_path = os.path.join(settings.BASE_DIR, "SaaS dashboard landing page", "dist")
if os.path.exists(dashboard_path):
    app.mount("/", StaticFiles(directory=dashboard_path, html=True), name="dashboard")

if __name__ == "__main__":
    uvicorn.run("src.api_server:app", host="127.0.0.1", port=8000, reload=True)
