from datetime import date
from uuid import UUID

from pydantic import BaseModel


class TeamOut(BaseModel):
    id: UUID
    name: str
    short_name: str | None = None
    logo_url: str | None = None

    class Config:
        from_attributes = True


class LeagueOut(BaseModel):
    id: UUID
    name: str
    season: str
    lock_date: date

    class Config:
        from_attributes = True


