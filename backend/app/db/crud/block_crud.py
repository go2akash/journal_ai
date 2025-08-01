from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.block import Block
from app.schemas.block import BlockCreate


async def create_block(db: AsyncSession, data: BlockCreate):
    block = Block(
        id=uuid4(),
        page_id=data.page_id,
        user_id=data.user_id,
        parent_id=data.parent_id,
        type=data.type,
        content=data.content,
        position=data.position or 0,
    )

    db.add(block)
    await db.commit()
    await db.refresh(block)
    return block
