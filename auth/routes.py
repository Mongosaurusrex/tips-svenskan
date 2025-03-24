from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth import services
from auth.schemas import Token, UserCreate, UserOut
from db.database import get_db 

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = services.register_user(db=db, user_in=user_in)
    return user


@router.post("/login", response_model=Token)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    token = services.login_user(db=db, user_in=user_in)
    return {"access_token": token, "token_type": "bearer"}
