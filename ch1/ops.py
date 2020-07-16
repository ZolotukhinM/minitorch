class Tensor:
    def __init__(self, init_val=[0, 0]):
        self.val = init_val

    def and_op(self, A, B):
        (a, b) = (A.val, B.val)
        self.val = [a[i] & b[i] for i in range(len(a))]

    def add_op(self, A, B):
        (a, b) = (A.val, B.val)
        self.val = [a[i] + b[i] for i in range(len(a))]

    def mul_op(self, A, B):
        (a, b) = (A.val, B.val)
        self.val = [a[i] * b[i] for i in range(len(a))]

    def print_op(self):
        print('>> ' + str(self.val))

    def assign_op(self, A):
        self.val = A.val
