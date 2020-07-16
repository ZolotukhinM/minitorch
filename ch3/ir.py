class Program:
    def __init__(self):
        self.nodes = []
    def add_node(self, node):
        self.nodes.append(node)
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
        inputs = [str(x.ID()) for x in self.inputs]
        print('{output} {opcode} {inputs}'.format(output=self.output.ID(), \
                                                  opcode=self.opcode,      \
                                                  inputs=' '.join(inputs)))

class Value:
    def __init__(self, name):
        self.node = None
        self.name = name
        self.uses = []
    def ID(self):
        return self.name

def parse(s):
    value_map = {}
    def get_or_create_value(name, value_map):
        if name not in value_map:
            value_map[name] = Value('t' + str(len(value_map)))
        return value_map[name]

    p = Program()
    for l in s.split('\n'):
        parts = l.split(' ')
        if len(parts) < 2:
            continue
        output = parts[0]
        opcode = parts[1]
        inputs = parts[2:]
        new_node = Node(opcode)
        new_node.set_output(get_or_create_value(output, value_map))
        for i in inputs:
            new_node.add_input(get_or_create_value(i, value_map))
        p.add_node(new_node)
    return p
