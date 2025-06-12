from fastapi import APIRouter, Depends
from app.services.user_service import UserService

from app.dtos.user import UserResponse, UserCreate, UserUpdate
from app.infraestructure.auth import get_current_user
from app.exceptions.http import UserNotFound

router = APIRouter()

@router.get("/users/me", response_model=UserResponse)
async def get_current_user(
    current_user: UserResponse = Depends(get_current_user)
    ):
    return current_user

@router.post("/users", response_model=UserResponse)
async def create_new_user(
    user: UserCreate, 
    service: UserService = Depends(UserService),
    ):
    created_user = service.create_user(user)
    return created_user

@router.get("/users/{user_id}",response_model=UserResponse)
async def get_user_by_id(
    user_id: int, 
    service: UserService = Depends(UserService)
    ):
    user = service.get_user_by_id(user_id)
    if not user:
        raise UserNotFound
    return user

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int, 
    user: UserUpdate, 
    service: UserService = Depends(UserService)
    ):
    updated_user = service.update_user(user_id, user)
    if not updated_user:
        raise UserNotFound
    return updated_user

@router.delete("/users/{user_id}", response_model=UserResponse)
async def delete_user(
    user_id: int, 
    service: UserService = Depends(UserService)
    ):
    deleted_user = service.delete_user(user_id)
    if not deleted_user:
        raise UserNotFound
    return deleted_user