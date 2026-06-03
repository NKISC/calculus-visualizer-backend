"""Application configuration values.

Keep configuration simple for the skeleton phase. If environment-specific
settings are needed later, this module can be expanded without changing routes.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Static settings used by the FastAPI application."""

    PROJECT_NAME: str = "Calculus Visualizer Backend"
    PROJECT_DESCRIPTION: str = (
        "Local computation and rendering backend for calculus visualization."
    )
    API_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api"


settings = Settings()
