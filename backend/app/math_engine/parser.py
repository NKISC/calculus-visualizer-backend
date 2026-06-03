# backend/app/math_engine/parser.py

import sympy as sp
from sympy.parsing.latex import parse_latex


def parse_expression(expression: str) -> sp.Expr:
    try:
        return parse_latex(expression)
    except Exception as e:
        raise ValueError(f"There is an expression error: {expression}, {e}")
