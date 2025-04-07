import pytest
from fastapi.testclient import TestClient

from tests.factories import UserFactory


@pytest.fixture
def test_user():
    """Creates a user with a known password using the factory."""
    return UserFactory()


def test_register_user(client: TestClient):
    res = client.post(
        "/auth/register", json={"email": "newuser@example.com", "password": "secure123"}
    )

    assert res.status_code == 200
    data = res.json()
    assert data["email"] == "newuser@example.com"
    assert "id" in data


def test_register_existing_user(client: TestClient, test_user):
    res = client.post(
        "/auth/register", json={"email": test_user.email, "password": "secure123"}
    )

    assert res.status_code == 400
    assert "already registered" in res.json()["detail"].lower()


def test_login_success(client: TestClient, test_user):
    res = client.post(
        "/auth/login", json={"email": test_user.email, "password": "secure123"}
    )

    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert "refresh_token" in data


def test_login_wrong_password(client: TestClient, test_user):
    res = client.post(
        "/auth/login", json={"email": test_user.email, "password": "wrongpass"}
    )

    assert res.status_code == 401


def test_login_and_refresh(client: TestClient, test_user):
    login_res = client.post(
        "/auth/login", json={"email": test_user.email, "password": "secure123"}
    )

    tokens = login_res.json()
    old_token = tokens["access_token"]
    refresh_token = tokens["refresh_token"]

    res = client.post("/auth/refresh", json={"refresh_token": refresh_token})
    assert res.status_code == 200

    new_token = res.json()["access_token"]
    assert new_token != old_token
    assert res.json()["token_type"] == "bearer"


def test_refresh_token_invalid(client: TestClient):
    res = client.post("/auth/refresh", json={"refresh_token": "this.is.not.valid"})
    assert res.status_code == 401
