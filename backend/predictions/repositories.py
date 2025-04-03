from sqlalchemy.orm import Session
from db.models.prediction import Prediction, PredictionEntry
from db.models.league import League
from uuid import UUID
from typing import List


def get_league(db: Session, league_id: UUID) -> League | None:
    return db.query(League).filter(League.id == league_id).first()


def get_prediction_by_user_and_league(
    db: Session, user_id: UUID, league_id: UUID
) -> Prediction | None:
    return (
        db.query(Prediction)
        .filter(Prediction.user_id == user_id, Prediction.league_id == league_id)
        .first()
    )


def create_or_update_prediction(
    db: Session, user_id: UUID, league_id: UUID, team_ids: List[UUID]
):
    prediction = get_prediction_by_user_and_league(db, user_id, league_id)

    if prediction:
        db.query(PredictionEntry).filter(
            PredictionEntry.prediction_id == prediction.id
        ).delete()
    else:
        prediction = Prediction(user_id=user_id, league_id=league_id)
        db.add(prediction)
        db.flush()

    for index, team_id in enumerate(team_ids):
        entry = PredictionEntry(
            prediction_id=prediction.id,
            team_id=team_id,
            predicted_position=index + 1
        )
        db.add(entry)

    db.commit()
    return prediction
