from uuid import uuid4

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.users import Users
from app.schemas.user import UserCreate


async def create_user(db: AsyncSession, data: UserCreate):
    user = Users(
        id=uuid4(),
        username=data.username,
        name=data.name,
        email=data.email,
        password=data.password,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
