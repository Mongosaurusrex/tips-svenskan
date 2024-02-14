from typing import Any
from fastapi import HTTPException


class NotFoundError(Exception):
    entity_name: str
    entity_property: str

    def __init__(self, entity_id: Any):
        super().__init__(
            f"{self.entity_name} with {self.entity_property} ({entity_id}) not found"
        )


class UserIdNotFoundError(NotFoundError):
    entity_name: str = "User"
    entity_property: str = "id"


class UserNameNotFoundError(NotFoundError):
    entity_name: str = "User"
    entity_property = "user name"


class InvalidUserCredentials(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403, detail="The provided credentials were invalid"
        )
