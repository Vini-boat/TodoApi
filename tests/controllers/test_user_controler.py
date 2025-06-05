from app.main import app
from fastapi.testclient import TestClient
import pytest
    
client = TestClient(app)

@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross@gmail.com", "123567")
])
def test_create_user_deve_criar(username,email,password):
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