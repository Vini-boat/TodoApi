from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    assigned_to_user_id: Optional[int] = None
    due_to: Optional[datetime] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None
    created_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None


class TaskCreate(TaskBase):
    title: str

''
class TaskUpdate(TaskBase):
    title: str
    created_at: datetime


class TaskPatch(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: int
    completed: bool
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }
