# -*- coding: utf-8 -*-

from __future__ import division
import math


class Instruction(object):

    def __init__(self, orig_func, filled_in_func, ans):
        self.orig_func = orig_func
        self.filled_in_func = filled_in_func
        self.ans = ans

class Function(object):

    def __init__(self, name, expr, args):
        self.name = name
        self.expr = expr
        self.args = args

class Abc(Function):

    def __call__(self, args):
        a = args["a"]
        b = args["b"]
        c = args["c"]

        instructions = []
        instructions.append(Instruction("0 = ax^2 + bx + c",
                                        "{a}x^2 + {b}x + {c}".format(a=a, b=b,
                                                                    c=c),
                                        "0"))

        D = b**2 - 4 * a * c
        instructions.append(Instruction("D = b^2 - 4 * a * c",
                                        "{b}^2 - 4 * {a} * {c}".format(a=a,
                                                                       b=b,
                                                                       c=c),
                                        str(D)))

        if D < 0:
            raise Exception()

        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)

        instructions.append(Instruction("x1 = (-b + √(D)) / (2 * a) V "
                                        "x2 = (-b - √(D)) / (2 * a)",
                                        "(-{b} + √({D})) / (2 * {a}) V "
                                        "(-{b} - √({D})) / (2 * {a})".format(
                                            b=b, D=D, a=a),
                                        "{x1} V {x2}".format(x1=x1, x2=x2)))

        return instructions

abc = Abc("Abc formule", u"x = (-b +/- √(b^2 - 4 * a * c)) / (2 * a)",
          ["a", "b", "c"])

class ExponentialSum(Function):

    def __call__(self, args):
        a = args["a"]
        p = args["p"]
        q = args["q"]

        instructions = []
        r = p + q
        instructions.append(Instruction("a^(p+q) = a^p * a^q",
                            "{a}^({p}+{q}) = {a}^{p} * {a}^{q}".format(a=a,
                                                                       p=p,
                                                                       q=q),
                            "{a}^{r}".format(a=a, r=r)))

        return instructions

exponential_sum = ExponentialSum("Exponentiële som", "a^(p+q) = a^p * a^q",
                                 ["a", "p", "q"])

class ValuePercentage(Function):

    def __call__(self, args):
        a = args["a"]
        b = args["b"]

        instructions = []
        c = a / b
        x = c * 100
        instructions.append(Instruction("x% = a / b * 100",
                                        "{c} * 100 = {a} / {b} * 100".format(
                                            a=a, b=b, c=c),
                                        "{x}%".format(x=x)))
        return instructions

value_percentage = ValuePercentage("Percentage berekening", "x% = a / b * 100",
                                   ["a", "b"])

class PercentageNewValue(Function):

    def __call__(self, args):
        x = args["x"]
        b = args["b"]

        instructions = []
        c = x * b
        a = c / 100
        instructions.append(Instruction("a = x% / 100 * b",
                                        "{c} / 100 = {x}% / 100 * {b}".format(
                                            x=x, b=b, c=c),
                                        "{a}".format(a=a)))
        return instructions

percentage_new_value = PercentageNewValue("Percentage nieuwe waarde",
                                          "a = x% / 100 * b", ["x", "b"])

class PercentageOrigValue(Function):

    def __call__(self, args):
        x = args["x"]
        a = args["a"]

        instructions = []
        c = x * a
        b = 100 / c
        instructions.append(Instruction("b = 100 / x% * a",
                                        "100 / {c} = 100 / {x}% * {a}".format(
                                            c=c, x=x, a=a),
                                        "{b}".format(b=b)))
        return instructions

percentage_orig_value = PercentageOrigValue("Percentage originele waarde",
                                                    "b = 100 / x% * a",
                                                    ["x", "a"])

class ExponentialGrowthTotal(Function):

    def  __call__(self, args):
        a = args["a"]
        g = args["g"]
        x = args["x"]

        instructions = []
        b = g**x
        y = a * b
        instructions.append(Instruction("y = a * g^x",
                                        "{a} * {b} = {a} * {g}^{x}".format(
                                            a=a, b=b, g=g, x=x),
                                        "{y}".format(y=y)))
        return instructions

exponential_growth_total = ExponentialGrowthTotal("Exponentiële functie",
                                                  "y = a * g^x",
                                                  ["a", "g", "x"])

class ExponentialGrowthBase(Function):

    def __call__(self, args):
        y = args["y"]
        g = args["g"]
        x = args["x"]

        instructions = []
        b = g**x
        a = y / b
        instructions.append(Instruction("a = y / g^x",
                                        "{y} / {b} = {y} / {g}^{x}".format(
                                            y=y, b=b, g=g, x=x),
                                        "{a}".format(a=a)))
        return instructions

exponential_growth_base = ExponentialGrowthBase("Exponentiële deelfunctie",
                                                "a = y / g^x",
                                                ["y", "g", "x"])

class PythagorasDiagonal(Function):

    def __call__(self, args):
        a = args["a"]
        b = args["b"]

        instructions = []
        d = a**2 + b**2
        instructions.append(Instruction("c^2 = a^2 + b^2",
                                        "{a}^2 + {b}^2".format(a=a, b=b),
                                        "{d}".format(d=d)))
        c = math.sqrt(d)
        instructions.append(Instruction("c = √(a^2 + b^2)",
                                        "√{d}".format(d=d),
                                        "{c}".format(c=c)))
        return instructions

pythagoras_diagonal = PythagorasDiagonal("Pythagoras: schuine zijde",
                                        "c^2 = a^2 + b^2",
                                        ["a", "b"])

class PythagorasRectangular(Function):

    def __call__(self, args):
        a = args["a"]
        c = args["c"]

        instructions = []
        d = c**2 - a**2
        instructions.append(Instruction("b^2 = c^2 - a^2",
                                        "{c}^2 - {a}^2".format(c=c, a=a),
                                        "{d}".format(d=d)))
        b = math.sqrt(d)
        instructions.append(Instruction("b = √(c^2 - a^2)",
                                        "√{d}".format(d=d),
                                        "{b}".format(b=b)))
        return instructions

pythagoras_rectangular = PythagorasRectangular("Pythagoras: rechthoekszijde",
                                               "b^2 = c^2 - a^2",
                                               ["a", "c"])

class TangensRadian(Function):

    def __call__(self, args):
        o = args["o"]
        a = args["a"]

        instructions = []
        tan = o / a
        instructions.append(Instruction("tan(x) = overstaand / aanliggend",
                                        "{o} / {a}".format(o=o, a=a),
                                        "{tan}".format(tan=tan)))
        x = math.atan(tan)
        instructions.append(Instruction("x = tan-1(tan(x))",
                                        "tan-1({tan})".format(tan=tan),
                                        "{x}".format(x=x)))
        return instructions

tangens_radian = TangensRadian("Tangens hoekberekening",
                               "tan(x) = overstaand / aanliggend",
                               ["o", "a"])

class SinusRadian(Function):

    def __call__(self, args):
        o = args["o"]
        s = args["s"]

        instructions = []
        sin = o / s
        instructions.append(Instruction("sin(x) = overstaand / schuin",
                                        "{o} / {s}".format(o=o, s=s),
                                        "{sin}".format(sin=sin)))
        x = math.asin(sin)
        instructions.append(Instruction("x = sin-1(sin(x))",
                                        "sin-1({sin})".format(sin=sin),
                                        "{x}".format(x=x)))
        return instructions

sinus_radian = SinusRadian("Sinus hoekberekening",
                           "sin(x) = overstaand / schuin",
                           ["o", "s"])

class CosinusRadian(Function):

    def __call__(self, args):
        a = args["a"]
        s = args["s"]

        instructions = []
        cos = a / s
        instructions.append(Instruction("cos(x) = aanliggend / schuin",
                                        "{a} / {s}".format(a=a, s=s),
                                        "{cos}".format(cos=cos)))
        x = math.acos(cos)
        instructions.append(Instruction("x = cos-1(cos(x))",
                                        "cos-1({cos})".format(cos=cos),
                                        "{x}".format(x=x)))
        return instructions

cosinus_radian = CosinusRadian("Cosinus hoekberekening",
                               "cos(x) = aanliggend / schuin",
                               ["a", "s"])

class TangensO(Function):

    def __call__(self, args):
        x = args["x"]
        a = args["a"]

        instructions = []
        tan = math.tan(x)
        o = tan * a
        instructions.append(Instruction("overstaand = tan(x) * aanliggend",
                                        "{tan} * {a}".format(tan=tan, a=a),
                                        "{o}".format(o=o)))
        return instructions

tangens_o = TangensO("Tangens: overstaand",
                     "overstaand = tan(x) * aanliggend",
                     ["x", "a"])

class SinusO(Function):

    def __call__(self, args):
        x = args["x"]
        s = args["s"]

        instructions = []
        sin = math.sin(x)
        o = sin * s
        instructions.append(Instruction("overstaand = sin(x) * schuin",
                                        "{sin} * {s}".format(sin=sin, s=s),
                                        "{o}".format(o=o)))
        return instructions

sinus_o = SinusO("Sinus: overstaand",
                 "overstaand = sin(x) * schuin",
                 ["x", "s"])

class CosinusA(Function):

    def __call__(self, args):
        x = args["x"]
        s = args["s"]

        instructions = []
        cos = math.cos(x)
        a = cos * s
        instructions.append(Instruction("aanliggend = cos(x) * schuin",
                                        "{cos} * {s}".format(cos=cos, s=s),
                                        "{a}".format(a=a)))
        return instructions

cosinus_a = CosinusA("Cosinus: aanliggend",
                     "aanliggend = cos(x) * schuin",
                     ["x", "s"])

class TangensA(Function):

    def __call__(self, args):
        x = args["x"]
        o = args["o"]

        instructions = []
        tan = math.tan(x)
        a = o / tan
        instructions.append(Instruction("aanliggend = overstaand / tan(x)",
                                        "{o} / {tan}".format(tan=tan, o=o),
                                        "{a}".format(a=a)))
        return instructions

tangens_a = TangensA("Tangens: aanliggend",
                     "aanliggend = overstaand / tan(x)",
                     ["x", "o"])

class SinusS(Function):

    def __call__(self, args):
        x = args["x"]
        o = args["o"]

        instructions = []
        sin = math.sin(x)
        s = o / sin
        instructions.append(Instruction("schuin = overstaand / sin(x)",
                                        "{o} / {sin}".format(sin=sin, o=o),
                                        "{s}".format(s=s)))
        return instructions

sinus_s = SinusS("Sinus: schuin",
                 "schuin = overstaand / sin(x)",
                 ["x", "o"])

class CosinusS(Function):

    def __call__(self, args):
        x = args["x"]
        a = args["a"]

        instructions = []
        cos = math.cos(x)
        s = a / cos
        instructions.append(Instruction("schuin = aanliggend / cos(x)",
                                        "{a} / {cos}".format(cos=cos, a=a),
                                        "{s}".format(s=s)))
        return instructions

cosinus_s = CosinusS("Cosinus: schuin",
                     "schuin = aanliggend / cos(x)",
                     ["x", "a"])
