import pyformula
import math
from sympy import *

def main():
    for instruction in pyformula.formulae.guided.abc(2, 10, 3)[1]:
        print(instruction)

    print()

    from pyformula import formulae
    print(formulae.maths['pythagoras'].calc({'a':2, 'b':2}))

if __name__ == "__main__":
    main()
