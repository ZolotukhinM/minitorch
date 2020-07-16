from ir import Program, Value, Node

def get_or_create_value(name, value_map):
    if name not in value_map:
        value_map[name] = Value('t' + str(len(value_map)))
    return value_map[name]
value_map = {}

traced_program = Program()
tracing_enabled = False

def start_tracing():
    global tracing_enabled
    traced_program = Program()
    tracing_enabled = True

def stop_tracing():
    global tracing_enabled
    tracing_enabled = False

def trace_op(opcode, output, inputs):
    if not tracing_enabled:
        return
    new_node = Node(opcode)
    new_node.set_output(get_or_create_value(output, value_map))
    for i in inputs:
        new_node.add_input(get_or_create_value(i, value_map))
    traced_program.add_node(new_node)

class Tensor:
    def __init__(self, init_val=[0, 0]):
        trace_op('input', id(self), [])
        self.val = init_val

    def and_op(self, A, B):
        trace_op('and', id(self), [id(A), id(B)])
        (a, b) = (A.val, B.val)
        self.val = [a[i] & b[i] for i in range(len(a))]

    def add_op(self, A, B):
        trace_op('add', id(self), [id(A), id(B)])
        (a, b) = (A.val, B.val)
        self.val = [a[i] + b[i] for i in range(len(a))]

    def mul_op(self, A, B):
        trace_op('mul', id(self), [id(A), id(B)])
        (a, b) = (A.val, B.val)
        self.val = [a[i] * b[i] for i in range(len(a))]

    def input_op(self, A):
        trace_op('input', id(self), [])
        self.val = A

    def print_op(self):
        trace_op('print', id(self), [])
        print('>> ' + str(self.val))

    def assign_op(self, A):
        trace_op('assign', id(self), [id(A)])
        self.val = A.val
