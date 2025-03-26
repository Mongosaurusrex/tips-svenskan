from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import services
from auth.dependencies import get_current_user
from auth.schemas import RefreshIn, Token, UserCreate, UserOut
from auth.utils import (create_access_token, create_refresh_token,
                        verify_refresh_token)
from db.database import get_db
from db.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    user = services.register_user(db=db, user_in=user_in)
    return user


@router.post("/login", response_model=Token)
def login(user_in: UserCreate, db: Session = Depends(get_db)):
    (access_token, refresh_token) = services.login_user(db=db, user_in=user_in)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/refresh", response_model=Token)
def refresh_token(payload: RefreshIn):
    try:
        data = verify_refresh_token(payload.refresh_token)
        user_id = data.get("sub")
    except:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_access_token({"sub": user_id})
    new_refresh_token = create_refresh_token({"sub": user_id})
    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer",
    }


@router.get("/me", response_model=UserOut)
def get_me(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return services.get_user_profile(db=db, user_id=str(current_user.id))
