# from pydantic import BaseSettings
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    NEWS_FETCH_INTERVAL: int
    NEWS_API_URL: str
    TWITTER_ACCOUNTS: List[str] = []  

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
