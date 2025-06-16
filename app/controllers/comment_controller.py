from fastapi import APIRouter, Depends, Query

from app.models.user import User
from app.services.comment_service import CommentService
from app.dtos.comment import CommentResponse, CommentCreate, CommentUpdate

from app.infraestructure.auth import get_current_user

router = APIRouter()

@router.post("/comments", response_model=CommentResponse)
async def create_comment(
    comment: CommentCreate,
    service: CommentService = Depends(CommentService),
    user: User = Depends(get_current_user)
    ):
    return service.create_comment(comment, user.id)

@router.get("/comments", response_model=list[CommentResponse])
async def get_task_comments(
    task_id: int = Query(..., description="task_id"),
    service: CommentService = Depends(CommentService)
    ):
    return service.get_task_comments(task_id)

@router.get("/comments/{comment_id}", response_model=CommentResponse)
async def get_comment_by_id(
    comment_id: int,
    service: CommentService = Depends(CommentService)
    ):
    return service.get_comment_by_id(comment_id)

@router.delete("/comments/{comment_id}", response_model=CommentResponse)
async def delete_comment(
    comment_id: int,
    service: CommentService = Depends(CommentService),
    user: User = Depends(get_current_user)
    ):
    return service.delete_comment(comment_id, user.id)

@router.put("/comments/{comment_id}", response_model=CommentResponse)
async def update_comment(
    comment_id: int,
    comment: CommentUpdate,
    service: CommentService = Depends(CommentService),
    user: User = Depends(get_current_user)
    ):
    return service.update_comment(comment_id, comment, user.id)
