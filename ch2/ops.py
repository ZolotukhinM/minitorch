from ir import Program, Value, Node

def get_or_create_value(name, value_map):
    if name not in value_map:
        value_map[name] = Value('t' + str(len(value_map)))
    return value_map[name]
value_map = {}

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

    def input_op(self, A):
        self.val = A

    def print_op(self):
        print('>> ' + str(self.val))

    def assign_op(self, A):
        self.val = A.val
