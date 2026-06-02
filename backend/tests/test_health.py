"""Skeleton tests for the health configuration."""

from app.core.config import settings


def test_backend_version_is_configured() -> None:
    """The API version should match the current skeleton release."""

    assert settings.API_VERSION == "0.1.0"
