from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base import get_db
from app.db.crud.user_crud import create_user
from app.schemas.user import UserCreate

router = APIRouter()


@router.post("/")
async def create_new_user(data: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, data)
