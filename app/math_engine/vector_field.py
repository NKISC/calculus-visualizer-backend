from typing import Any
from app.math_engine.parser import parse_expression


def parse_vector_field(vector_field: list[str]) -> list[Any]:
    return [parse_expression(comp) for comp in vector_field]