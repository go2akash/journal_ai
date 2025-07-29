from db.base import engine , Base
from db.models.users import Users
import asyncio
from db.models.block import Block
from db.models.journal_page import JournalPage
from db.models.users import Users

__all__ = ["Block", "Users", "JournalPage"]

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(init_db())