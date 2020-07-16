from ir import Program, Value, Node

def get_or_create_value(name, id_to_value_map):
    if name not in id_to_value_map:
        id_to_value_map[name] = Value('t' + str(len(id_to_value_map)))
    return id_to_value_map[name]

id_to_value = {}

traced_program = Program()
tracing_enabled = False

def start_tracing():
    global tracing_enabled
    traced_program = Program()
    tracing_enabled = True
    id_to_value = {}

def stop_tracing():
    global tracing_enabled
    tracing_enabled = False

def trace_op(opcode, output_tensor, input_tensors):
    if not tracing_enabled:
        return
    new_node = Node(opcode)
    new_node.set_output(get_or_create_value(id(output_tensor), id_to_value))
    for i in input_tensors:
        new_node.add_input(get_or_create_value(id(i), id_to_value))
    traced_program.add_node(new_node)

class Tensor:
    def __init__(self, init_val=[0, 0]):
        trace_op('input', self, [])
        self.val = init_val

    def and_op(self, A, B):
        trace_op('and', self, [A, B])
        (a, b) = (A.val, B.val)
        self.val = [a[i] & b[i] for i in range(len(a))]

    def add_op(self, A, B):
        trace_op('add', self, [A, B])
        (a, b) = (A.val, B.val)
        self.val = [a[i] + b[i] for i in range(len(a))]

    def mul_op(self, A, B):
        trace_op('mul', self, [A, B])
        (a, b) = (A.val, B.val)
        self.val = [a[i] * b[i] for i in range(len(a))]

    def input_op(self, A):
        trace_op('input', self, [])
        self.val = A

    def print_op(self):
        trace_op('print', self, [])
        print('>> ' + str(self.val))

    def assign_op(self, A):
        trace_op('assign', self, [A])
        self.val = A.val
