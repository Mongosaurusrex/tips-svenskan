from typing_extensions import Tuple
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
import datetime
import jwt
from time import time


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(
            auto_error=auto_error,
        )

    async def __call__(self, request: Request) -> None:
        credentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authorization scheme."
                )

            is_token_valid, user_id = self._verify_jwt(credentials.credentials)

            if not is_token_valid:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )

            credentials.credentials = user_id

            return
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")

    def _verify_jwt(self, jwtoken: str) -> Tuple[bool, str]:
        is_token_valid: bool = False
        user_id = None
        try:
            decoded_token = jwt.decode(
                jwtoken,
                key="super-secret-123-key",
                algorithms=["HS256"],
            )  # TODO: ENV VAR
            print("HELLO", decoded_token)
            user_id = (
                decoded_token["user_id"]
                if datetime.datetime.fromisoformat(decoded_token["expires"])
                > datetime.datetime.now()
                else None
            )
        except Exception as error:
            print("Error from decoding JWT:", error)

        if user_id:
            is_token_valid = True

        return (is_token_valid, user_id)
