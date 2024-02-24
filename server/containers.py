from dependency_injector import containers, providers

from server.database import Database
from server.repositories.users import UserRepository
from server.repositories.teams import TeamsRepository
from server.services.users import UserService
from server.services.auth import AuthService
from server.services.teams import TeamsService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "server.endpoints.health",
            "server.endpoints.users",
            "server.endpoints.auth",
            "server.endpoints.teams",
        ]
    )

    db = providers.Singleton(
        Database,
        db_url="postgresql://postgres:supersecret@localhost/tips_svenskan",  # TODO: ENV VAR
    )

    user_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session
    )
    teams_repository = providers.Factory(
        TeamsRepository, session_factory=db.provided.session
    )

    user_service = providers.Factory(UserService, user_repository=user_repository)
    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    teams_service = providers.Factory(TeamsService, teams_repository=teams_repository)
