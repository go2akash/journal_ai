from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.db.crud.user_crud import create_user
from app.db.base import get_db

router = APIRouter()

@router.post("/")
async def create_new_user(
    data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_user(db, data)
