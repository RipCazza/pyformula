from sympy import *
import pyformula
from pyformula.formulae import get_results


def pythagoras(a=None, b=None, c=None):
    """a^2 + b^2 = c^2"""
    a_, b_, c_ = symbols('a b c')
    expr = Eq(a_**2 + b_**2, c_**2)

    return get_results(expr, (a, b, c), (a_, b_, c_))

def sine_law(a=None, b=None, alpha=None, beta=None):
    """a/sin(alpha) = b/sin(beta)"""
    a_, b_, alpha_, beta_ = symbols('a b alpha beta')
    expr = Eq(a_/sin(alpha_), b_/sin(beta_))

    return get_results(expr, (a, b, alpha, beta), (a_, b_, alpha_, beta_))

def angle_calculation(alpha=None, beta=None, gamma=None):
    """pi - alpha - beta = gamma"""
    alpha_, beta_, gamma_ = symbols('alpha beta gamma')
    expr = Eq(pi - alpha_ - beta_, gamma_)

    return get_results(expr, (alpha, beta, gamma), (alpha_, beta_, gamma_))

def cosine_law(a=None, b=None, c=None, gamma=None):
    """c^2 = a^2 + b^2 - 2 * a * b * cos(gamma)"""
    a_, b_, c_, gamma_ = symbols('a b c gamma')
    expr = Eq(c_**2, a_**2 + b_**2 - 2 * a_ * b_ * cos(gamma_))

    return get_results(expr, (a, b, c, gamma), (a_, b_, c_, gamma_))
