import logging
from fastapi import FastAPI
from .database import Base, engine, SessionLocal
from .routers import news
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from .services.news_fetcher import fetch_news_periodically
from .config import settings
import os
# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()  # Logs to console
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(news.router)

# Initialize Scheduler
scheduler = AsyncIOScheduler()

def job_with_logging():
    logger.info("Scheduler job started.")
    db = SessionLocal()
    try:
        fetch_news_periodically(db)
        logger.info("Scheduler job completed successfully.")
    except Exception as e:
        logger.error(f"Scheduler job failed: {e}")
    finally:
        db.close()


@app.on_event("startup")
async def startup_event():
    logger.info(f"NEWS_FETCH_INTERVAL from os.environ: {os.environ.get('NEWS_FETCH_INTERVAL')}")
    logger.info(f"Job interval from settings: {settings.NEWS_FETCH_INTERVAL} minutes")
    # Add the job to the scheduler
    scheduler.add_job(
        job_with_logging,
        trigger=IntervalTrigger(minutes=settings.NEWS_FETCH_INTERVAL),
        id="fetch_news_job",
        replace_existing=True
    )
    scheduler.start()
    logger.info("Scheduler started.")

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
    logger.info("Scheduler stopped.")
