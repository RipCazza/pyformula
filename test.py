import pyformula
import math
from sympy import *

def main():
    for instruction in pyformula.formulae.guided.abc(2, 10, 3)[1]:
        print(instruction)
    for instruction in pyformula.formulae.guided.exponential_sum(2, 2, 2)[1]:
        print(instruction)
    for instruction in pyformula.formulae.guided.value_percentage(4, 5)[1]:
        print(instruction)
    for instruction in pyformula.formulae.guided.percentage_new_value(80, 4)[1]:
        print(instruction)
    for instruction in pyformula.formulae.guided.exponential_growth_total(2, 2 ,2)[1]:
        print(instruction)
    for instruction in pyformula.formulae.guided.exponential_growth_base(8, 2 ,2)[1]:
        print(instruction)
    for instruction in pyformula.formulae.guided.exponential_growth_rate(2, 2 ,8)[1]:
        print(instruction)
    for instruction in pyformula.formulae.guided.exponential_growth_time(8, 2 ,2)[1]:
        print(instruction)

    print()

    from pyformula import formulae
    print(formulae.maths['pythagoras'].calc({'a':2, 'b':2}))

if __name__ == "__main__":
    main()
