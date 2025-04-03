import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.database import Base


class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    league_id = Column(UUID(as_uuid=True), ForeignKey("leagues.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    shared_slug = Column(String, unique=True)

    user = relationship("User", back_populates="predictions")
    league = relationship("League", back_populates="predictions")
    entries = relationship("PredictionEntry", back_populates="prediction")

    __table_args__ = (
        UniqueConstraint('user_id', 'league_id', name='_user_league_uc'),
    )


class PredictionEntry(Base):
    __tablename__ = "prediction_entries"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prediction_id = Column(UUID(as_uuid=True), ForeignKey("predictions.id"))
    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"))
    predicted_position = Column(Integer, nullable=False)

    prediction = relationship("Prediction", back_populates="entries")
    team = relationship("Team", back_populates="prediction_entries")
