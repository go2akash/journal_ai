import uuid
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from .journal_page import JournalPage


class Block(Base):
    __tablename__ = "blocks"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    page_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("journal_pages.id"), nullable=False
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    ## Tracking the nested blocks
    parent_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("blocks.id"), nullable=True
    )

    type: Mapped[str] = mapped_column(String(50))  ## paragraph todos
    content: Mapped[dict] = mapped_column(JSONB)
    position: Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )

    ## Relationship

    page: Mapped["JournalPage"] = relationship("JournalPage", back_populates="blocks")
    parent: Mapped["Block | None"] = relationship(
        "Block", remote_side="Block.id", backref="children"
    )
