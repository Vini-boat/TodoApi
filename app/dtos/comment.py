from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CommentResponse(BaseModel):
    id: int
    task_id: int
    user_id: Optional[int]
    content: str
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }

class CommentCreate(BaseModel):
    task_id: int
    content: str

class CommentUpdate(BaseModel):
    content: str