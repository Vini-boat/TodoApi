from app.dtos.user import UserCredentials, UserResponse
from fastapi import Depends
from app.dtos.user import UserCreate, UserUpdate
from app.repository.sqlite_user_repository import SQLiteUserRepository
from app.infraestructure.security import get_password_hash

from app.exceptions.domain import UserNotActive

class UserService:
    def __init__(self, user_repository: SQLiteUserRepository = Depends(SQLiteUserRepository)):
        self.user_repository = user_repository

    def create_user(self, user_data: UserCreate) -> UserResponse:
        user_data.password = get_password_hash(user_data.password)
        return self.user_repository.create_user(user_data)
    
    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.user_repository.get_user_by_id(user_id)
        if user.deleted:
            raise UserNotActive
        return user

    def get_user_by_email(self, email: str) -> UserResponse:
        user = self.user_repository.get_user_by_email(email)
        if user.deleted:
            raise UserNotActive
        return user 
    
    def get_user_credentials(self, email: str) -> UserCredentials:
        user = self.user_repository.get_user_by_email(email)
        if user.deleted:
            raise UserNotActive
        credentials = self.user_repository.get_user_login(email)
        return credentials
    
    def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        user = self.user_repository.update_user(user_id, user_data)
        if user.deleted:
            raise UserNotActive
        return user

    def delete_user(self, user_id: int) -> UserResponse:
        return self.user_repository.delete_user(user_id)