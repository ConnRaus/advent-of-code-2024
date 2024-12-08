import fileinput
from collections import defaultdict

def parseInput(filename):
    towersDict = defaultdict(list)
    for y,line in enumerate(fileinput.input(filename)):
        for x,char in enumerate(line.strip()):
            if(char != '.'):
                towersDict[char].append((x, y))
    return towersDict

def getInputDimensions(filename):
    lines = []
    for line in fileinput.input(filename):
        lines.append(line.strip())
    return len(lines[0]), len(lines)

def checkPointExists(dimensions, point):
    return point[0] < dimensions[0] and point[0] >= 0 and point[1] < dimensions[1] and point[1] >= 0

filename = 'input.txt'
towersDict = parseInput(filename)
dimensions = getInputDimensions(filename)

hitCoords = dict()
for antennaChar, coordsList in towersDict.items():

    towercombos = [(pair1, pair2) for pair1 in coordsList for pair2 in coordsList if pair1 != pair2]
        
    for coordpair in towercombos:
        dx = coordpair[0][0] - coordpair[1][0]
        dy = coordpair[0][1] - coordpair[1][1]

        checkCoord1 = (coordpair[0][0], coordpair[0][1])
        checkCoord2 = (coordpair[1][0], coordpair[1][1])

        while checkPointExists(dimensions, checkCoord1):
            hitCoords[checkCoord1] = True
            checkCoord1 = (checkCoord1[0]+dx, checkCoord1[1]+dy)

        while checkPointExists(dimensions, checkCoord2):
            hitCoords[checkCoord2] = True
            checkCoord2 = (checkCoord2[0]-dx, checkCoord2[1]-dy)

print(len(hitCoords))
