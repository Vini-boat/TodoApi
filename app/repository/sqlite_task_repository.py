from datetime import datetime
from fastapi import Depends
from app.infraestructure.sqlite import get_db_session
from sqlalchemy.orm import Session

from app.dtos.task import TaskFilter, TaskResponse, TaskCreate, TaskUpdate
from app.models.task import Task
from app.models.user import User

from app.exceptions.domain import TaskNotFound, UserNotFound

from sqlalchemy import insert, update, delete

class SQLiteTaskRepository:
    def __init__(self, db_session: Session = Depends(get_db_session)):
        self.session: Session = db_session
        self.task_response_columns = [col for col in Task.__table__.c if col.name in TaskResponse.model_fields]
    
    def create_task(self, task_data: TaskCreate) -> TaskResponse:
        stmt = (
            insert(Task)
            .values(task_data.model_dump())
            .returning(*self.task_response_columns)    
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
        completed_at = datetime.now() if task_data.completed else None

        stmt = (
            update(Task)
            .where(Task.id == task_id)
            .values(task_data.model_dump(exclude_unset=True))
            .values(completed_at=completed_at)
            .returning(*self.task_response_columns)
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
            .returning(*self.task_response_columns)
        )
        deleted_task = self.session.execute(stmt).first()
        if not deleted_task:
            self.session.rollback()
            raise TaskNotFound(detail=f"Task with id {task_id} not found")
        self.session.commit()
        return TaskResponse.model_validate(deleted_task)

    def get_filtered_tasks(self, filter: TaskFilter) -> list[TaskResponse]:
        query = self.session.query(Task)

        if filter.title:
            query = query.filter(Task.title.ilike(f"%{filter.title}%"))
        if filter.completed is not None:
            query = query.filter(Task.completed == filter.completed)
        if filter.assigned_to_user_id is not None:
            user = self.session.query(User).filter(User.id == filter.assigned_to_user_id).first()
            if not user:
                raise UserNotFound(detail=f"User with id {filter.assigned_to_user_id} not found")
            query = query.filter(Task.assigned_to_user_id == filter.assigned_to_user_id)

        if filter.created_before:
            query = query.filter(Task.created_at <= filter.created_before)
        if filter.created_after:
            query = query.filter(Task.created_at >= filter.created_after)

        if filter.completed_before:
            query = query.filter(Task.completed_at <= filter.completed_before)
        if filter.completed_after:
            query = query.filter(Task.completed_at >= filter.completed_after)

        if filter.due_before:
            query = query.filter(Task.due_to <= filter.due_before)
        if filter.due_after:
            query = query.filter(Task.due_to >= filter.due_after)

        if filter.min_priority is not None:
            query = query.filter(Task.priority >= filter.min_priority)
        if filter.max_priority is not None:
            query = query.filter(Task.priority <= filter.max_priority)

        tasks = query.all()
        return [TaskResponse.model_validate(task) for task in tasks]


    def patch_task(self, task_id: int, task_data: TaskUpdate) -> TaskResponse:
        completed_at = datetime.now() if task_data.completed else None

        stmt = (
            update(Task)
            .where(Task.id == task_id)
            .values(task_data.model_dump(exclude_unset=True))
            .values(completed_at=completed_at)
            .returning(*self.task_response_columns)
        )
        patched_task = self.session.execute(stmt).first()
        if not patched_task:
            self.session.rollback()
            raise TaskNotFound(detail=f"Task with id {task_id} not found")
        
        self.session.commit()
        return TaskResponse.model_validate(patched_task)