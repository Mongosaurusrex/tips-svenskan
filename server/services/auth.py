from time import time
from typing import Dict
import hashlib

import jwt

from server.repositories.user import UserRepository
from server.utils.dataclasses.responses import TokenResponse
from server.utils.dataclasses.users import UserSignupSchema, UserLoginSchema
from server.utils.errors import UserNameNotFoundError, InvalidUserCredentials


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def _sign_jwt(self, user_id: int) -> TokenResponse:
        payload = {"user_id": user_id, "expires": time() + 900_000}
        token = jwt.encode(payload, "HAHAHAHAH", algorithm="HS256")  # TODO: ENV VAR
        return TokenResponse(token=token)

    def _decode_jwt(self, token: str) -> Dict[str, str]:
        try:
            decoded_token = jwt.decode(token, "HAHAHAHAH")  # TODO: ENV VAR
            return decoded_token if decoded_token["expires"] >= time() else None
        except:
            return {}

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
            return self._sign_jwt(found_user["id"])
        except UserNameNotFoundError:
            raise InvalidUserCredentials()
