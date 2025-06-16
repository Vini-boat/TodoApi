from fastapi import Depends
from sqlalchemy import insert, update
from app.dtos.user import UserCredentials, UserResponse, UserCreate, UserUpdate
from app.infraestructure.sqlite import get_db_session

from sqlalchemy.orm import Session

from app.models.user import User
from sqlalchemy.exc  import IntegrityError 
from app.exceptions.domain import UserAlreadyExists, UserNotFound

class SQLiteUserRepository:
    def __init__(self, db_session: Session = Depends(get_db_session)):
        self.session: Session = db_session
        self.user_response_colums = [col for col in User.__table__.c if col.name in UserResponse.model_fields]

    def create_user(self, user_data: UserCreate) -> UserResponse:
        stmt = (
            insert(User)
            .values(user_data.model_dump())
            .returning(*self.user_response_colums)
        )
        try:
            created_user = self.session.execute(stmt).first()
        except IntegrityError as e:
            self.session.rollback()
            raise UserAlreadyExists("Email already in use") from e
        self.session.commit()
        return UserResponse.model_validate(created_user) 

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.session.query(User).filter(User.id == user_id).first()
        
        if not user: 
            raise UserNotFound(f"User with id {user_id} not found")
        
        return UserResponse.model_validate(user)
    
    def get_user_by_email(self, email: str) -> UserResponse:
        user = self.session.query(User).filter(User.email == email).first()
        
        if not user: 
            raise UserNotFound(f"User with email {email} not found")

        return UserResponse.model_validate(user)
    
    def get_user_login(self, email: str) -> UserResponse:
        user = self.session.query(User).filter(User.email == email).first()
        
        if not user:
            raise UserNotFound(f"User with email {email} not found")
        
        return UserCredentials.model_validate(user)

    def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(user_data.model_dump())
            .returning(*self.user_response_colums)
        )
        updated_user = self.session.execute(stmt).first()
        if not updated_user:
            self.session.rollback()
            raise UserNotFound(f"User with id {user_id} not found")
        self.session.commit()
        return UserResponse.model_validate(updated_user)

    def delete_user(self, user_id: int) -> UserResponse:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(deleted=True)
            .returning(*self.user_response_colums)
        )
        deleted_user = self.session.execute(stmt).first()
        if not deleted_user:
            self.session.rollback()
            raise UserNotFound(f"User with id {user_id} not found")
        self.session.commit()
        return UserResponse.model_validate(deleted_user)