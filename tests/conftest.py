from app.infraestructure.sqlite import get_db_session
from app.infraestructure.mockdb import create_all_tables as mock_create_all_tables
from app.infraestructure.mockdb import get_db_session as mock_get_db_session
from app.infraestructure.mockdb import drop_all_tables
from app.main import app
from fastapi.testclient import TestClient
import pytest

@pytest.fixture
def client():
    app.dependency_overrides[get_db_session] = mock_get_db_session
    mock_create_all_tables()
    yield TestClient(app)
    app.dependency_overrides.clear()
    drop_all_tables()
