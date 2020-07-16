from ir import Program, parse
from execution import interpret
from ops import Tensor, stop_tracing, start_tracing, traced_program

def main():
    print("Executing eagerly with tracing:")
    start_tracing()
    a = Tensor([7, 3])
    b = Tensor([5, 6])
    c = Tensor()
    d = Tensor()
    c.mul_op(a, b)
    d.and_op(c, c)
    d.print_op()
    stop_tracing()
    print("Traced IR: {")
    traced_program.dump()
    print("}")
    print("Executing traced program:")
    interpret(traced_program, [[7, 3], [5, 6]])

if __name__ == '__main__':
    main()
