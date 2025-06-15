from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    assigned_to_user_id: Optional[int] = None
    created_at: datetime
    completed_at: Optional[datetime] = None
    due_to: Optional[datetime] = None
    priority: Optional[int] = None
    
    model_config = {
        "from_attributes": True,
    }

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to_user_id: Optional[int] = None
    due_to: Optional[datetime] = None
    priority: Optional[int] = None


class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    assigned_to_user_id: Optional[int] = None
    created_at: datetime
    due_to: Optional[datetime] = None
    priority: Optional[int] = None

class TaskPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    assigned_to_user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    due_to: Optional[datetime] = None
    priority: Optional[int] = None