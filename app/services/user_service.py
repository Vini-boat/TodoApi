from app.dtos.user import UserResponse
from fastapi import Depends
from typing import Optional

from app.dtos.user import UserCreate, UserUpdate

from app.repository.sqlite_user_repository import SQLiteUserRepository

class UserService:
    def __init__(self, user_repository: SQLiteUserRepository = Depends(SQLiteUserRepository)):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        return self.user_repository.get_user(user_id)

    def get_active_user_by_id(self, user_id: int) -> Optional[UserResponse]:
        return self.user_repository.get_active_user(user_id)
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        return self.user_repository.create_user(user_data)

    def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
        return self.user_repository.update_user(user_id, user_data)

    def delete_user(self, user_id: int) -> Optional[UserResponse]:
        return self.user_repository.delete_user(user_id)