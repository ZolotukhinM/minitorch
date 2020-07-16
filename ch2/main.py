from ir import Program, parse
from execution import interpret
from ops import Tensor

def main():
    print("=== Scripting mode ===")
    program = """
a input
b input
c mul a b
d and c c
d print
"""
    ir = parse(program)
    print("Parsed IR: {")
    ir.dump()
    print("}")
    print("Executing parsed program:")
    interpret(ir, [[7, 3], [5, 6]])


if __name__ == '__main__':
    main()
