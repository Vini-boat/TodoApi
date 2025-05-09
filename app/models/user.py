from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base

from typing import Optional

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))

    tasks: Mapped[Optional["Task"]] = relationship(back_populates="assigned_to", cascade="all, delete-orphan")

