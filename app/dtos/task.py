from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    assigned_to_user_id: Optional[int] = None
    created_at: datetime
    completed_at: Optional[datetime] = None
    due_to: Optional[date] = None
    priority: Optional[int] = None
    
    model_config = {
        "from_attributes": True,
    }

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to_user_id: Optional[int] = None
    due_to: Optional[date] = None
    priority: Optional[int] = None


class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    assigned_to_user_id: Optional[int] = None
    due_to: Optional[date] = None
    priority: Optional[int] = None

class TaskPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    assigned_to_user_id: Optional[int] = None
    due_to: Optional[date] = None
    priority: Optional[int] = None

class TaskFilter(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None
    assigned_to_user_id: Optional[int] = None

    created_before: Optional[datetime] = None
    created_after: Optional[datetime] = None

    completed_before: Optional[datetime] = None
    completed_after: Optional[datetime] = None

    due_before: Optional[date] = None
    due_after: Optional[date] = None
    
    min_priority: Optional[int] = None
    max_priority: Optional[int] = None