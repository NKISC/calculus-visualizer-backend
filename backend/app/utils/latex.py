"""LaTeX formatting placeholder."""

from typing import Any


def to_latex(value: Any) -> str:
    """Convert a future symbolic value to LaTeX."""

    # TODO: Delegate to SymPy latex formatting after math engine is implemented.
    raise NotImplementedError("LaTeX formatting is not implemented yet.")
