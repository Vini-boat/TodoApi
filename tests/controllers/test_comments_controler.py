import pytest

def test_create_comment_deve_criar(client):
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
    
    # Arrange: login do usuário teste
    response = client.post(
        "/api/v1/auth/login",
        headers={"accept": "application/json",
                 "Content-Type": "application/x-www-form-urlencoded"},
        data={
            "username": "testuser@example.com",
            "password": "testpassword"
        }
    )
    access_token = response.json().get("access_token")
    assert access_token is not None

    # Arrange: criação de task para o comentário
    response = client.post(
        "/api/v1/tasks",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "title": "Task title",
            "description": "Task description",
            "assigned_to_user_id": 1
        }
    )
    task_id = response.json().get("id")

    # Act: criação de comentário
    response = client.post(
        "/api/v1/comments",
        headers={"accept": "application/json",
                 "Content-Type": "application/json",
                 "Authorization": f"Bearer {access_token}"},
        json={
            "task_id": task_id,
            "content": "Este é um comentário de teste."
        }
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["content"] is not None

@pytest.mark.parametrize("task_id, invalid_token", [
    #(9999, None),  # ID de tarefa inexistente
    (1, "invalid_token")  # Token de acesso inválido
])
def test_create_comment_nao_deve_criar(client, task_id, invalid_token):
    # Arrange: criação de usuário teste
    client.post(
        "/api/v1/users",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpassword"
        }
    )
    
    # Arrange: login do usuário teste
    response = client.post(
        "/api/v1/auth/login",
        headers={"accept": "application/json",
                 "Content-Type": "application/x-www-form-urlencoded"},
        data={
            "username": "testuser@example.com",
            "password": "testpassword"
        }
    )
    
    if invalid_token is None:
        access_token = response.json().get("access_token")
        assert access_token is not None
    else:
        access_token = invalid_token
    
    # Act: tentativa de criar comentário
    response = client.post(
        "/api/v1/comments",
        headers={
            "accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        },
        json={
            "task_id": task_id,
            "content": "Este é um comentário de teste."
        }
    )

    # Assert: espera erro
    assert response.status_code in [401, 404, 422]
    assert "detail" in response.json()