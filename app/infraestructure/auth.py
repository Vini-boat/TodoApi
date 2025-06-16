from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from pydantic import EmailStr
from app.dtos.user import UserCredentials, UserResponse
from app.dtos.token import TokenData
from app.services.user_service import UserService
from app.exceptions.http import  InvalidCredentials
from app.infraestructure.security import verify_password

from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from app.config import SECRET_KEY, JWT_ALGORITHM

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def fake_decode_token(token) -> EmailStr:
    return token

async def get_current_user(
        token = Depends(oauth2_scheme),
        service: UserService = Depends(UserService)
    ) -> UserResponse:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise InvalidCredentials
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise InvalidCredentials
    user = service.get_user_by_email(token_data.username)
    if user is None:
        raise InvalidCredentials
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def authenticate_user(
    user_credentials: UserCredentials,
    service: UserService = Depends(UserService),
):
    user = service.get_user_credentials(user_credentials.email)
    if not user:
        raise InvalidCredentials
    if not verify_password(user_credentials.password, user.password):
        raise InvalidCredentials
    return user