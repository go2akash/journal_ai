from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import get_db
from app.db.crud.journal_page_crud import create_journal_page
from app.schemas.journal_page import JournalCreate

router = APIRouter()


@router.post("/")
async def create_new_journal(data: JournalCreate, db: AsyncSession = Depends(get_db)):
    return await create_journal_page(db, data)
