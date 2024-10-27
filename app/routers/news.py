from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..crud import get_news
from ..schemas import NewsResponse

router = APIRouter()

@router.get("/news", response_model=list[NewsResponse])
def read_news(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    news = get_news(db, skip=skip, limit=limit)
    if not news:
        raise HTTPException(status_code=404, detail="No news found")
    return news
