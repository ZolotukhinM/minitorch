from ops import Tensor

class ExecutionState:
    def __init__(self, ext_inputs):
        self.ext_input_index = 0
        self.ext_inputs = ext_inputs
        self.values_to_tensors = {}

    def fetch_ext_input(self):
        v = self.ext_inputs[self.ext_input_index]
        self.ext_input_index += 1
        return v

    def get_actual_tensor(self, value_id):
        if value_id not in self.values_to_tensors:
            self.values_to_tensors[value_id] = Tensor()
        return self.values_to_tensors[value_id]

    def execute_node(self, node):
        input_tensors = [self.get_actual_tensor(inp.ID()) for inp in node.inputs]
        output_tensor = self.get_actual_tensor(node.output.ID())
        if node.opcode == 'input':
            output_tensor.input_op(self.fetch_ext_input())
        elif node.opcode == 'and':
            output_tensor.and_op(*input_tensors)
        elif node.opcode == 'add':
            output_tensor.add_op(*input_tensors)
        elif node.opcode == 'mul':
            output_tensor.mul_op(*input_tensors)
        elif node.opcode == 'print':
            output_tensor.print_op(*input_tensors)
        elif node.opcode == 'assign':
            output_tensor.assign_op(*input_tensors)
        else:
            print('Unknown op: ' + node.opcode)
            exit(1)

def interpret(ir, ext_inputs):
    state = ExecutionState(ext_inputs)
    for node in ir.nodes:
        state.execute_node(node)
