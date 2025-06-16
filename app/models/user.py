from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base

# WHY: isso é necessário para evitar o erro de importação circular
# https://github.com/sqlalchemy/sqlalchemy/discussions/9223#discussioncomment-4852967
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import Task, Comment
# WHY: isso é necessário para evitar o erro de importação circular

from typing import Optional

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    deleted: Mapped[bool] = mapped_column(default=False)

    tasks: Mapped[Optional["Task"]] = relationship(back_populates="assigned_to")

    comments: Mapped[list["Comment"]] = relationship(back_populates="user")


