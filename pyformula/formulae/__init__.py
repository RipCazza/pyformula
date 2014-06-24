from sympy import *
import pyformula


def get_results(expr, values, symbols_):
    for i, value in enumerate(values):
        if value is not None:
            expr = expr.subs(symbols_[i], value)

    return [result.evalf() for result in solve(expr)]

from . import maths
