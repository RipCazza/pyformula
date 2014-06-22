from sympy import *
import pyformula
from . import maths

def get_results(expr, values, symbol_dict):
    """Iterate over the key-value pairs of `values`. For every value that is not
    None, perform a substitution.

    `expr` holds objects that `symbol_dict` references to. The keys to these
    objects are identical to the keys that `values` has. The substitution takes
    advantage of that. Using the common key, it replaces the object in `expr`
    with its corresponding value.

    After the substitution, the expression is solved and the floats of the
    solved expression are returned in a list.
    """
    for key, value in values.items():
        if value is not None:
            expr = expr.subs(symbol_dict[key], value)

    return [result.evalf() for result in solve(expr)]
