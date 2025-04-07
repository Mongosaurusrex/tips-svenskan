from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.dependencies import get_current_user
from db.database import get_db
from predictions import services
from predictions.schemas import PredictionCreate, PredictionOut

router = APIRouter(prefix="/predictions", tags=["predictions"])


@router.post("/predict", status_code=201)
def submit_prediction(
    payload: PredictionCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    prediction = services.submit_prediction(
        db, user.id, payload.league_id, payload.team_ids
    )
    return {"message": "Prediction saved", "prediction_id": str(prediction.id)}


@router.get("/{league_id}", response_model=PredictionOut)
def get_user_prediction(
    league_id: UUID,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return services.get_prediction_by_user(db=db, user_id=user.id, league_id=league_id)
