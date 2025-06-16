
from fastapi import Depends
from sqlalchemy import delete, insert, update
from app.dtos.comment import  CommentResponse, CommentCreate, CommentUpdate
from app.infraestructure.sqlite import get_db_session
from app.models.task import Task
from sqlalchemy.orm import Session

from app.models.comment import Comment 
from app.exceptions.domain import  CommentNotFound, TaskNotFound

class SQLiteCommentRepository:
    def __init__(self, db_session: Session = Depends(get_db_session)):
        self.session: Session = db_session
        self.comment_response_columns = [col for col in Comment.__table__.c if col.name in CommentResponse.model_fields]

    def create_comment(self, user_id: int, comment_data: CommentCreate) -> CommentResponse:
        stmt = (
            insert(Comment)
            .values(user_id=user_id, **comment_data.model_dump())
            .returning(*self.comment_response_columns)
        )
        created_comment = self.session.execute(stmt).first()
        self.session.commit()
        return CommentResponse.model_validate(created_comment)
    
    def get_task_comments(self, task_id: int) -> list[CommentResponse]:
        task = self.session.query(Task).filter(Task.id == task_id).first()

        if not task:
            raise TaskNotFound(f"Task with id {task_id} not found")

        comments = self.session.query(Comment).filter(Comment.task_id == task_id).all()
        return [CommentResponse.model_validate(comment) for comment in comments]
    
    def get_comment_by_id(self, comment_id: int) -> CommentResponse:
        comment = self.session.query(Comment).filter(Comment.id == comment_id).first()

        if not comment:
            raise CommentNotFound(f"Comment with id {comment_id} not found")

        return CommentResponse.model_validate(comment)
    
    def delete_comment(self, comment_id: int) -> CommentResponse:
        stmt = (
            delete(Comment)
            .where(Comment.id == comment_id)
            .returning(*self.comment_response_columns)
        )
        deleted_comment = self.session.execute(stmt).first()
        if not deleted_comment:
            self.session.rollback()
            raise TaskNotFound(detail=f"Comment with id {comment_id} not found")
        self.session.commit()
        return CommentResponse.model_validate(deleted_comment)
    
    def update_comment(self, comment_id: int, comment_data: CommentUpdate) -> CommentResponse:
        stmt = (
            update(Comment)
            .where(Comment.id == comment_id)
            .values(comment_data.model_dump(exclude_unset=True))
            .returning(*self.comment_response_columns)
        )
        updated_comment = self.session.execute(stmt).first()
        if not updated_comment:
            self.session.rollback()
            raise CommentNotFound(detail=f"Comment with id {comment_id} not found")
        self.session.commit()
        return CommentResponse.model_validate(updated_comment)