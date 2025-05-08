from abc import ABC, abstractmethod

from app.schemas.task import TaskResponse, TaskCreate, TaskUpdate

class ITasksRepository(ABC):
    @abstractmethod
    def create_task(self, task_id: int, task: TaskCreate) -> TaskResponse:
        raise NotImplementedError

    @abstractmethod
    def get_task(self, task_id:int) -> TaskResponse:
        raise NotImplementedError

    @abstractmethod
    def update_task(self, task_id: int, task: TaskUpdate) -> TaskResponse:
        raise NotImplementedError

    @abstractmethod
    def delete_task(self, task_id: int):
        raise NotImplementedError