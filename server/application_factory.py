from fastapi import FastAPI

from server.containers import Container
from server.endpoints.health import router as health_router
from server.endpoints.users import router as users_router
from server.endpoints.auth import router as auth_router


def create_routes(app: FastAPI):
    app.include_router(health_router)
    app.include_router(users_router)
    app.include_router(auth_router)


def create_app() -> FastAPI:
    container = Container()
    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container
    create_routes(app)

    return app
