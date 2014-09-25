from pyformula.formulae import guided


def print_instructions(instructions):
    for instruction in instructions:
        print(instruction.orig_func)
        print(instruction.filled_in_func)
        print(instruction.ans)
        print()
    print()
    print()

def main():
    print_instructions(guided.abc({"a": 1, "b": 4, "c": 1}))
    print_instructions(guided.exponential_sum({"a": 1, "p": 1, "q": 1}))

if __name__ == "__main__":
    main()
