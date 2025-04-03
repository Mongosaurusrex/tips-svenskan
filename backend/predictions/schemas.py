from typing import List
from pydantic import BaseModel
from uuid import UUID

class PredictionCreate(BaseModel):
    league_id: UUID
    team_ids: List[UUID]
