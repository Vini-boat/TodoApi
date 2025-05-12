from pydantic import BaseModel
from typing import Optional

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    assigned_to_user_id: Optional[int] = None

    model_config = {
        "from_attributes": True,
    }

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assigned_to_user_id: Optional[int] = None

class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    assigned_to_user_id: Optional[int] = None