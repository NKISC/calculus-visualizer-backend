import sympy
from sympy import Symbol, Derivative

from app.math_engine.parser import parse_expression


def compute_derivative(expression: str, variable: str, num: int = 1,
                       x_num: float | None = None) -> str | Derivative:  # str输入一个字符串作为需要求导的公式，num不输入则求一阶导数，输入则求对应阶导
    f = parse_expression(expression)
    x = Symbol(variable)
    d = Derivative(f, x, num)
    d = d.doit()
    d_str = str(d)
    problematic = ['Derivative', 'nan', 'zoo']
    if any(word in d_str for word in problematic):
        return sympy.nan

    if x_num is None:
        return d
    else:
        return d.subs({x: x_num})
