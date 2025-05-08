from pydantic import BaseModel
from typing import Optional

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None