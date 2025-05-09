from fastapi import Depends
from sqlalchemy import insert
from app.dtos.user import UserResponse, UserCreate, UserUpdate
from app.infraestructure.sqlite import get_db_session

from sqlalchemy.orm import Session

from app.models.user import User

class SQLiteUserRepository():
    def __init__(self, db_session: Session = Depends(get_db_session)):
        self.session: Session = db_session
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        stmt = insert(User).values(user_data.model_dump()).returning(User.id, User.username, User.email)
        created_user = self.session.execute(stmt).first()
        self.session.commit()
        return UserResponse.model_validate(created_user) 

    def get_user(self, user_id: int) -> UserResponse:
        return UserResponse()

    def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        return UserResponse()

    def delete_user(self, user_id: int) -> UserResponse:
        return UserResponse()