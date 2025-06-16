from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from . import Base
from datetime import datetime
from typing import Optional

# WHY: isso é necessário para evitar o erro de importação circular
# https://github.com/sqlalchemy/sqlalchemy/discussions/9223#discussioncomment-4852967
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import User, Task
# WHY: isso é necessário para evitar o erro de importação circular

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(VARCHAR(500))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), default=None)

    task: Mapped["Task"] = relationship(back_populates="comments")
    user: Mapped[Optional["User"]] = relationship(back_populates="comments")
