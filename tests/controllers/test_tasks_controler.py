import pytest

# Arrumar a atribuição de user que nao existe e arrumar:
    # task nao deve atualizar
    # get_task by id nao deve retornar
    # get tasks assigned to user

@pytest.mark.parametrize("title, description, assigned_to_user_id", [
    ("Task 1", "Description for task 1", None),
    ("Task 2", "Description for task 2", None),
    ("Task 3", "Description for task 3", None)
])
def test_create_task_deve_criar(client, title, description, assigned_to_user_id):
    # Act
    response = client.post(
        "/api/v1/tasks",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "title": title,
            "description": description,
            "assigned_to_user_id": assigned_to_user_id
        }
    )
    # Assert
    assert response.status_code == 200

@pytest.mark.parametrize("title, description, assigned_to_user_id", [
    ("Task 1", "Description for task 1", 1), # user_id que não existe
    ("Task 2", "Description for task 2", 10),
    ("Task 3", "Description for task 3", 20)
])
def test_create_task_nao_deve_criar(client, title, description, assigned_to_user_id):
    # Arrange
    response = client.post(
        "/api/v1/tasks",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "title": title,
            "description": description,
            "assigned_to_user_id": assigned_to_user_id
        }
    )
    # Assert
    assert response.status_code == 404

@pytest.mark.parametrize("user_id", [
    (1)
])
def test_get_tasks_assigned_to_user_deve_retornar(client, user_id):
    # Arrange: criação de usuário teste
    response = client.post(
        "/api/v1/users",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "username": "test_user",
            "email": "test_user@example.com",
            "password": "test_password"
        },
    )

    # Act: criação de tarefa
    response = client.post(
        "/api/v1/tasks",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "title": "Task 1",
            "description": "Description for Task 1",
            "assigned_to_user_id": user_id
        }
    )
    response = client.post(
        "/api/v1/tasks",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "title": "Task 2",
            "description": "Description for Task 2",
            "assigned_to_user_id": user_id
        }
    )

    # Act: obtenção de tarefas atribuídas ao usuário
    response = client.get(
        f"/api/v1/tasks?assignedTo={user_id}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"}
    )

    # Assert
    assert response.status_code == 200

@pytest.mark.parametrize("user_id", [
    (1), (2)
])
def test_get_tasks_assigned_to_user_nao_deve_retornar(client, user_id):
    # Act: obtenção de tarefas atribuídas ao usuário que não existe
    response = client.get(
        f"/api/v1/tasks?assignedTo={user_id}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"}
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == [] 

@pytest.mark.parametrize("task_id", [
    (1), (2)
])
def test_get_tasks_by_id_deve_retornar(client, task_id):
    # Arrange
    response = client.post(
        "/api/v1/tasks",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "title": "Example Task",
            "description": "Example Description",
            "assigned_to_user_id": None
        }
    )

    response = client.post(
        "/api/v1/tasks",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "title": "Example Task 2",
            "description": "Example Description 2",
            "assigned_to_user_id": None
        }
    )    

    # Act
    response = client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
    )
    # Assert
    assert response.status_code == 200

@pytest.mark.parametrize("task_id", [
    (1), (2) # task_id que não existe
])
def test_get_tasks_by_id_nao_deve_retornar(client, task_id):
    # Arrange
    response = client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
    )

    # Assert
    assert response.status_code == 404


@pytest.mark.parametrize("new_title, new_description, completed, new_assigned_to_user_id",  [
    ("Updated Task", "Updated Description", True, None),
    ("Another Updated Task", "Another Updated Description", True, 1)
])
def test_update_task_deve_atualizar(client, new_title, new_description, completed, new_assigned_to_user_id):
    #Arrange
    response = client.post( # criação de usuário teste para atribuição de tarefa
        "/api/v1/users",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "username": "test_user",
            "email": "test_user@example.com",
            "password": "test_password"
        },
    )

    response = client.post( # criação de tarefa inicial
        "/api/v1/tasks",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "title": "Initial Task",
            "description": "Initial Description",
            "assigned_to_user_id": None
        },
    )
    task_id = response.json().get("id")

    #Act: atualização da tarefa
    response = client.put(
        f"/api/v1/tasks/{task_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "title": new_title,
            "description": new_description,
            "completed": completed,
            "assigned_to_user_id": new_assigned_to_user_id
        },
    )
    
    #Assert: verificação se a atualização foi bem-sucedida
    assert response.status_code == 200
    assert response.json()["title"] == new_title
    assert response.json()["description"] == new_description
    assert response.json()["completed"] == completed
    assert response.json()["assigned_to_user_id"] == new_assigned_to_user_id

@pytest.mark.parametrize("task_id, new_title, new_description, completed, new_assigned_to_user_id",  [
    (1, "Updated Task", "Updated Description", True, 1), # user não existe
    (2, "Another Updated Task", "Another Updated Description", True, None) # task não existe
])
def test_update_task_nao_deve_atualizar(client, task_id, new_title, new_description, completed, new_assigned_to_user_id):
    #Arrange
    response = client.post( # criação de tarefa inicial
        "/api/v1/tasks",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "title": "Initial Task",
            "description": "Initial Description",
            "assigned_to_user_id": None
        },
    )

    #Act: atualização da tarefa
    response = client.put(
        f"/api/v1/tasks/{task_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "title": new_title,
            "description": new_description,
            "completed": completed,
            "assigned_to_user_id": new_assigned_to_user_id
        },
    )
    
    #Assert: verificação se a atualização foi bem-sucedida
    assert response.status_code == 404

def test_delete_task_deve_deletar(client):
    # Arrange: criação de uma tarefa
    response = client.post(
        "/api/v1/tasks",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
        json={
            "title": "Task to be deleted",
            "description": "This task will be deleted",
            "assigned_to_user_id": None
        }
    )
    task_id = response.json().get("id")

    # Act: exclusão da tarefa
    response = client.delete(
        f"/api/v1/tasks/{task_id}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
    )

    #Act: get task after delete
    response2 = client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},
    )

    #Assert
    assert response.status_code == 200
    assert response2.status_code == 404 # Not Found

def test_delete_task_nao_deve_deletar(client):
    # Act: exclusão da tarefa
    task_id = 9999
    
    response = client.delete(
        f"/api/v1/tasks/{task_id}",  # ID que não existe
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
    )
    #Assert
    assert response.status_code == 404  # Not Found