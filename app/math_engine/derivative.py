import sympy as sp
from sympy import Symbol, Derivative

from app.math_engine.parser import parse_expression


def compute_derivative(expression: str, variable: str, num: int | None = 1,
                       x_num: float | None = None) -> sp.Expr:  # str输入一个字符串作为需要求导的公式，num不输入则求一阶导数，输入则求对应阶导
    f = parse_expression(expression)
    x = Symbol(variable)
    d = Derivative(f, x, num)
    if x_num is None:
        return d.doit()
    else:
        return d.doit().subs({x: x_num})
