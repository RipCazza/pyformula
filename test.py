import pyformula
import math

def main():
    print(pyformula.formulae.maths.pythagoras(a=9, b=9))
    tau = math.pi*2
    print(pyformula.formulae.maths.sine_law(b=9, alpha=tau/4, beta=tau/8))

if __name__ == "__main__":
    main()
