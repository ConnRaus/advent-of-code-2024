# This shows which areas may be a problem for manual testing, it doesn't auto solve
# YOU WILL NEED TO VARY THE INPUT GATES!!!
# I manually changed mine to test various values noting which spots kept printing out

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

def swapGates(gateName1, gateName2):
    temp = gates[gateName1]
    gates[gateName1] = gates[gateName2]
    gates[gateName2] = temp

xWires = list(reversed([i for i in states.keys() if i.startswith('x')]))
yWires = list(reversed([i for i in states.keys() if i.startswith('y')]))
xBin = ''
yBin = ''
for i in range(len(xWires)):
    xBin += str(states[xWires[i]])
    yBin += str(states[yWires[i]])
# We need to find which gates to swap to get this answer
expectedAnswer = bin(int(xBin, 2) + int(yBin, 2))[2:], int(xBin, 2) + int(yBin, 2)

# Test swap gates here
gatesToSwap = [
    ('gvm', 'z26'),
    ('z17', 'wmp'),
    ('qjj', 'gjc'),
    ('qsb', 'z39')
]

for tup in gatesToSwap:
    swapGates(tup[0], tup[1])
    
zGates = reversed(sorted([x for x in gates.keys() if x.startswith('z')]))
output = ''
badSpots = []
for i,gateName in enumerate(zGates):
    gateValue = gates[gateName]

    result = str(solveGate(gateValue))
    
    wire1, gateOperation, wire2 = gateValue
    wire1State, wire2State = states[wire1], states[wire2]
    output += result

    # find spots where bits don't follow correct operations
    # by looking at which bits don't follow correct operations and educated guess swapping the answer can be found
    if expectedAnswer[0][i] != str(solveGate(gateValue)):
        print(f"SPOT {i}: {gateValue[0]}({wire1State}) {gateValue[1]} {gateValue[2]}({wire2State}) -> {gateName} gives {result} instead of {expectedAnswer[0][i]}")

solvedAnswer = output, int(output, 2)

print(solvedAnswer)
print(expectedAnswer)

if solvedAnswer == expectedAnswer:
    print("MAY BE SOLUTION!!!! TRY OTHER INPUTS TOO!")
    gatesToSwap = sorted([gate for pair in gatesToSwap for gate in pair])
    print(','.join(gatesToSwap))