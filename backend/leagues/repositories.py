from uuid import UUID

from db.models.league import League
from db.models.team import Team
from sqlalchemy.orm import Session


def get_teams_by_league(db: Session, league_id: UUID):
    return db.query(Team).filter(Team.league_id == league_id).all()

def get_league_by_active_status(db: Session):
    return db.query(League).filter(League.is_active.is_(True)).first()
