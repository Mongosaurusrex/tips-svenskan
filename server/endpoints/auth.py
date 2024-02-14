from fastapi import APIRouter, Body, Depends
from dependency_injector.wiring import inject, Provide

from server.utils.dataclasses.users import UserSignupSchema
from server.services.auth import AuthService
from server.containers import Container

router = APIRouter(prefix="/auth", tags=["auth", "user"])


@router.post("/signup")
@inject
async def create_user(
    user: UserSignupSchema = Body(),
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
):
    return auth_service.sign_up(user)
