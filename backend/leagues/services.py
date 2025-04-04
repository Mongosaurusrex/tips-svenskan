from uuid import UUID

from fastapi.exceptions import HTTPException

from leagues.repositories import (get_league_by_active_status,
                                  get_teams_by_league)
from sqlalchemy.orm import Session


def list_teams(db: Session, league_id: UUID):
    return get_teams_by_league(db, league_id)


def get_current_active_league(db: Session):
    league = get_league_by_active_status(db)
    
    if not league:
        raise HTTPException(404, detail="No active league found")
         
    return league
