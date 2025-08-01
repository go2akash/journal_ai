import uuid
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import Date, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from .block import Block


class JournalPage(Base):
    __tablename__ = "journal_pages"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    userid: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, server_default=func.now()
    )
    journal_date: Mapped[datetime] = mapped_column(Date, nullable=False)

    ## Relationship
    blocks: Mapped[list["Block"]] = relationship(
        "Block", back_populates="page", cascade="all, delete"
    )
