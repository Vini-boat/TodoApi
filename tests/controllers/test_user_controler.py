from app.infraestructure.sqlite import get_db_session
from app.infraestructure.mockdb import create_all_tables as mock_create_all_tables, get_db_session as mock_get_db_session
from app.main import app
from fastapi.testclient import TestClient
import pytest

app.dependency_overrides[get_db_session] = mock_get_db_session

client = TestClient(app)
mock_create_all_tables()

@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross@gmail.com", "123567"),
    ("Vini", "vinibezerra2004@gmail.com", "00000000")
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


@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross", "123567")
])
def test_create_user_nao_deve_criar(username,email,password):
    ## TODO: testar a resposta pela exceção http que é levantda
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
    assert response.status_code != 200

@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross1@gmail.com", "123567"),
])
def test_get_user_by_id_deve_retornar(username,email,password):
    #Arrange
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
    #Act
    user_id = response.json().get("id")
    response = client.get(
        f"/api/v1/users/{user_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},
    )
    #Assert
    assert response.status_code == 200