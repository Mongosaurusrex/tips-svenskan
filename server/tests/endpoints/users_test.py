from unittest import mock
import pytest
from fastapi.testclient import TestClient
from server.main import app
from server.services.users import UserService
from server.models.user import User


@pytest.fixture
def client():
    yield TestClient(app=app)


def test_get_users():
    users_service_mock = mock.Mock(spec=UserService)
    users_service_mock.get_users.return_value = [
        {"id": 1, "user_name": "user_1"},
        {"id": 2, "user_name": "user_2"},
    ]

    with app.container.auth_service.override(users_service_mock):
        response = client.get("/users")

    assert response.status_code == 200
    data = response.json()
    assert data == [
        {"user_name": "user_1"},
        {"user_name": "user_2"},
    ]
    users_service_mock.get_users.assert_called_once()
