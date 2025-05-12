from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.mark.parametrize("path", ["/docs", "/redoc"])
def test_get_root(path):
    response = client.get(path)
    assert response.status_code == 200