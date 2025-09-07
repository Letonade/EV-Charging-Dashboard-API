from fastapi import FastAPI

from .adapters.http.errors import not_found_handler
from .config import settings
from .logging_config import logger
from .adapters.http.routers import health, stations, sessions

app = FastAPI(title=settings.app_name, debug=settings.debug)

app.include_router(health.router)
app.include_router(stations.router)
app.include_router(sessions.router)

app.add_exception_handler(KeyError, not_found_handler)

@app.on_event("startup")
async def on_startup():
    logger.info(f"Starting {settings.app_name} in {settings.environment} mode")


@app.on_event("shutdown")
async def on_shutdown():
    logger.info("Shutting down API")
