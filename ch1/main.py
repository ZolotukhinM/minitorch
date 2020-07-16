from ops import Tensor

def main():
    print("Executing eagerly:")
    a = Tensor([7, 3])
    b = Tensor([5, 6])
    c = Tensor()
    d = Tensor()
    c.mul_op(a, b)
    d.and_op(c, c)
    d.print_op()

if __name__ == '__main__':
    main()
