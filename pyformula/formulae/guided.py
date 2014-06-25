import math
import pyformula


def abc(a, b, c):
    instructions = []
    instructions.append("ax^2 + bx + c = 0")
    instructions.append("{a}x^2 + {b}x + {c} = 0".format(a = a, b = b, c = c))

    D = b**2 - 4 * a * c
    instructions.append("D = b^2 - 4 * a * c")
    instructions.append("{D} = {b}^2 - 4 * {a} * {c}".format(a = a, b = b,
                                                             c = c, D = D))

    if D < 0:
        return Exception()

    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    instructions.append("x = (-b +/- sqrt(D)) / (2 * a)")
    instructions.append("(-{b} +/- sqrt({D})) / (2 * {a})".format(b = b, D = D,
                                                                  a = a))
    instructions.append("x = {x1} V x = {x2}".format(x1 = x1, x2 = x2))

    return [x1, x2], instructions

def exponential_sum(a, p, q):
    instructions = []
    instructions.append("a^p * a^q = a^(p+q)")
    instructions.append("{a}^{p} * {a}^{q} = {a}^({p}+{q})".format(a = a, p = p,
                                                                   q = q))

    r = p + q
    instructions.append("{a}^({p}+{q}) = {a}^{r}".format(a = a, p = p,
                                                         q = q, r = r))

    x = a**r
    instructions.append("{a}^{r} = {x}".format(a = a, r = r, x = x))

    return [x], instructions
