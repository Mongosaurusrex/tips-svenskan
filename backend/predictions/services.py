from sqlalchemy.orm import Session
from datetime import datetime
from uuid import UUID
from fastapi import HTTPException

from predictions import repositories as repo

def submit_prediction(
    db: Session, user_id: UUID, league_id: UUID, team_ids: list[UUID]
):
    league = repo.get_league(db, league_id)
    if not league:
        raise HTTPException(404, detail="League not found")

    if datetime.utcnow().date() > league.lock_date:
        raise HTTPException(403, detail="Predictions are locked for this league")

    return repo.create_or_update_prediction(db, user_id, league_id, team_ids)
