def parseInput(filename):
    with open(filename, "r") as file:
        program = [int(c) for c in file.readline().strip().split(',')]
    return program

program = parseInput('input.txt') 

# Functionalized to test differnet regAs
def runProgram(program, regA):
    output = []
    regA = regA
    regB = 0
    regC = 0
    ip = 0

    def comboOperand(n):
        returnList = [n, n, n, n, regA, regB, regC]
        return returnList[n]

    while ip < len(program)-1:
        instruction = program[ip]
        
        match instruction:
            case 0:
                # [adv] division, regA = numerator, denominator = 2^combo operand, output to regA
                operand = program[ip+1]
                regA = regA // 2**comboOperand(operand)
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
                regB = regA // 2**comboOperand(operand)
                ip+=2
            case 7:
                # [cdv] just like adv but output to regC
                operand = program[ip+1]
                regC = regA // 2**comboOperand(operand)
                ip+=2
    return ','.join(output)

# Function to increment specific spot in program output
# Program output kinda base 8 sort of except out of order
def incrementSpot(spotToIncrement):
    return 8**(spotToIncrement-1)

# 16 digit outputs must be in range 8^15-8^16, thats where the magic numbers 35184372088832 and 281474976710656 come from
# Search for the number to put into regA that makes the quine valid
def search(n=35184372088832):
    # If result program would be more than 16 digits it's not possible
    if n >= 281474976710656:
        return None
    # Find invalid number in program output from right to left and increment it
    for i in range(len(program), -1, -1):
        if int(program[i-1]) != int(runProgram(program, n).split(',')[i-1]):
            return search(n+incrementSpot(i))
        # Made it through and found it
        if i == 0: return n
     
print(search())
