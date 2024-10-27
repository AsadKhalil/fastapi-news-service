from pydantic import BaseModel
from datetime import datetime

class NewsBase(BaseModel):
    title: str
    digest: str
    url: str
    source: str
    short_description: str

class NewsResponse(NewsBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
