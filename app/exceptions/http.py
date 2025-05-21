from fastapi import HTTPException


UserNotFound = HTTPException(
    status_code=404,
    detail="User not found",
)

InvalidCredentials = HTTPException(
    status_code=401,
    detail="Invalid email or password",
)