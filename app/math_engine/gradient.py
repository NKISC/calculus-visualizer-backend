from typing import Union
from sympy import Symbol, Derivative
from app.math_engine.parser import parse_expression


def compute_gradient(expression: Union[str, list[str]], variables: list[str]) -> Union[list, list[list]]:
    symbols = [Symbol(v) for v in variables]

    if isinstance(expression, str):
        f = parse_expression(expression)
        return [Derivative(f, sym).doit() for sym in symbols]

    else:
        result = []
        i=0
        for comp in expression:
            f = parse_expression(comp)
            row = Derivative(f, symbols[i]).doit()
            i = i + 1
            result.append(row)
        return result
