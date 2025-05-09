from fastapi import Depends
from app.infraestructure.sqlite import get_db_session
from sqlalchemy.orm import Session
from typing import Optional

from app.dtos.task import TaskResponse, TaskCreate, TaskUpdate
from app.models.task import Task

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
    
    def get_task(self, task_id: int) -> Optional[TaskResponse]:
        task = self.session.query(Task).filter(Task.id == task_id).first()
        return TaskResponse.model_validate(task) if task else None

    def update_task(self, task_id: int, task_data: TaskUpdate) -> Optional[TaskResponse]:
        stmt = (
            update(Task)
            .where(Task.id == task_id)
            .values(task_data.model_dump())
            .returning(Task.id, Task.title, Task.description, Task.completed, Task.assigned_to_user_id)
        )
        updated_task = self.session.execute(stmt).first()
        self.session.commit()
        return TaskResponse.model_validate(updated_task) if updated_task else None
    
    def delete_task(self, task_id: int) -> Optional[TaskResponse]:
        stmt = (
            delete(Task)
            .where(Task.id == task_id)
            .returning(Task.id, Task.title, Task.description, Task.completed, Task.assigned_to_user_id)
        )
        deleted_task = self.session.execute(stmt).first()
        self.session.commit()
        return TaskResponse.model_validate(deleted_task) if deleted_task else None

    def get_tasks_assigned_to_user(self, user_id: int) -> Optional[list[TaskResponse]]:
        tasks = self.session.query(Task).filter(Task.assigned_to_user_id == user_id).all()
        return [TaskResponse.model_validate(task) for task in tasks] if tasks else None