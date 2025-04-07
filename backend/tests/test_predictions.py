import pytest
from fastapi.testclient import TestClient
from tests.factories import UserFactory, LeagueFactory, TeamFactory
from datetime import date, timedelta


@pytest.fixture
def league():
    return LeagueFactory(lock_date=date.today() + timedelta(days=1))


@pytest.fixture
def locked_league():
    return LeagueFactory(lock_date=date.today() - timedelta(days=1))


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def teams(league):
    return TeamFactory.create_batch(5, league=league)


def login_user(client: TestClient, user):
    res = client.post("/auth/login", json={
        "email": user.email,
        "password": "secure123"
    })
    return res.json()["access_token"]


def auth_headers(token: str):
    return {"Authorization": f"Bearer {token}"}


def test_create_prediction(client: TestClient, user, league, teams):
    token = login_user(client, user)
    team_ids = [str(team.id) for team in teams]

    res = client.post("/predictions", json={
        "league_id": str(league.id),
        "team_ids": team_ids
    }, headers=auth_headers(token))

    assert res.status_code == 201 or res.status_code == 200


def test_get_user_prediction(client: TestClient, user, league, teams):
    token = login_user(client, user)
    team_ids = [str(team.id) for team in teams]

    # First create a prediction
    client.post("/predictions", json={
        "league_id": str(league.id),
        "team_ids": team_ids
    }, headers=auth_headers(token))

    # Then fetch it
    res = client.get(f"/predictions/{league.id}", headers=auth_headers(token))
    assert res.status_code == 200
    assert len(res.json()["entries"]) == len(teams)


def test_duplicate_prediction_fails(client: TestClient, user, league, teams):
    token = login_user(client, user)
    team_ids = [str(team.id) for team in teams]

    # First create one
    client.post("/predictions", json={
        "league_id": str(league.id),
        "team_ids": team_ids
    }, headers=auth_headers(token))

    # Try again
    res = client.post("/predictions", json={
        "league_id": str(league.id),
        "team_ids": team_ids
    }, headers=auth_headers(token))

    assert res.status_code == 400
    assert "already submitted" in res.json()["detail"].lower()


def test_prediction_blocked_after_lock(client: TestClient, user, locked_league):
    teams = TeamFactory.create_batch(5, league=locked_league)
    team_ids = [str(team.id) for team in teams]
    token = login_user(client, user)

    res = client.post("/predictions", json={
        "league_id": str(locked_league.id),
        "team_ids": team_ids
    }, headers=auth_headers(token))

    assert res.status_code == 403
    assert "locked" in res.json()["detail"].lower()
