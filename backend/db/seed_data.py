import uuid
from datetime import date

from db.database import SessionLocal
from db.models import League, Team
from sqlalchemy.orm import Session


def seed_league(
    db: Session,
    name: str,
    season: str,
    league_lock_date: date,
    team_names: list[tuple[str, str, str]],
):
    existing = db.query(League).filter_by(name=name, season=season).first()
    if existing:
        print(f"✔ {name} {season} already seeded.")
        return

    league = League(
        id=uuid.uuid4(),
        name=name,
        season=season,
        lock_date=league_lock_date,
        is_active=True,
    )
    db.add(league)
    db.commit()
    db.refresh(league)

    for team_name, short_name, logo_url in team_names:
        team = Team(
            id=uuid.uuid4(),
            league_id=league.id,
            name=team_name,
            short_name=short_name,
            logo_url=logo_url,
        )
        db.add(team)

    db.commit()
    print(f"✅ Seeded {name} {season} with {len(team_names)} teams.")


def seed_all():
    db = SessionLocal()
    try:
        seed_league(
            db,
            "Allsvenskan",
            "2025",
            date.today(),
            [
                (
                    "AIK",
                    "AIK",
                    "https://data-20ca4.kxcdn.com/teamImages%2FAIK%2Flo739j5e-aik.png?width=50",
                ),
                (
                    "BK Häcken",
                    "BKH",
                    "https://data-20ca4.kxcdn.com/teamImages%2FBKH%2Flo70ljkw-bkh.png?width=50",
                ),
                (
                    "Degerfors IF",
                    "DEIF",
                    "https://data-20ca4.kxcdn.com/teamImages%2FDEIF%2Flo70mdul-deif.png?width=50",
                ),
                (
                    "Djurgården",
                    "DIF",
                    "https://data-20ca4.kxcdn.com/teamImages%2FDIF%2Flo8dlmz8-Djurgrden.png?width=50",
                ),
                (
                    "GAIS",
                    "GAIS",
                    "https://data-20ca4.kxcdn.com/teamImages%2FGAIS%2Flo72z1bx-gais.png?width=50",
                ),
                (
                    "Halmstads BK",
                    "HBK",
                    "https://data-20ca4.kxcdn.com/teamImages%2FHBK%2Flo70nff2-hbk.png?width=50",
                ),
                (
                    "Hammarby",
                    "HAM",
                    "https://data-20ca4.kxcdn.com/teamImages%2FHAM%2Flopo2qqr-hammarby-2.png?width=50",
                ),
                (
                    "IF Brommapojkarna",
                    "IFBP",
                    "https://data-20ca4.kxcdn.com/teamImages%2FIFBP%2Fle8buz9z-BPlogoguldtransparent.png?width=50",
                ),
                (
                    "IF Elfsborg",
                    "IFE",
                    "https://data-20ca4.kxcdn.com/teamImages%2FIFE%2Flo70p360-ife.png?width=50",
                ),
                (
                    "IFK Göteborg",
                    "GBG",
                    "https://data-20ca4.kxcdn.com/teamImages%2FGBG%2Flo8dlo50-ifkgoteborgfotboll.png?width=50",
                ),
                (
                    "IFK Norrköping",
                    "NOR",
                    "https://data-20ca4.kxcdn.com/teamImages%2FNOR%2Flo70rrkn-nor.png?width=50",
                ),
                (
                    "IFK Värnamo",
                    "VARN",
                    "https://data-20ca4.kxcdn.com/teamImages%2FVARN%2Flo72dctd-varn.png?width=50",
                ),
                (
                    "IK Sirius",
                    "IKS",
                    "https://data-20ca4.kxcdn.com/teamImages%2FIKS%2Flo70q4e1-iks.png?width=50",
                ),
                (
                    "Mjällby AIF",
                    "MAIF",
                    "https://data-20ca4.kxcdn.com/teamImages%2FIFE%2Flo70p360-ife.png?width=50",
                ),
                (
                    "Malmö FF",
                    "MFF",
                    "https://data-20ca4.kxcdn.com/teamImages%2FMFF%2Flo70qypl-mff.png?width=50",
                ),
                (
                    "Öster",
                    "OIF",
                    "https://data-20ca4.kxcdn.com/teamImages%2FOIF%2Flo734oh6-oster.png?width=50",
                ),
            ],
        )
    finally:
        db.close()


if __name__ == "__main__":
    seed_all()
