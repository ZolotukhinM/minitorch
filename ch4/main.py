from ir import Program, parse, optimize
from execution import interpret
from ops import Tensor, stop_tracing, start_tracing, traced_program

def main():
    # Script mode:
    print("=== Scripting mode ===")
    program = """
a input
b input
c input
d input
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

    # Eager mode + tracing:
    print("=== Eager mode + tracing ===")
    start_tracing()
    print("Executing eagerly:")
    a = Tensor([7, 3])
    b = Tensor([5, 6])
    c = Tensor()
    d = Tensor()
    c.mul_op(a, b)
    d.and_op(c, c)
    d.print_op()
    stop_tracing()
    print("Traced: {")
    traced_program.dump()
    print("}")
    print("Executing traced program:")
    interpret(traced_program, [[7, 3], [5, 6]])

    print("Optimizing program:")
    optimize(ir)
    print("Optimized IR: {")
    ir.dump()
    print("}")
    print("Executing optimized program:")
    interpret(ir, [[7, 3], [5, 6]])

if __name__ == '__main__':
    main()
