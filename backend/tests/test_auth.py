from time import sleep

def test_register_user(client):
    res = client.post(
        "/auth/register", json={"email": "test@example.com", "password": "secure123"}
    )
    assert res.status_code == 200
    data = res.json()
    assert data["email"] == "test@example.com"
    assert "id" in data


def test_register_existing_user(client):
    res = client.post(
        "/auth/register", json={"email": "test@example.com", "password": "secure123"}
    )
    assert res.status_code == 400
    assert res.json()["detail"] == "Email already registered"


def test_login_success(client):
    res = client.post(
        "/auth/login", json={"email": "test@example.com", "password": "secure123"}
    )
    assert res.status_code == 200
    assert "access_token" in res.json()


def test_login_wrong_password(client):
    res = client.post(
        "/auth/login", json={"email": "test@example.com", "password": "wrongpass"}
    )
    assert res.status_code == 401


def test_login_and_get_tokens(client):
    res = client.post(
        "/auth/login", json={"email": "test@example.com", "password": "secure123"}
    )
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert "refresh_token" in data
    global access_token, refresh_token
    access_token = data["access_token"]
    refresh_token = data["refresh_token"]


def test_refresh_token(client):
    sleep(1)
    res = client.post("/auth/refresh", json={"refresh_token": refresh_token})
    assert res.status_code == 200
    new_token = res.json()["access_token"]
    assert new_token != access_token  # tokens should differ
    assert res.json()["token_type"] == "bearer"


def test_refresh_token_invalid(client):
    res = client.post("/auth/refresh", json={"refresh_token": "this.is.not.valid"})
    assert res.status_code == 401
