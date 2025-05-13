import pytest
from app.repository.sqlite_user_repository import SQLiteUserRepository
from app.dtos.user import UserCreate
from app.infraestructure.mockdb import get_db_session, create_all_tables


@pytest.fixture
def repository() -> SQLiteUserRepository:
    create_all_tables()
    return SQLiteUserRepository(next(get_db_session()))


@pytest.mark.parametrize("username, email, password, should_create", [
    ("John Doe", "john.doe@example.com", "securepassword", True),
    ("Jane Doe", "jane", "securepassword", False),
])
@pytest.mark.usefixtures("repository")
def test_create_user(repository: SQLiteUserRepository, username: str, email: str, password: str, should_create: bool):
    try:
        user = UserCreate(username=username, email=email, password=password)
        created_user = repository.create_user(user)
    except ValueError:
        created_user = None
    
    if should_create:
        assert created_user is not None
        assert created_user.email == email
    else:
        assert created_user is None

# @pytest.mark.usefixtures("repository")
# def test_get_user_by_id(repository):
#     user = User(id=2, name="Jane Doe", email="jane.doe@example.com")
#     repository.create_user(user)
#     retrieved_user = repository.get_user_by_id(2)
#     assert retrieved_user is not None
#     assert retrieved_user.name == "Jane Doe"

# @pytest.mark.usefixtures("repository")
# def test_update_user(repository):
#     user = User(id=3, name="Alice", email="alice@example.com")
#     repository.create_user(user)
#     user.name = "Alice Updated"
#     repository.update_user(user)
#     updated_user = repository.get_user_by_id(3)
#     assert updated_user.name == "Alice Updated"

# @pytest.mark.usefixtures("repository")
# def test_delete_user(repository):
#     user = User(id=4, name="Bob", email="bob@example.com")
#     repository.create_user(user)
#     repository.delete_user(4)
#     deleted_user = repository.get_user_by_id(4)
#     assert deleted_user is None
