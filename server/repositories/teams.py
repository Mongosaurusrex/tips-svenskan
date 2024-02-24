from contextlib import AbstractContextManager
from typing import List, Callable

from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row

from server.models.team import Team


class TeamsRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self._session_factory = session_factory

    def get_all(self) -> List[dict]:
        with self._session_factory() as session:
            return [
                u._asdict()
                for u in session.query(Team)
                .with_entities(Team.id, Team.name, Team.logo)
                .all()
            ]
