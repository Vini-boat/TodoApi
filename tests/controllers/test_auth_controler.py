import pytest

def test_login_for_access_token_deve_logar(client):
    # Arrange
    response = client.post(
        "/api/v1/users",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        },
    )
    
    # Act
    response = client.post(
        "/api/v1/auth/login",
        headers={"accept": "application/json",
                 "Content-Type": "application/x-www-form-urlencoded"},
        data={
            "username": "testuser@example.com",
            "password": "testpassword"
        }
    )
    # Assert
    assert response.status_code == 200
    assert "access_token" in response.json() and response.json()["access_token"] is not None

@pytest.mark.parametrize("username,password", [
    ("testuser@wrong.com", "testpassword"), # wrong username
    ("testuser@example.com", "wrongpassword") # wrong password
])
def test_login_for_access_token_nao_deve_logar(client, username, password):
    # Arrange: criação de usuário teste
    response = client.post(
        "/api/v1/users",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        }
    )

    # Act
    response = client.post(
        "/api/v1/auth/login",
        headers={"accept": "application/json",
                 "Content-Type": "application/x-www-form-urlencoded"},
        data={
            "username": username,
            "password": password
        }
    )
    # Assert
    assert response.status_code == 401 or response.status_code == 404