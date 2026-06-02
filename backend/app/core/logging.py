"""Logging setup for the backend.

TODO: Configure structured logging once computation and rendering tasks produce
meaningful runtime events.
"""

import logging


def configure_logging() -> None:
    """Prepare logging for future backend modules."""

    # Placeholder only. Keep startup quiet until real task execution exists.
    logging.basicConfig(level=logging.INFO)
