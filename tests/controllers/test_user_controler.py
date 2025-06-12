import pytest

@pytest.mark.parametrize("username,email,password", [
    ("kauan", "kauangross@gmail.com", "123567"),
    ("Vini", "vinibezerra2004@gmail.com", "00000000")
])
def test_create_user_deve_criar(client, username,email,password):
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
    assert response.status_code != 200

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