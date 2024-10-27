import httpx
from sqlalchemy.orm import Session
from ..crud import store_news
from ..config import settings
import logging

logger = logging.getLogger(__name__)

async def fetch_and_store_news(db: Session, limit: int = 10):
    print("Fetching news")
    url = settings.NEWS_API_URL.format(limit=limit)
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0",
    }

    logger.info("Fetching news from external API...")
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            if data.get('code') == "200":
                news_items = data.get('data', {}).get('list', [])
                for item in news_items:
                    title = item.get("title", "No Title")
                    digest = item.get("digest", "No Digest")
                    url = item.get("url", "No URL")
                    source = item.get("source", "Unknown Source")
                    short_description = item.get("short", "No Short Description")

                    store_news(db, title, digest, url, source, short_description)
                logger.info(f"Fetched and stored {len(news_items)} news items.")
            else:
                logger.error(f"Error in response: {data.get('msg', 'Unknown Error')}")
        else:
            logger.error(f"Failed to fetch news. Status code: {response.status_code}")

def fetch_news_periodically(db: Session):
    import asyncio
    asyncio.run(fetch_and_store_news(db))
