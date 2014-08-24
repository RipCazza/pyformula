from copy import deepcopy
from sympy import solve


class Function:

    def __init__(self, name, symbols_, expr):
        """Creates a Function with a tuple of symbols and two expression
        strings. The symbols are put in a dictionary with their corresponding
        string values. The two expressions are equated and made into a single
        equation.
        """
        self.name = name
        self.symbols = {}
        for symbol in symbols_:
            self.symbols[str(symbol)] = symbol

        self.expr = expr

    def __call__(self, values):
        """Returns a list of floats. ``values`` is a dictionary with the
        strings of symbols as keys, and their corresponding assigned numerical
        value as value. The symbols in ``temp_expr`` are substituted with
        values from ``values``.

        After the substitution, the expression is solved and the floats of the
        solved expression are returned in a list.
        """
        temp_expr = deepcopy(self.expr)

        for key, value in values.items():
            if value is not None:
                temp_expr = temp_expr.subs(self.symbols[key], value)

        return [result.evalf() for result in solve(temp_expr)]
