from sqlalchemy import Column, Integer, String, Boolean

from server.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    def __repr__(self):
        return f"(id={self.id}, user_name={self.user_name}, hashed_password={self.hashed_password})"
