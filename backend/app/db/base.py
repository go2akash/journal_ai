import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

load_dotenv()

DB_URL = os.getenv("DB_URL")

if DB_URL is None:
    raise ValueError("Environment variable DB_URL is not set!")
engine = create_async_engine(DB_URL, echo=True)


SessionLocal = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


async def get_db():
    async with SessionLocal() as db:
        yield db


class Base(DeclarativeBase):
    pass
