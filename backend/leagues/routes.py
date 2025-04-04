from uuid import UUID

from db.database import get_db
from fastapi import APIRouter, Depends
from leagues.schema import LeagueOut, TeamOut
from leagues.services import list_teams, get_current_active_league
from sqlalchemy.orm import Session

router = APIRouter(prefix="/leagues", tags=["leagues"])


@router.get("/{league_id}/teams", response_model=list[TeamOut])
def get_league_teams(league_id: UUID, db: Session = Depends(get_db)):
    return list_teams(db, league_id)

@router.get("/active", response_model=LeagueOut)
def get_active_league(db: Session = Depends(get_db)):
    return get_current_active_league(db)
