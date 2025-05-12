from typing import Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base

# WHY: isso é necessário para evitar o erro de importação circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import User


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(255))
    completed: Mapped[bool] = mapped_column(default=False)
    assigned_to_user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))

    assigned_to: Mapped[Optional["User"]] = relationship(back_populates="tasks")