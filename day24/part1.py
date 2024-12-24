def parseInput(filename):
    with open(filename, 'r') as file:
        states = dict()
        gates = dict()
        for line in file:
            if ':' in line.strip():
                wire, value = line.strip().split(':')
                wire, value = wire.strip(), int(value.strip())
                states[wire] = value
            if '->' in line.strip():
                splits = line.split()
                wire1, op, wire2, _, wire3 = splits
                gates[wire3] = (wire1, op, wire2)
    return states, gates

states, gates = parseInput('input.txt')

def XOR(a, b):
    return a ^ b
def AND(a, b):
    return a & b
def OR(a, b):
    return a | b

operations = {
    'AND' : AND,
    'OR' : OR,
    'XOR' : XOR
}

def solveGate(gate):
    w1, op, w2 = gate
    if w1 not in states.keys():
        states[w1] = solveGate(gates[w1]) 
    if w2 not in states.keys():
        states[w2] = solveGate(gates[w2])   
    return operations[op](states[w1], states[w2])

# gates need to be reversed for little endian
zGates = reversed(sorted([x for x in gates.keys() if x.startswith('z')]))
output = ''
for gateName in zGates:
    gateValue = gates[gateName]
    output += str(solveGate(gateValue))
print(int(output, 2))
