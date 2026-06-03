import sympy as sp
from sympy import Symbol, Derivative
from app.math_engine.parser import parse_expression

def compute_derivative(expression: str, variable: str, num: int | None = 1) -> sp.Expr: # str输入一个字符串作为需要求导的公式，num不输入则求一阶导数，输入则求对应阶导
    f=parse_expression(expression)
    x=Symbol(variable)
    d=Derivative(f,x, num)
    return d.doit()