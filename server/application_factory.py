from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from server.containers import Container
from server.endpoints.health import router as health_router
from server.endpoints.users import router as users_router
from server.endpoints.auth import router as auth_router
from server.endpoints.teams import router as teams_router


def create_routes(app: FastAPI):
    app.include_router(health_router)
    app.include_router(users_router)
    app.include_router(auth_router)
    app.include_router(teams_router)


def create_app() -> FastAPI:
    container = Container()
    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    create_routes(app)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
