from typing import Optional
from pydantic import BaseModel, EmailStr

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    deleted: bool
    model_config = {
        "from_attributes": True,
    }

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    username: str
    email: EmailStr

class UserPatch(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    deleted: Optional[bool] = None

class UserCredentials(BaseModel):
    email: str
    password: str
    model_config = {
        "from_attributes": True,
    }