import json
import pytest
from sqlalchemy import true

# Arrumar a atribuição de user que nao existe e arrumar:
    # task nao deve atualizar
    # get_task by id nao deve retornar
    # get tasks assigned to user

@pytest.mark.parametrize("title, description, assigned_to_user_id", [
    ("Task 1", "Description for task 1", None),
    ("Task 2", "Description for task 2", 1),
    ("Task 3", "Description for task 3", 2)
])
def test_create_task_deve_criar(client, title, description, assigned_to_user_id):
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
    assert response.status_code == 200


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
            "assigned_to_user_id": 1
        }
    )    

    response = client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
    )
    assert response.status_code == 200

@pytest.mark.parametrize("task_id", [
    (1), (2)
])
def test_get_tasks_by_id_nao_deve_retornar(client, task_id):
    # Arrange
    response = client.get(
        f"/api/v1/tasks/{task_id}",
        headers={"accept": "application/json",
                 "Content-Type": "application/json"},
    )
    assert response.status_code == 404


@pytest.mark.parametrize("new_title, new_description, completed, new_assigned_to_user_id",  [
    ("Updated Task", "Updated Description", True, 1),
    ("Another Updated Task", "Another Updated Description", True, None)
])
def test_update_task_deve_atualizar(client, new_title, new_description, completed, new_assigned_to_user_id):
    #Arrange
    response = client.post(
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

