from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.dtos.user import UserCredentials
from app.infraestructure.auth import authenticate_user

from app.dtos.token import Token
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from app.infraestructure.auth import create_access_token
from app.services.user_service import UserService

router = APIRouter()

@router.post("/auth/login", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: UserService = Depends(UserService)
    ) -> Token:
    user = authenticate_user(UserCredentials(
        email=form_data.username,
        password=form_data.password
    ),service)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@router.post("/auth/logout")
async def todo_logout():
    return "todo: logout"