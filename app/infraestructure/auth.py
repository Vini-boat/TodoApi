from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from pydantic import EmailStr
from app.dtos.user import UserResponse
from app.services.user_service import UserService
from app.exceptions.http import UserNotFound

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def fake_decode_token(token) -> EmailStr:
    return token

async def get_current_user(
        token = Depends(oauth2_scheme),
        service: UserService = Depends(UserService)
    ) -> UserResponse:
    email = fake_decode_token(token)
    user = service.get_user_by_email(email)
    if not user:
        raise UserNotFound
    return user
