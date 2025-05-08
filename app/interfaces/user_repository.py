from abc import ABC, abstractmethod

from app.dtos.user import UserResponse, UserCreate, UserUpdate

class IUserRepository(ABC):
    @abstractmethod
    def create_user(self, user_id: int, user: UserCreate) -> UserResponse:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, user_id: int) -> UserResponse:
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id: int):
        raise NotImplementedError