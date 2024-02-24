import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from server.database import Base


class Team(Base):
    __tablename__ = "teams"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    logo = Column(String, nullable=False)

    def __repr__(self):
        return f"(id={self.id}, name={self.user_name}, logo={self.logo})"
