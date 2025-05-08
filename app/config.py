from app.main import app

from app.interfaces.user_repository import IUserRepository
from app.repository.mock_user_repository import MockUserRepository

from app.interfaces.task_repository import ITasksRepository
from app.repository.mock_task_repository import MockTaskRepository

app.dependency_overrides[IUserRepository] = MockUserRepository
app.dependency_overrides[ITasksRepository] = MockTaskRepository