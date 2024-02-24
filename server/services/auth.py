import datetime
import hashlib

import jwt

from server.repositories.users import UserRepository
from server.utils.dataclasses.responses import TokenResponse
from server.utils.dataclasses.users import UserSignupSchema, UserLoginSchema
from server.utils.errors import UserNameNotFoundError, InvalidUserCredentials


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def _sign_jwt(self, user_id: int) -> TokenResponse:
        payload = {
            "user_id": str(user_id),
            "expires": (
                datetime.datetime.now() + datetime.timedelta(minutes=15)
            ).isoformat(),
        }
        print(payload)
        token = jwt.encode(
            payload,
            "super-secret-123-key",
            algorithm="HS256",
        )  # TODO: ENV VAR
        return TokenResponse(token=token)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def sign_up(self, user: UserSignupSchema) -> TokenResponse:
        user = self._user_repository.add_user(
            user_name=user.user_name, password=self._hash_password(user.password)
        )
        return self._sign_jwt(int(user.id))

    def sign_in(self, user: UserLoginSchema) -> TokenResponse:
        try:
            found_user = self._user_repository.get_by_user_name(user.user_name)
            if found_user.hashed_password != self._hash_password(user.password):
                raise InvalidUserCredentials()
            return self._sign_jwt(int(found_user.id))
        except UserNameNotFoundError:
            raise InvalidUserCredentials()
