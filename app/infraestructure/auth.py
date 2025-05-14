from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.dtos.user import UserResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def fake_decode_token(token) -> UserResponse:

    return UserResponse(
        id=1,
        username="fakeuser" + token,
        email="fake@email.com",
        )

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserResponse:
    user = fake_decode_token(token)
    return user