from app.math_engine.parser import parse_expression
from sympy import Symbol, Integral, oo
import sympy as sp

def compute_integral(expression: str,variable: str,lower_bound: float | None = None,upper_bound: float | None = None) -> sp.Expr:
    f=parse_expression(expression)
    x=Symbol(variable)
    if lower_bound is None and upper_bound is None:
        integral=Integral(f,x)
        return integral.doit()
    else:
        integral=Integral(f,(x,lower_bound,upper_bound))
        return integral.doit()