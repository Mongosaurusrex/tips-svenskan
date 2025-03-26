import uuid

from sqlalchemy.orm import Session

from db.database import SessionLocal
from db.models import League, Team


def seed_league(db: Session, name: str, season: str, team_names: list[str]):
    existing = db.query(League).filter_by(name=name, season=season).first()
    if existing:
        print(f"✔ {name} {season} already seeded.")
        return

    league = League(id=uuid.uuid4(), name=name, season=season)
    db.add(league)
    db.commit()
    db.refresh(league)

    for team_name in team_names:
        team = Team(
            id=uuid.uuid4(),
            league_id=league.id,
            name=team_name,
            short_name=team_name.split()[0],
            logo_url=None,
        )
        db.add(team)

    db.commit()
    print(f"✅ Seeded {name} {season} with {len(team_names)} teams.")


def seed_all():
    db = SessionLocal()
    try:
        seed_league(
            db,
            "Premier League",
            "2024/25",
            [
                "Manchester City",
                "Arsenal",
                "Liverpool",
                "Manchester United",
                "Chelsea",
                "Tottenham",
                "Newcastle",
                "Brighton",
                "Aston Villa",
                "Brentford",
                "West Ham",
                "Wolves",
                "Fulham",
                "Crystal Palace",
                "Bournemouth",
                "Everton",
                "Nottingham Forest",
                "Luton Town",
                "Burnley",
                "Sheffield United",
            ],
        )

        seed_league(
            db,
            "Allsvenskan",
            "2025",
            [
                "AIK",
                "Djurgården",
                "IFK Göteborg",
                "IFK Norrköping",
                "Malmö FF",
                "Hammarby",
                "Halmstads BK",
                "Elfsborg",
                "Degerfors",
                "BK Häcken",
                "Degerfors IF",
                "Mjällby AIF",
                "Varbergs BoIS",
                "IK Sirius",
                "GAIS",
                "Öster",
            ],
        )
    finally:
        db.close()


if __name__ == "__main__":
    seed_all()
