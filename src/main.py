import sys
from pathlib import Path

# Add the project root directory to Python's path so 'src' can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import time
import schedule
from loguru import logger
from src.db.database import init_db, SessionLocal
from src.scrapers.instagram import InstagramScraper
from src.scrapers.linkedin import LinkedInScraper
from src.ai.generator import CommentGenerator
from src.actions.poster import ActionPoster

def run_agent_job():
    logger.info("Starting agent cycle...")
    
    # Initialize components
    db_session = SessionLocal()
    poster = ActionPoster(db_session)
    generator = CommentGenerator()
    
    # Initialize scrapers lazily per cycle to handle fresh sessions
    ig_scraper = InstagramScraper()
    li_scraper = LinkedInScraper()

    # --- Instagram Routine ---
    logger.info("Executing Instagram routine...")
    ig_posts = ig_scraper.get_recent_posts_by_hashtag("aiengineering", amount=3)
    for post in ig_posts:
        comment = generator.generate_networking_comment(post['content'], "Instagram")
        if comment:
            poster.execute_comment(
                platform="instagram",
                post_id=post['id'],
                author=post['author'],
                comment=comment,
                api_executor_func=ig_scraper.post_comment
            )
            
    # --- LinkedIn Routine ---
    logger.info("Executing LinkedIn routine...")
    li_posts = li_scraper.get_feed_posts(limit=3)
    for post in li_posts:
        comment = generator.generate_networking_comment(post['content'], "LinkedIn")
        if comment:
            poster.execute_comment(
                platform="linkedin",
                post_id=post['id'],
                author=post['author'],
                comment=comment,
                api_executor_func=li_scraper.post_comment
            )
            
    # --- Mentions & Replies Routine ---
    logger.info("Executing Replies routine...")
    # NOTE: Scraping mentions and replying requires specific API calls (e.g., getting latest notifications).
    # Since we are using session wrappers, you can utilize:
    # ig_scraper.client.notifications() or li_scraper.api.get_conversations() 
    # and feed the text into generator.generate_networking_comment() to post a reply.
    # This is a scaffolding block for that feature:
    
    # recent_notifications = ig_scraper.get_recent_mentions()
    # for mention in recent_notifications:
    #     reply_comment = generator.generate_networking_comment(mention['text'], "Instagram_Reply")
    #     if reply_comment:
    #         poster.execute_comment(..., reply_comment, ...)
            
    db_session.close()
    logger.info("Agent cycle complete.")

def main():
    logger.add("logs/agent_{time}.log", rotation="1 day", retention="7 days")
    logger.info("Initializing Database...")
    init_db()
    
    logger.info("Starting CommentAI Agent...")
    
    # Run once immediately on start
    run_agent_job()
    
    # Schedule to run every 90 minutes
    schedule.every(90).minutes.do(run_agent_job)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
