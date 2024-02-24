import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from server.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    def __repr__(self):
        return f"(id={self.id}, user_name={self.user_name}, hashed_password={self.hashed_password})"
