from fastapi import HTTPException
from sqlalchemy.orm import Session

from auth import repositories
from auth.schemas import UserCreate
from auth.utils import (create_access_token, create_refresh_token,
                        hash_password, verify_password)
from db.models.user import User


def register_user(db: Session, user_in: UserCreate):
    existing = repositories.get_user_by_email(db=db, email=user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_in.password = hash_password(user_in.password)
    return repositories.create_user(db, user_in)


def login_user(db: Session, user_in: UserCreate) -> tuple[str, str]:
    user = repositories.get_user_by_email(db, user_in.email)
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return (
        create_access_token({"sub": str(user.id)}),
        create_refresh_token({"sub": str(user.id)}),
    )


def get_user_profile(db: Session, user_id: str) -> User:
    user = repositories.get_user_by_id(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
