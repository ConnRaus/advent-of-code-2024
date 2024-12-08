import fileinput
import regex as re

filename = './input.txt'

lines = []
for line in fileinput.input(filename):
    lines.append(line.strip())

horizontals = 0
for line in lines:
    horizontals += len(re.findall("XMAS|SAMX", line, overlapped=True))

# Rotate entire array 90 degrees and use same regex to get verticals
rotatedLines = []
for index in range(0, len(lines[0])):
    currentLine = ""
    for line in lines:
        currentLine += line[index]
    rotatedLines.append(currentLine)

verticals = 0
for line in rotatedLines:
    verticals += len(re.findall("XMAS|SAMX", line, overlapped=True))
    
# Now diagonals
checkStr = 'XMAS'
diagTotal = 0
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        downLeft = ""
        downRight = ""
        #at least a few from the bottom
        if i < len(lines)-3:
            # not at left side, can check down left
            if j >= 3:
                downLeft = "" + lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]
            #not at right side, can check down right
            if j < len(line)-3:
                downRight = "" + lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
            
        diagTotal += sum([downRight == checkStr, downRight == checkStr[::-1], downLeft == checkStr, downLeft == checkStr[::-1]])

print(verticals + horizontals + diagTotal)
