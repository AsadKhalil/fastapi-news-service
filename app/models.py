from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    digest = Column(String)
    url = Column(String)
    source = Column(String)
    short_description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
