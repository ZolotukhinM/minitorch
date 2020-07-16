from ops import Tensor

class ExecutionState:
    def __init__(self, ext_inputs):
        self.ext_input_index = 0
        self.ext_inputs = ext_inputs
        self.ivalues = {}
    def fetch_ext_input(self):
        if self.ext_input_index >= len(self.ext_inputs):
            return [0, 0]
        v = self.ext_inputs[self.ext_input_index]
        self.ext_input_index += 1
        return v
    def set_val(self, ivalue_id, ivalue):
        self.ivalues[ivalue_id] = ivalue
    def get_val(self, ivalue_id):
        if ivalue_id not in self.ivalues:
            self.ivalues[ivalue_id] = Tensor()
        return self.ivalues[ivalue_id]
    def execute_node(self, node):
        inputs = [self.get_val(inp.ID()) for inp in node.inputs]
        output = self.get_val(node.output.ID())
        if node.opcode == 'input':
            output.input_op(self.fetch_ext_input())
        elif node.opcode == 'and':
            output.and_op(*inputs)
        elif node.opcode == 'add':
            output.add_op(*inputs)
        elif node.opcode == 'mul':
            output.mul_op(*inputs)
        elif node.opcode == 'print':
            output.print_op(*inputs)
        elif node.opcode == 'assign':
            output.assign_op(*inputs)
        else:
            print('Unknown op: ' + node.opcode)
            exit(1)

def interpret(ir, ext_inputs):
    state = ExecutionState(ext_inputs)
    for node in ir.nodes:
        state.execute_node(node)
