from contextlib import AbstractContextManager
from typing import List, Callable

from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row

from server.models.table import Table


class TableRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self._session_factory = session_factory

    def get_all(self) -> List[Row]:
        with self._session_factory() as session:
            return session.query(Table).with_entities(Table.id, Table.created_by).all()
