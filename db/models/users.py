from db.base import  Base
from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy import String, DateTime, func
from uuid import uuid4
from datetime import datetime
import uuid



class Users(Base):
    __tablename__ = "users"
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    username:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password:Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())


