from pydantic import BaseModel,Field
from datetime import datetime,date
from typing import List,Optional



class JournalBase(BaseModel):
    userid:str 
    title: Optional[str] =None
    journal_date: date = Field(default_factory=date.today)

class JournalCreate(JournalBase):
    pass

class JournalRead(JournalBase):
    created_at:datetime
    class Config:
        orm_mode = True
