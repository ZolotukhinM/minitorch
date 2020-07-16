class Program:
    def __init__(self):
        self.nodes = []
        self.values = {}
    def add_node(self, node):
        self.nodes.append(node)
    def get_or_add_value(self, val):
        if val not in self.values:
            self.values[val] = Value(val)
        return self.values[val]
    def dump(self):
        for n in self.nodes:
            n.dump()

class Node:
    def __init__(self, opcode):
        self.opcode = opcode
        self.inputs = []
        self.output = None
    def add_input(self, val):
        self.inputs.append(val)
        val.uses.append(self)
    def set_output(self, val):
        self.output = val
        val.node = self
    def dump(self):
        inputs = [str(x.name) for x in self.inputs]
        print('{output} {opcode} {inputs}'.format(output=self.output.name, \
                                                  opcode=self.opcode,      \
                                                  inputs=' '.join(inputs)))

class Value:
    def __init__(self, name):
        self.node = None
        self.name = name
        self.uses = []
    def ID(self):
        # return id(self)
        return self.name

def parse(s):
    p = Program()
    for l in s.split('\n'):
        parts = l.split(' ')
        if len(parts) < 2:
            continue
        output = parts[0]
        opcode = parts[1]
        inputs = parts[2:]
        new_node = Node(opcode)
        new_node.set_output(p.get_or_add_value(output))
        for i in inputs:
            new_node.add_input(p.get_or_add_value(i))
        p.add_node(new_node)
    return p

def optimize_node(node):
    if node.opcode == 'and':
        if node.inputs[0] == node.inputs[1]:
            print('Replaced:')
            node.dump()
            node.opcode = 'assign'
            node.inputs = node.inputs[:1]
            print('With:')
            node.dump()

def optimize(ir):
    print('== Optimizing ==')
    for i in range(len(ir.nodes)):
        optimize_node(ir.nodes[i])
    print('-- Finished optimizing --\n')

