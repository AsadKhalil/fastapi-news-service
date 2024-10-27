from sqlalchemy.orm import Session
from .models import News

def store_news(db: Session, title: str, digest: str, url: str, source: str, short_description: str):
    db_news = News(
        title=title, 
        digest=digest, 
        url=url, 
        source=source, 
        short_description=short_description
    )
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

def get_news(db: Session, skip: int = 0, limit: int = 10):
    return db.query(News).order_by(News.timestamp.desc()).offset(skip).limit(limit).all()
