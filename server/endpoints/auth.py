from fastapi import APIRouter, Body, Depends
from dependency_injector.wiring import inject, Provide
from server.endpoints.middleware.JWTBearer import JWTBearer

from server.utils.dataclasses.users import UserSignupSchema, UserLoginSchema
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


@router.post("/login")
@inject
async def login(
    credentials: UserLoginSchema,
    auth_service: AuthService = Depends(Provide[Container.auth_service]),
):
    return auth_service.sign_in(credentials)
