from app.main import app
from fastapi.testclient import TestClient
import pytest

from app.infraestructure.mockdb import get_db_session as mock_get_db_session
from app.infraestructure.sqlite import get_db_session 

app.dependency_overrides[get_db_session] = mock_get_db_session



@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross@gmail.com", "123567")
])
def test_create_user_deve_criar(username,email,password):
    with TestClient(app) as client:
        
        response = client.post(
            "/api/v1/users",
            headers={"accept" : "application/json",
                    "Content-Type" : "application/json"},

            json={
                "username": username,
                "email": email,
                "password": password
            },
        )
        assert response.status_code == 200