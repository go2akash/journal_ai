from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.journal_page import JournalCreate
from app.db.crud.journal_page_crud import CreateJournalPage
from app.db.base import get_db

router = APIRouter()

@router.post("/")
async def create_new_journal(
    data: JournalCreate,
    db: AsyncSession = Depends(get_db)
):
    return await CreateJournalPage(db, data)
