"""Main API router for the backend."""

from fastapi import APIRouter

from app.api.routes import compute, health, render
from app.core.config import settings


api_router = APIRouter(prefix=settings.API_PREFIX)
api_router.include_router(health.router)
api_router.include_router(compute.router)
api_router.include_router(render.router)
