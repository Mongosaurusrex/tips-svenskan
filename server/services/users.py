from typing import List

from server.repositories.users import UserRepository
from server.models.user import User


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def get_users(self) -> List[User]:
        return self._user_repository.get_all()

    def get_user_by_id(self, id: int) -> User:
        return self._user_repository.get_by_id(id)

    def get_user_by_username(self, user_name: str) -> User:
        return self._user_repository.get_by_user_name(user_name)

    def create_user(self) -> User:
        return self._user_repository.add_user(
            user_name="mongosaurusrex", password="pwd"
        )

    def delete_user_by_id(self, id: int) -> None:
        self._user_repository.delete_user_by_id(id)
