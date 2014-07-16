from sympy import *
import pyformula
from copy import deepcopy


class Function:
    def __init__(self, name, symbols_, expr_left, expr_right):
        """Creates a Function with a tuple of symbols and two expression
        strings. The symbols are put in a dictionary with their corresponding
        string values. The two expressions are equated and made into a single
        equation.
        """
        self.name = name
        self.symbols = {}
        for symbol in symbols_:
            self.symbols[str(symbol)] = symbol

        self.expr = Eq(sympify(expr_left), sympify(expr_right))

    def calc(self, values):
        """Returns a list of floats. ``values`` is a dictionary with the strings
        of symbols as keys, and their corresponding assigned numerical value as
        value. The symbols in ``temp_expr`` are substituted with values from
        ``values``.

        After the substitution, the expression is solved and the floats of the
        solved expression are returned in a list.
        """
        temp_expr = deepcopy(self.expr)

        for key, value in values.items():
            if value is not None:
                temp_expr = temp_expr.subs(self.symbols[key], value)

        return [result.evalf() for result in solve(temp_expr)]

maths = {
          'pythagoras' : Function("Pythagoras",
                                  symbols('a b c'),
                                  "a**2 + b**2", "c**2"),
          'sine law'   : Function("Sinusregel",
                                  symbols('a b alpha_ beta_'),
                                  "a/sin(alpha_)", "b/sin(beta_)"),
          'cosine law' : Function("Cosinusregel",
                                  symbols('a b c gamma_'),
                                  "a**2 + b**2 - 2 * a * b * cos(gamma_)",
                                  "c**2"),
          'angle calculation' : Function("Hoekberekening",
                                         symbols('alpha_ beta_ gamma_'),
                                         "pi - alpha_ - beta_", "gamma_"),
        }

from . import guided
