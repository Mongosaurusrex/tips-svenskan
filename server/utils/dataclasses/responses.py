from pydantic import BaseModel, Field


class TokenResponse(BaseModel):
    token: str = Field(...)
