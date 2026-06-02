"""Shared error definitions for future API and service layers.

TODO: Add structured exception classes and FastAPI exception handlers when
real computation and rendering workflows are implemented.
"""


class CalculusVisualizerError(Exception):
    """Base exception for backend-specific errors."""


class UnsupportedTaskTypeError(CalculusVisualizerError):
    """Raised when a task_type is not supported by the backend."""
