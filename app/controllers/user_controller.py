from fastapi import APIRouter, Depends
from app.services.user_service import UserService

from app.dtos.user import UserResponse, UserCreate, UserUpdate
from app.infraestructure.auth import get_current_user


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
    return service.get_user_by_id(user_id)

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int, 
    user: UserUpdate, 
    service: UserService = Depends(UserService)
    ):
    return service.update_user(user_id, user)

@router.delete("/users/{user_id}", response_model=UserResponse)
async def delete_user(
    user_id: int, 
    service: UserService = Depends(UserService)
    ):
    return service.delete_user(user_id)