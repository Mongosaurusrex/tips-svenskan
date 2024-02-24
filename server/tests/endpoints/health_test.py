import pytest
from fastapi.testclient import TestClient
from server.main import app


@pytest.fixture
def client():
    yield TestClient(app=app)


def test_health_check_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()
    assert data == "Healthy boi"
