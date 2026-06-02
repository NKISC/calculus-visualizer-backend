"""Expression parsing placeholder.

Future responsibility:
- Convert frontend expression strings into safe SymPy expressions.
- Validate allowed symbols and operations.
- Normalize expression input before calculus operations.
"""

from typing import Any


def parse_expression(expression: str, variables: list[str]) -> Any:
    """Parse an expression string into a future symbolic representation.

    TODO: Use SymPy parsing with validation once computation begins.
    """

    raise NotImplementedError("Expression parsing is not implemented yet.")
