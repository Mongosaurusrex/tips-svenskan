from unittest import mock
import pytest
from fastapi.testclient import TestClient
from server.main import app
from server.services.auth import AuthService
from server.utils.dataclasses.responses import TokenResponse


@pytest.fixture
def client():
    yield TestClient(app=app)


def test_create_user_wrong_signup_schema_1(client):
    response = client.post(
        "/auth/signup", json={"user_name": 1234, "password": "correct_format"}
    )

    assert response.status_code == 422


def test_create_user_wrong_signup_schema_2(client):
    response = client.post(
        "/auth/signup", json={"user_name": "user_name", "password": 1234}
    )

    assert response.status_code == 422


def test_create_user(client):
    auth_service_mock = mock.Mock(spec=AuthService)
    auth_service_mock.sign_up.return_value = TokenResponse(token="ASHINYNEWTOKEN")

    with app.container.auth_service.override(auth_service_mock):
        response = client.post(
            "/auth/signup", json={"user_name": "user_name", "password": "password"}
        )

    assert response.status_code == 200
    data = response.json()
    assert data == {"token": "ASHINYNEWTOKEN"}
    auth_service_mock.sign_up.assert_called_once()
