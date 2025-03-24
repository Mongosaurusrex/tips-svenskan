def test_register_user(client):
    res = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "secure123"
    })
    assert res.status_code == 200
    data = res.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_register_existing_user(client):
    res = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "secure123"
    })
    assert res.status_code == 400
    assert res.json()["detail"] == "Email already registered"

def test_login_success(client):
    res = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "secure123"
    })
    assert res.status_code == 200
    assert "access_token" in res.json()

def test_login_wrong_password(client):
    res = client.post("/auth/login", json={
        "email": "test@example.com",
        "password": "wrongpass"
    })
    assert res.status_code == 401

