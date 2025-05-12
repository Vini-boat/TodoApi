from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# WHY: isso é necessário para evitar o erro de importação circular
from .user import User
from .task import Task
