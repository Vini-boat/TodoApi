from app.schemas.user import UserResponse
from app.interfaces.user_repository import IUserRepository
from fastapi import Depends

class UserService:
    def __init__(self, user_repository: IUserRepository = Depends()):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id) -> UserResponse:
        return self.user_repository.get_user_by_id(user_id)

    def create_user(self, user_data):
        return self.user_repository.create_user(user_data)

    def update_user(self, user_id, user_data):
        return self.user_repository.update_user(user_id, user_data)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)