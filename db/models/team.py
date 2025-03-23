import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.database import Base


class Team(Base):
    __tablename__ = "teams"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    league_id = Column(UUID(as_uuid=True), ForeignKey("leagues.id"))
    name = Column(String, nullable=False)
    short_name = Column(String)
    logo_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    league = relationship("League", back_populates="teams")
    prediction_entries = relationship("PredictionEntry", back_populates="team")
