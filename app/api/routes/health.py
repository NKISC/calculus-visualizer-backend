"""Health check endpoint."""

from fastapi import APIRouter

from app.core.config import settings
from app.schemas.common import HealthResponse


router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Confirm that the local backend process is running."""

    return HealthResponse(
        success=True,
        message="Calculus Visualizer backend is running.",
        version=settings.API_VERSION,
    )
