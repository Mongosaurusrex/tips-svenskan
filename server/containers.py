from dependency_injector import containers, providers

from server.database import Database
from server.repositories.user import UserRepository
from server.services.users import UserService
from server.services.auth import AuthService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "server.endpoints.health",
            "server.endpoints.users",
            "server.endpoints.auth",
        ]
    )

    db = providers.Singleton(
        Database,
        db_url="postgresql://postgres:supersecret@localhost/tips_svenskan",  # TODO: ENV VAR
    )

    user_repository = providers.Factory(
        UserRepository, session_factory=db.provided.session
    )

    user_service = providers.Factory(UserService, user_repository=user_repository)
    auth_service = providers.Factory(AuthService, user_repository=user_repository)
