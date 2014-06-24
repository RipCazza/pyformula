from sympy import *
import pyformula

def pythagoras(a=None, b=None, c=None):
    """a^2 + b^2 = c^2"""
    arguments = locals()
    
    _a, _b, _c = symbols('a b c')
    symbol_dict = {'a':_a, 'b':_b, 'c':_c}
    
    expr = Eq(_a**2 + _b**2, _c**2)

    return pyformula.formulae.get_results(expr, arguments, symbol_dict)

def sine_law(a=None, b=None, alpha=None, beta=None):
    """a/sin(alpha) = b/sin(beta)"""
    arguments = locals()

    _a, _b, _alpha, _beta = symbols('a b alpha beta')
    symbol_dict = {'a':_a, 'b':_b, 'alpha':_alpha, 'beta':_beta}

    expr = Eq(_a/sin(_alpha), _b/sin(_beta))

    return pyformula.formulae.get_results(expr, arguments, symbol_dict)

def angle_calculation(alpha=None, beta=None, gamma=None):
    """pi - alpha - beta = gamma"""
    arguments = locals()

    _alpha, _beta, _gamma = symbols('alpha beta gamma')
    symbol_dict = {'alpha':_alpha, 'beta':_beta, 'gamma':_gamma}

    expr = Eq(pi - _alpha - _beta, _gamma)

    return pyformula.formulae.get_results(expr, arguments, symbol_dict)

def cosine_law(a=None, b=None, c=None, gamma=None):
    """c^2 = a^2 + b^2 - 2 * a * b * cos(gamma)"""
    arguments = locals()

    _a, _b, _c, _gamma = symbols('a b c gamma')
    symbol_dict = {'a':_a, 'b':_b, 'c':_c, 'gamma':_gamma}

    expr = Eq(_c**2, _a**2 + _b**2 - 2 * _a * _b * cos(_gamma))

    return pyformula.formulae.get_results(expr, arguments, symbol_dict)
