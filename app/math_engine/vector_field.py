from typing import Any

from sympy import symbols

from app.math_engine.parser import parse_expression


def parse_vector_field(vector_field: list[str]) -> list[Any]:
    return [parse_expression(comp) for comp in vector_field]


def evaluate_vector_field(vector_field: list[str],
                          variables: list[str], point: dict[str, float]) -> list[float]:
    components = parse_vector_field(vector_field)

    syms = [symbols(v) for v in variables]

    subs_dict = {syms[i]: point[var] for i, var in enumerate(variables)}

    result = []
    for comp in components:
        val = comp.subs(subs_dict)
        if val.is_number:
            result.append(float(val))
        else:
            result.append(val)

    return result


def evaluate_vector_field_multiple(vector_field: list[str], variables: list[str],
                                   points: list[dict[str, float]]) -> list[list[float]]:
    results = []
    for point in points:
        results.append(evaluate_vector_field(vector_field, variables, point))
    return results