from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.journal_page import JournalPage
from app.schemas.journal_page import JournalCreate
from uuid import uuid4


async def CreateJournalPage(db:AsyncSession,data:JournalCreate):
    journalpage=JournalPage(
        id=uuid4(),
        title=data.title,
        userid=data.userid,
        journal_date=data.journal_date,        
    )

    db.add(journalpage)
    await db.commit()
    await db.refresh(journalpage)
    return journalpage
