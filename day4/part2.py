import fileinput
import regex as re

filename = './input.txt'

lines = []
for line in fileinput.input(filename):
    lines.append(line.strip())

# Find valid X-MASes
checkStr = ['MSAMS', 'SMASM', 'MMASS', 'SSAMM']
xTotal = 0
for i,line in enumerate(lines):
    for j,c in enumerate(line):
        xString = ""
        # safe zone to look for a's
        if i >= 1 and i < len(lines)-1:
            if j >= 1 and j < len(line)-1:
                xString += lines[i-1][j-1] + lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1] + lines[i+1][j+1]
            
        xTotal += xString in checkStr

print(xTotal)