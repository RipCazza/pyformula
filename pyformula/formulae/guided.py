import math
import pyformula


def abc(a, b, c):
    instructions = []
    instructions.append("ax^2 + bx + c = 0")
    instructions.append("{a}x^2 + {b}x + {c} = 0".format(a=a, b=b, c=c))

    D = b**2 - 4 * a * c
    instructions.append("D = b^2 - 4 * a * c")
    instructions.append("{D} = {b}^2 - 4 * {a} * {c}".format(a=a, b=b, c=c,
                                                             D=D))

    if D < 0:
        return Exception()

    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    instructions.append("x = (-b +/- sqrt(D)) / (2 * a)")
    instructions.append("(-{b} +/- sqrt({D})) / (2 * {a})".format(b=b, D=D,
                                                                  a=a))
    instructions.append("x = {x1} V x = {x2}".format(x1=x1, x2=x2))

    return [x1, x2], instructions

def exponential_sum(a, p, q):
    instructions = []
    instructions.append("a^p * a^q = a^(p+q)")
    instructions.append("{a}^{p} * {a}^{q} = {a}^({p}+{q})".format(a=a, p=p,
                                                                   q=q))

    r = p + q
    instructions.append("{a}^({p}+{q}) = {a}^{r}".format(a=a, p=p, q=q, r=r))

    x = a**r
    instructions.append("{a}^{r} = {x}".format(a=a, r=r, x=x))

    return [x], instructions

def value_percentage(a, b):
    instructions = []
    instructions.append("a / b * 100 = c * 100")

    c = a / b
    instructions.append("{a} / {b} * 100 = {c} * 100".format(a=a, b=b, c=c))

    d = c * 100
    instructions.append("{c} * 100 = {d}%".format(c=c, d=d))

    return [d], instructions

def percentage_new_value(b, d):
    instructions = []
    instructions.append("d / 100 * b = a")

    c = d * b
    instructions.append("{d}% / 100 * {b} = {c} / 100".format(d=d, b=b, c=c))

    a = c / 100
    instructions.append("{c} / 100 = {a}".format(a=a, c=c))

    return [b], instructions

def percentage_original_value(d, a):
    instructions = []
    instructions.append("100 / d * a = b")
    
    b = 100 / d * a
    instructions.append("100 / {d}% * {a} = {b}".format(d=d, a=a, b=b))

    return [b], instructions

def exponential_growth_total(a, b, c):
    instructions = []
    instructions.append("a * b^c = e ")

    d = b**c
    instructions.append("{a} * {b}^{c} = {a} * {d} ".format(a=a, b=b, c=c,
                                                             d=d))

    e = a * d
    instructions.append("{a} * {d} = {e}".format(a=a, d=d, e=e))

    return [e], instructions

def exponential_growth_base(a, b, c):
    instructions = []
    instructions.append("a / b^c = e")

    d = b**c
    instructions.append("{a} / {b}^{c} = {a} / {d}".format(a=a, b=b, c=c, d=d))

    e = a / d
    instructions.append("{a} / {d} = {e}".format(a=a, d=d, e=e))

    return [e], instructions

def exponential_growth_rate(a, b, c):
    instructions = []
    instructions.append("c ROOT(a / b) = d")
    instructions.append("a / b = e")

    e = a / b
    instructions.append("{a} / {b} = {e}".format(a=a, b=b, e=e))
    instructions.append("c ROOT(e) = d")
    
    f = 1 / c
    d = e**f
    instructions.append("{c} ROOT({e}) = {d}".format(c=c, e=e, d=d))

    return [d], instructions

def exponential_growth_time(a, b, c):
    instructions = []
    instructions.append("a / b = c^e")
    instructions.append("c log(a / b) = e")
    instructions.append("a / b = d")

    d = a / b
    instructions.append("{a} / {b} = {d}".format(a=a, b=b, d=d))
    instructions.append("c log(d) = e")

    e = math.log(d, c)
    instructions.append("{c} log({d}) = {e}".format(c=c, d=d, e=e))

    return [e], instructions
 
def parabola_top(a, b, c):
    instructions = []
    instructions.append("ax^2 + bx = 0")
    instructions.append("{a}x^2 + {b}x = 0".format(a=a, b=b))
    instructions.append("x({a}x + {b}) = 0".format(a=a, b=b))
    instructions.append("x = 0 V {a}x + {b} = 0".format(a=a, b=b))
    instructions.append("x = 0 V x = -{b} / {a}".format(a=a, b=b))

    x = -b / a
    instructions.append("x = 0 V x = {x}".format(x=x))
    d = x / 2
    instructions.append("x for symmetry axis is {d}".format(d=d))

    y = a * d**2 + b * d + c
    instructions.append("{a} * {d}^2 + {b} * {d} + {c} = {y}".format(a=a, b=b,
                                                                     c=c, d=d,
                                                                     y=y))
    instructions.append("({d};{y})".format(d=d, y=y))

    return [y], instructions

