from contextlib import AbstractContextManager
from typing import List, Callable

from sqlalchemy.orm import Session
from sqlalchemy.engine.row import Row

from server.models.user import User
from server.utils.errors import UserIdNotFoundError, UserNameNotFoundError


class UserRepository:
    def __init__(
        self, session_factory: Callable[..., AbstractContextManager[Session]]
    ) -> None:
        self._session_factory = session_factory

    def get_all(self) -> List[Row]:
        with self._session_factory() as session:
            return session.query(User).with_entities(User.id, User.user_name).all()

    def get_by_id(self, id: int) -> User:
        with self._session_factory() as session:
            user = session.query(User).filter(User.id == id).first()
            if not user:
                raise UserIdNotFoundError(str(id))
            return user

    def get_by_user_name(self, user_name: str) -> User:
        with self._session_factory() as session:
            user = session.query(User).filter(User.user_name == user_name).first()
            if not user:
                raise UserNameNotFoundError(user_name)
            return user

    def add_user(self, user_name: str, password: str) -> User:
        with self._session_factory() as session:
            user = User(
                user_name=user_name,
                hashed_password=password,
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    def delete_user_by_id(self, id: int) -> None:
        with self._session_factory() as session:
            user = session.query(User).filter(User.id == id).first()
            if not user:
                raise UserIdNotFoundError(id)
            session.delete(user)
            session.commit()
