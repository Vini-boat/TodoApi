from app.dtos.comment import CommentResponse, CommentCreate, CommentUpdate
from fastapi import Depends
from app.exceptions.domain import PermissionDenied
from app.repository.sqlite_comment_repository import SQLiteCommentRepository
from app.repository.sqlite_user_repository import SQLiteUserRepository

class CommentService:
    def __init__(self, 
            comment_repository: SQLiteCommentRepository = Depends(SQLiteCommentRepository),
            user_repository: SQLiteUserRepository = Depends(SQLiteUserRepository),    
        ):
        self.comment_repository = comment_repository
        self.user_repository = user_repository

    def create_comment(self, 
            comment_data: CommentCreate, 
            user_id: int
        ) -> CommentResponse:
        return self.comment_repository.create_comment(user_id, comment_data)
    
    def get_task_comments(self, task_id: int) -> list[CommentResponse]:
        return self.comment_repository.get_task_comments(task_id)
    
    def get_comment_by_id(self, comment_id: int) -> CommentResponse:
        return self.comment_repository.get_comment_by_id(comment_id)
    
    def delete_comment(self, 
            comment_id: int, 
            user_id: int
        ) -> CommentResponse:
        original_comment = self.comment_repository.get_comment_by_id(comment_id)

        if original_comment.user_id != user_id:
            raise PermissionDenied("You do not have permission to update this comment.")
        
        return self.comment_repository.delete_comment(comment_id)
    
    def update_comment(self, 
            comment_id: int, 
            comment_data: CommentUpdate, 
            user_id: int
        ) -> CommentResponse:
        original_comment = self.comment_repository.get_comment_by_id(comment_id)

        if original_comment.user_id != user_id:
            raise PermissionDenied("You do not have permission to update this comment.")
        
        return self.comment_repository.update_comment(comment_id, comment_data)