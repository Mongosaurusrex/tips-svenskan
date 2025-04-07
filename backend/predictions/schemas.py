from typing import List
from uuid import UUID

from pydantic import BaseModel


class PredictionCreate(BaseModel):
    league_id: UUID
    team_ids: List[UUID]


class PredictionEntryOut(BaseModel):
    team_id: UUID
    predicted_position: int


class PredictionOut(BaseModel):
    id: UUID
    league_id: UUID
    entries: list[PredictionEntryOut]

    class Config:
        from_attributes = True
