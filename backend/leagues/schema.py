from uuid import UUID

from pydantic import BaseModel
from datetime import date


class TeamOut(BaseModel):
    id: UUID
    name: str
    short_name: str | None = None
    logo_url: str | None = None

    class Config:
        orm_mode = True




class LeagueOut(BaseModel):
    id: UUID
    name: str
    season: str
    lock_date: date

    class Config:
        orm_mode = True
