from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.block import BlockCreate, BlockRead
from app.db.crud.block_crud import create_block
from app.db.base import get_db

router = APIRouter()

@router.post("/", response_model=BlockRead)
async def create_new_block(
    data: BlockCreate,
    db: AsyncSession = Depends(get_db)
):
    return await create_block(db, data)
