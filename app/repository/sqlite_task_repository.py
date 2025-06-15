from fastapi import Depends
from app.infraestructure.sqlite import get_db_session
from sqlalchemy.orm import Session

from app.dtos.task import TaskResponse, TaskCreate, TaskUpdate
from app.models.task import Task
from app.models.user import User

from app.exceptions.domain import TaskNotFound, UserNotFound

from sqlalchemy import insert, update, delete

class SQLiteTaskRepository:
    def __init__(self, db_session: Session = Depends(get_db_session)):
        self.session: Session = db_session
    
    def create_task(self, task_data: TaskCreate) -> TaskResponse:
        stmt = (
            insert(Task)
            .values(task_data.model_dump())
            .returning(Task.id, Task.title, Task.description, Task.completed, Task.assigned_to_user_id)    
        )
        created_task = self.session.execute(stmt).first()
        self.session.commit()
        return TaskResponse.model_validate(created_task)
    
    def get_task(self, task_id: int) -> TaskResponse:
        task = self.session.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise TaskNotFound(detail=f"Task with id {task_id} not found")
        
        return TaskResponse.model_validate(task)

    def update_task(self, task_id: int, task_data: TaskUpdate) -> TaskResponse:
        stmt = (
            update(Task)
            .where(Task.id == task_id)
            .values(task_data.model_dump())
            .returning(Task.id, Task.title, Task.description, Task.completed, Task.assigned_to_user_id)
        )
        updated_task = self.session.execute(stmt).first()
        if not updated_task:
            self.session.rollback()
            raise TaskNotFound(detail=f"Task with id {task_id} not found")
        
        self.session.commit()
        return TaskResponse.model_validate(updated_task)
    
    def delete_task(self, task_id: int) -> TaskResponse:
        stmt = (
            delete(Task)
            .where(Task.id == task_id)
            .returning(Task.id, Task.title, Task.description, Task.completed, Task.assigned_to_user_id)
        )
        deleted_task = self.session.execute(stmt).first()
        if not deleted_task:
            self.session.rollback()
            raise TaskNotFound(detail=f"Task with id {task_id} not found")
        self.session.commit()
        return TaskResponse.model_validate(deleted_task)

    def get_tasks_assigned_to_user(self, user_id: int) -> list[TaskResponse]:
        user = self.session.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound(detail=f"User with id {user_id} not found")
        
        tasks = self.session.query(Task).filter(Task.assigned_to_user_id == user_id).all()
        return [TaskResponse.model_validate(task) for task in tasks] if tasks else []