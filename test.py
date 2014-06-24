import pyformula
import math

def main():
    print(pyformula.formulae.maths.pythagoras(a=9, b=9))
    tau = math.pi*2
    print(pyformula.formulae.maths.sine_law(b=9, alpha=tau/4, beta=tau/8))
    print(pyformula.formulae.maths.angle_calculation(alpha=math.pi/4, beta=math.pi/4))
    print(pyformula.formulae.maths.cosine_law(a=9, b=9, gamma=tau/4))

if __name__ == "__main__":
    main()
