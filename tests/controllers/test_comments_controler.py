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
    (9999, None),  # ID de tarefa inexistente
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

def test_get_comments_by_task_id_deve_retornar(client):
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

    # Arrange: criação de comentário
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

    #Act
    response = client.get(
        f"/api/v1/comments?task_id={task_id}",
        headers ={
            "accept": "application/json",
        }
    )
    
    # Assert
    assert response.status_code == 200

@pytest.mark.parametrize("task_id", [
    (1), (999) # ID de tarefa inexistente
])
def test_get_comments_by_task_id_nao_deve_retornar(client, task_id):
    #Act
    response = client.get(
        f"/api/v1/comments?task_id={task_id}",
        headers ={
            "accept": "application/json",
        }
    )
    
    # Asserts
    assert response.status_code == 404

def test_get_comment_by_id_deve_retornar(client):
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

    # Arrange: criação de comentário
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
    comment_id = response.json().get("id")

    #Act
    response = client.get(
        f"/api/v1/comments/{comment_id}",
        headers ={
            "accept": "application/json",
        }
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["task_id"] == task_id
    assert response.json()["content"] == "Este é um comentário de teste."

@pytest.mark.parametrize("comment_id", [
    (1), (999) # ID de comment inexistente
])
def test_get_comment_by_id_nao_deve_retornar(client, comment_id):
    #Act
    response = client.get(
        f"/api/v1/comments/{comment_id}",
        headers ={
            "accept": "application/json",
        }
    )
    
    # Assert
    assert response.status_code == 404

def test_update_comment_deve_atualizar(client):
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

    # Arrange: criação de comentário
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
    comment_id = response.json().get("id")
    
    # Act
    response = client.put(
        f"/api/v1/comments/{comment_id}",
        headers={"accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}"},
        json={
            "content": "Comentario atualizado!"
        }
    )

    # Assert
    assert response.status_code == 200

@pytest.mark.parametrize("wrong_comment_id, wrong_access_token", [
    (None, "Wrong acess"), # Token incorreto e id de comemnt existente 
    (999, None) # Toker correto e id de comment inexistente
])
def test_update_comment_nao_deve_atualizar(client, wrong_comment_id, wrong_access_token):
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
    if wrong_access_token: 
        access_token = wrong_access_token
    else:
        access_token = response.json().get("access_token")

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

    # Arrange: criação de comentário
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
    if wrong_comment_id:
        comment_id = wrong_comment_id
    else:
        comment_id = response.json().get("id")
    
    # Act
    response = client.put(
        f"/api/v1/comments/{comment_id}",
        headers={"accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {access_token}"},
        json={
            "content": "Comentario atualizado!"
        }
    )

    # Assert
    assert response.status_code in [401, 404]

def test_delete_comment_deve_deletar(client):
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

    # Arrange: criação de comentário
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
    comment_id = response.json().get("id")
    

    # Act: delete
    response = client.delete(
        f"/api/v1/comments/{comment_id}",
        headers={"accept": "application/json",
            "Authorization": f"Bearer {access_token}"}
    )

    # Confirmar que não existe mais
    response2 = client.get(
        f"/api/v1/comments/{comment_id}",
        headers={"accept": "application/json"}
    )
    assert response2.status_code == 404

    # Assert
    assert response.status_code == 200

@pytest.mark.parametrize("wrong_comment_id, wrong_access_token", [
    (1, "Wrong access"), # Token incorreto e id de comemnt existente 
    (999, None) # Toker correto e id de comment inexistente
])
def test_delete_comment_nao_deve_deletar(client, wrong_comment_id, wrong_access_token):
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
    if wrong_access_token:
        access_token = wrong_access_token
    else:
        access_token = response.json().get("access_token")

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

    # Arrange: criação de comentário
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

    # Act: delete
    response = client.delete(
        f"/api/v1/comments/{wrong_comment_id}",
        headers={"accept": "application/json",
            "Authorization": f"Bearer {access_token}"}
    )

    # Confirmar que não existe mais
    response2 = client.get(
        f"/api/v1/comments/{wrong_comment_id}",
        headers={"accept": "application/json"}
    )
    assert response2.status_code == 404

    # Assert
    assert response.status_code in [401, 404]