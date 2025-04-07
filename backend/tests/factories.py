from datetime import date, timedelta
from uuid import uuid4

from factory.alchemy import SQLAlchemyModelFactory
from factory.declarations import (LazyAttribute, LazyFunction, Sequence,
                                  SubFactory)
from factory.helpers import post_generation

from auth.utils import hash_password
from db.models import League, Prediction, PredictionEntry, Team, User
from tests.conftest import TestingSessionLocal


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = TestingSessionLocal()  # ✅ session instance
        sqlalchemy_session_persistence = "commit"


class UserFactory(BaseFactory):
    class Meta:
        model = User

    id = LazyFunction(uuid4)
    email = Sequence(lambda n: f"user{n}@test.com")
    hashed_password = LazyFunction(lambda: hash_password("secure123"))


class LeagueFactory(BaseFactory):
    class Meta:
        model = League

    id = LazyFunction(uuid4)
    name = "Allsvenskan"
    season = "2025"
    lock_date = LazyFunction(lambda: date.today() + timedelta(days=1))
    is_active = True


class TeamFactory(BaseFactory):
    class Meta:
        model = Team

    id = LazyFunction(uuid4)
    name = Sequence(lambda n: f"Team {n}")
    short_name = Sequence(lambda n: f"T{n}")
    logo_url = "https://example.com/logo.png"
    league = SubFactory(LeagueFactory)


class PredictionFactory(BaseFactory):
    class Meta:
        model = Prediction

    id = LazyFunction(uuid4)
    user = SubFactory(UserFactory)
    league = SubFactory(LeagueFactory)
    shared_slug = Sequence(lambda n: f"slug-{n}")


class PredictionEntryFactory(BaseFactory):
    class Meta:
        model = PredictionEntry

    id = LazyFunction(uuid4)
    prediction = SubFactory(PredictionFactory)
    team = SubFactory(TeamFactory)
    predicted_position = Sequence(lambda n: n + 1)
