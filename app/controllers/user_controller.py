from fastapi import APIRouter, Depends, HTTPException
from app.services.user_service import UserService

from app.schemas.user import UserResponse

router = APIRouter()

@router.get("/users/{user_id}",response_model=UserResponse)
async def get_user_by_id(
    user_id: int, 
    service: UserService = Depends(UserService)
    ):
    user = service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
