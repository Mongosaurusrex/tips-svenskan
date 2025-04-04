from time import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth import routes as auth_routes
from predictions import routes as predictions_routes
from leagues import routes as leagues_routes

app = FastAPI()
start_time = time()

app.include_router(auth_routes.router)
app.include_router(predictions_routes.router)
app.include_router(leagues_routes.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "uptime_seconds": round(time() - start_time),
    }
