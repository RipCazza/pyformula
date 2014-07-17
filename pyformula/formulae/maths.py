from sympy import symbols, Eq, sin, pi
from .Function import Function

a, b, c, d, e, alpha, beta, gamma = symbols('a b c d e alpha beta gamma')

pythagoras = Function("Pythagoras",
                      (a, b, c),
                      Eq(a**2 + b**2, c**2))

sine_law = Function("Sinusregel",
                    (a, b, alpha, beta),
                    Eq(a/sin(alpha), b/sin(beta)))

cosine_law = Function("Cosinusregel",
                      (a, b, alpha, beta),
                      Eq(a/sin(alpha), b/sin(beta)))

angle_calculation = Function("Hoekberekening",
                             (alpha, beta, gamma),
                             Eq(pi - alpha - beta, gamma))
