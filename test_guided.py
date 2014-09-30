from pyformula.formulae import guided
from math import sqrt


def print_instructions(instructions):
    for instruction in instructions:
        print(instruction.orig_func)
        print(instruction.filled_in_func)
        print(instruction.ans)
        print("")
    print("")
    print("")

def main():
    print_instructions(guided.abc({"a": 1, "b": 4, "c": 1}))
    print_instructions(guided.exponential_sum({"a": 1, "p": 1, "q": 1}))
    print_instructions(guided.value_percentage({"a": 1, "b": 2}))
    print_instructions(guided.percentage_new_value({"x": 50, "b": 2}))
    print_instructions(guided.percentage_orig_value({"x": 50, "a": 1}))
    print_instructions(guided.exponential_growth_total({"a": 1, "g": 2,
                                                        "x": 4}))
    print_instructions(guided.exponential_growth_base({"y": 16, "g": 2,
                                                       "x": 4}))
    print_instructions(guided.pythagoras_diagonal({"a": 1, "b": 1}))
    print_instructions(guided.pythagoras_rectangular({"a": 1, "c": sqrt(2)}))
    print_instructions(guided.tangens_radian({"o": 1, "a": 2}))
    print_instructions(guided.sinus_radian({"o": 1, "s": 5}))
    print_instructions(guided.cosinus_radian({"a": 1, "s": 5}))
    print_instructions(guided.tangens_o({"x": 0.5, "a": 3}))
    print_instructions(guided.sinus_o({"x": 0.5, "s": 3}))
    print_instructions(guided.cosinus_a({"x": 0.5, "s": 3}))
    print_instructions(guided.tangens_a({"x": 0.5, "o": 3}))
    print_instructions(guided.sinus_s({"x": 0.5, "o": 3}))
    print_instructions(guided.cosinus_s({"x": 0.5, "a": 3}))

if __name__ == "__main__":
    main()
