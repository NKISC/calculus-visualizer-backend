"""FastAPI entry point for the Calculus Visualizer backend.

This file only initializes the application and attaches the API router.
Business logic belongs in services and engine modules.
"""

from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.API_VERSION,
)

app.include_router(api_router)
