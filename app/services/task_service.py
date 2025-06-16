from fastapi import Depends

from app.repository.sqlite_task_repository import SQLiteTaskRepository
from app.dtos.task import TaskResponse, TaskCreate, TaskUpdate, TaskFilter

class TaskService:
    def __init__(self, task_repository: SQLiteTaskRepository = Depends(SQLiteTaskRepository)):
        self.task_repository = task_repository

    def create_task(self, task_data: TaskCreate) -> TaskResponse:
        return self.task_repository.create_task(task_data)


    def get_task_by_id(self, task_id: int) -> TaskResponse:
        return self.task_repository.get_task(task_id)

    def update_task(self, task_id, task_data: TaskUpdate) -> TaskResponse:
        return self.task_repository.update_task(task_id, task_data)

    def delete_task(self, task_id: int) -> TaskResponse:
        return self.task_repository.delete_task(task_id)
    
    def get_filtered_tasks(self, task_filter: TaskFilter) -> list[TaskResponse]:
        return self.task_repository.get_filtered_tasks(task_filter)
    
    def patch_task(self, task_id: int, task_data: TaskUpdate) -> TaskResponse:
        return self.task_repository.patch_task(task_id, task_data)