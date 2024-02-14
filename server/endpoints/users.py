from fastapi import APIRouter, Depends, Response
from dependency_injector.wiring import inject, Provide

from server.services.users import UserService
from server.containers import Container

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
@inject
def get_users(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.get_users()


@router.delete("/{user_id}")
@inject
def delete_user(
    user_id: int, user_service: UserService = Depends(Provide[Container.user_service])
):
    return user_service.delete_user_by_id(user_id)
