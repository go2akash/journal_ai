from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class JournalBase(BaseModel):
    user_id: str
    title: Optional[str] = None
    journal_date: date = Field(default_factory=date.today)


class JournalCreate(JournalBase):
    pass


class JournalRead(JournalBase):
    created_at: datetime

    class Config:
        orm_mode = True
