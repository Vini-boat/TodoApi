from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user_service import UserService

router = APIRouter()

@router.post("/auth/login")
async def todo_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(UserService)
    ):
    
    return "todo: jwt token"

@router.post("/auth/logout")
async def todo_logout():
    return "todo: logout"