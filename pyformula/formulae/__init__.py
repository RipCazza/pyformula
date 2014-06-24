from sympy import *
import pyformula


def get_results(expr, values, symbols_):
    """Iterate over the number/None values of `values`. For every value that is
    not None, perform a substitution.

    `expr` holds references to objects that `symbols_` stores. The corresponding
    substitution value of these objects is stored in the same indices in
    `values` as they do in `symbols_`. Using these common indices, the objects
    in `expr` are replaced with values from `values`.

    After the substitution, the expression is solved and the floats of the
    solved expression are returned in a list.
    """
    for i, value in enumerate(values):
        if value is not None:
            expr = expr.subs(symbols_[i], value)

    return [result.evalf() for result in solve(expr)]

from . import maths
from . import guided
