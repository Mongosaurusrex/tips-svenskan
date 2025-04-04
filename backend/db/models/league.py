import uuid
from datetime import datetime

from db.database import Base
from sqlalchemy import Boolean, Column, Date, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class League(Base):
    __tablename__ = "leagues"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    season = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    lock_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=False)

    teams = relationship("Team", back_populates="league")
    predictions = relationship("Prediction", back_populates="league")
