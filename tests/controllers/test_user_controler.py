import pytest

@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross@gmail.com", "123567"),
    ("Vini", "vinibezerra2004@gmail.com", "00000000")
])
def test_create_user_deve_criar(client, username,email,password):
    # Act
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
    # Assert
    assert response.status_code == 200


@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross", "123567")
])
def test_create_user_nao_deve_criar(client, username,email,password):
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
    # Assert
    assert response.status_code == 422


@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross@gmail.com", "123567"),
])
def test_get_user_by_id_deve_retornar(client, username,email,password):
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

def test_get_user_by_id_nao_deve_retornar(client):
    #Act: espera-se que a criação falhe e não retorne um ID válido
    user_id = "999"  # ID que não existe
    response = client.get(
        f"/api/v1/users/{user_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},
    )
    #Assert
    assert response.status_code == 404  # Not Found

@pytest.mark.parametrize("new_username,new_email,new_password", [
    ("kauan", "kauangross@gmail.com", "123567"),
])
def test_update_user_deve_atualizar(client, new_username,new_email,new_password):
    #Arrange: criação de um usuário
    response = client.post(
        "/api/v1/users",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "username": "usuario_teste",
            "email": "teste@gmail.com",
            "password": "0000000",
        },
    )
    user_id = response.json().get("id")

    #Act: atualização do usuário
    response = client.put(
        f"/api/v1/users/{user_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "username": new_username,
            "email": new_email,
            "password": new_password
        },
    )
    #Assert: verificação se a atualização foi bem-sucedida
    assert response.status_code == 200
    assert response.json()["username"] == new_username
    assert response.json()["email"] == new_email

@pytest.mark.parametrize("new_email", [
    ("teste.gmail.com"),
])
def test_update_user_nao_deve_atualizar(client,new_email):
    #Arrange: criação de um usuário
    response = client.post(
        "/api/v1/users",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "username": "usuario_teste",
            "email": "teste@gmail.com",
            "password": "0000000",
        },
    )
    user_id = response.json().get("id")

    #Act: atualização do usuário
    response = client.put(
        f"/api/v1/users/{user_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "email": new_email,
        },
    )

    #act: obter o usuário atualizado
    response2 = client.get(
        f"/api/v1/users/{user_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},
    )

    #Assert: verificação se a atualização foi bem-sucedida
    assert response.status_code == 422 # Unprocessable Entity
    assert response2.json()["email"] != new_email


def test_delete_user_deve_deletar(client):
    #Arrange
    response1 = client.post(
        "/api/v1/users",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},

        json={
            "username": "usuario_teste",
            "email": "teste@gmail.com",
            "password": "0000000",
        },
    )
    user_id = response1.json().get("id")
    

    #Act: delete
    response = client.delete(
        f"/api/v1/users/{user_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},
    )

    #Act: get user after delete
    response3 = client.get(
        f"/api/v1/users/{user_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},
    )

    #Assert
    assert response.status_code == 200
    assert response3.status_code == 403 # Forbidden

def test_delete_user_nao_deve_deletar(client):
    #Act: delete user that does not exist
    user_id = 0
    
    response = client.delete(
        f"/api/v1/users/{user_id}",
        headers={"accept" : "application/json",
                "Content-Type" : "application/json"},
    )

    #Assert
    assert response.status_code == 404  # Not Found
    