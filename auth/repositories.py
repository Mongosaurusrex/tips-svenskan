from uuid import uuid4

from sqlalchemy.orm import Session

from auth.schemas import UserCreate
from db.models.user import User


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: str) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate) -> User:
    created_user = User(id=uuid4(), email=user.email, hashed_password=user.password)

    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user
