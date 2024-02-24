from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from server.services.teams import TeamsService
from server.containers import Container

router = APIRouter(prefix="/teams", tags=["teams"])


@router.get("/")
@inject
async def get_all_teams(
    teams_service: TeamsService = Depends(Provide[Container.teams_service]),
):
    return teams_service.get_all_teams()
