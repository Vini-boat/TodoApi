from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.infraestructure.security import verify_password
from app.services.user_service import UserService
from app.exceptions.http import InvalidCredentials

router = APIRouter()

@router.post("/auth/login")
async def todo_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(UserService)
    ):
    user = service.get_user_login(form_data.username)
    if not user:
        raise InvalidCredentials
    if not verify_password(form_data.password, user.password):
        raise InvalidCredentials
    
    return {"access_token": user.email, "token_type": "bearer"}

@router.post("/auth/logout")
async def todo_logout():
    return "todo: logout"