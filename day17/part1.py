def parseInput(filename):
    with open(filename, "r") as file:
        program = [int(c) for c in file.readline().strip().split(',')]
    return program

def comboOperand(n):
    returnList = [n, n, n, n, regA, regB, regC]
    return returnList[n]

program = parseInput('input.txt')

# Hardcoding registers much easier than parsing input for them
# Inside of input.txt is only my program instructions list
regA = 59590048
regB = 0
regC = 0
ip = 0

output = []
while ip < len(program)-1:
    instruction = program[ip]

    match instruction:
        case 0:
            # [adv] division, regA = numerator, denominator = 2^combooperand, output to regA
            operand = program[ip+1]
            regA = int(regA / 2**comboOperand(operand))
            ip+=2
        case 1:
            # [bxl] bitwise XOR of regB and literal operand, output to regB
            operand = program[ip+1]
            regB = regB ^ operand
            ip+=2
        case 2:
            # [bst] calculate its combo operand mod 8, output to regB
            operand = program[ip+1]
            regB = comboOperand(operand)%8
            ip+=2
        case 3:
            # [jnz] nothing if regA is 0, else set IP to value of its literal operand. if jumps, dont increase pointer 
            operand = program[ip+1]
            if regA == 0:
                ip+=2
            else:
                ip = operand
        case 4:
            # [bxc] bitwise XOR of regB and regC, output to regB. still reads operand but doesnt use it
            regB = regB^regC
            ip+=2
        case 5:
            # [out] calculates value of combo operand mod 8, prints it. multiple values have comma between
            operand = program[ip+1]
            output.append(str(comboOperand(operand)%8))
            ip+=2
        case 6:
            # [bdv] just like adv but output to regB
            operand = program[ip+1]
            regB = int(regA / 2**comboOperand(operand))
            ip+=2
        case 7:
            # [cdv] just like adv but output to regC
            operand = program[ip+1]
            regC = int(regA / 2**comboOperand(operand))
            ip+=2

print(','.join(output))
