from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# WHY: isso é necessário para evitar o erro de importação circular
# https://github.com/sqlalchemy/sqlalchemy/discussions/9223#discussioncomment-4852967
from .user import User
from .task import Task
# WHY: isso é necessário para evitar o erro de importação circular