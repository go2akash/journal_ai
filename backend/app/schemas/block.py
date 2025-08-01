from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BlockCreate(BaseModel):
    page_id: UUID
    user_id: UUID
    parent_id: Optional[UUID] = None
    type: str
    content: dict
    position: Optional[int] = 0


class BlockRead(BaseModel):
    id: UUID
    page_id: UUID
    user_id: UUID
    parent_id: Optional[UUID]
    type: str
    content: dict
    position: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
