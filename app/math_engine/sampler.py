"""Numerical sampling placeholder.

Future responsibility:
- Use NumPy to sample scalar fields and vector fields.
- Produce frontend-friendly visualization data.
- Keep sampling output separate from symbolic math results.
"""

from typing import Any


def sample_scalar_field(expression: Any, variables: list[str], parameters: dict[str, Any]) -> dict[str, Any]:
    """Generate future numeric samples for scalar visualizations."""

    # TODO: Implement NumPy sampling after visualization data contracts are set.
    raise NotImplementedError("Scalar field sampling is not implemented yet.")


def sample_vector_field(vector_field: list[Any], variables: list[str], parameters: dict[str, Any]) -> dict[str, Any]:
    """Generate future numeric samples for vector visualizations."""

    # TODO: Implement NumPy sampling after vector visualization contracts are set.
    raise NotImplementedError("Vector field sampling is not implemented yet.")
