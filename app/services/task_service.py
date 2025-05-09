from typing import Optional
from fastapi import Depends

from app.repository.sqlite_task_repository import SQLiteTaskRepository
from app.dtos.task import TaskResponse, TaskCreate, TaskUpdate

class TaskService:
    def __init__(self, task_repository: SQLiteTaskRepository = Depends(SQLiteTaskRepository)):
        self.task_repository = task_repository

    def create_task(self, task_data: TaskCreate) -> TaskResponse:
        return self.task_repository.create_task(task_data)

    def get_task_by_id(self, task_id: int) -> Optional[TaskResponse]:
        return self.task_repository.get_task(task_id)

    def update_task(self, task_id, task_data: TaskUpdate) -> Optional[TaskResponse]:
        return self.task_repository.update_task(task_id, task_data)

    def delete_task(self, task_id: int) -> Optional[TaskResponse]:
        return self.task_repository.delete_task(task_id)
    
    def get_tasks_assigned_to_user(self, user_id: int) -> Optional[list[TaskResponse]]:
        return self.task_repository.get_tasks_assigned_to_user(user_id)