import pyformula
import math

def main():
    print(pyformula.formulae.maths.pythagoras(a=9, b=9))
    tau = math.pi*2
    print(pyformula.formulae.maths.sine_law(b=9, alpha=tau/4, beta=tau/8))
    print(pyformula.formulae.maths.angle_calculation(alpha=math.pi/4, beta=math.pi/4))
    print(pyformula.formulae.maths.cosine_law(a=9, b=9, gamma=tau/4))
    print()
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
    for instruction in pyformula.formulae.guided.parabola_top(2, 6, 11)[1]:
        print(instruction)

if __name__ == "__main__":
    main()
