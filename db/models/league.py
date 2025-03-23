import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from db.database import Base


class League(Base):
    __tablename__ = "leagues"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    season = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    teams = relationship("Team", back_populates="league")
    predictions = relationship("Prediction", back_populates="league")
