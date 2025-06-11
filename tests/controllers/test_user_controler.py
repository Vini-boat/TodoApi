from app.main import app
from fastapi.testclient import TestClient
import pytest

from app.infraestructure.mockdb import get_db_session as mock_get_db_session
from app.infraestructure.mockdb import create_all_tables
from app.infraestructure.sqlite import get_db_session 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# Banco de dados em memória para teste
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar tabelas no banco em memória
Base.metadata.create_all(bind=engine)

# Dependency override
def override_get_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db_session] = override_get_db
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