import fileinput
from collections import defaultdict

def getCharXY(array, x, y):
    return array[y][x]

def setCharXY(array, x, y, newChar):
    copyStr = list(array[y])
    copyStr[x] = newChar
    array[y] = "".join(copyStr)

def findGuard(array):
    searchFor = ['^', 'v', '>', '<']
    for y in range(0, len(array)):
        for x in range(0, len(array[0])):
            if getCharXY(array, x, y) in searchFor:
                return x, y

def getForwardTile(array, x, y, direction):
    if y+direction[1] < 0 or y+direction[1] >= len(array) or x+direction[0] < 0 or x+direction[0] >= len(array[0]): return None
    return array[y+direction[1]][x+direction[0]]

def getPossibleTiles(array, startX, startY):
    # up right down left
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    facingIndex = 0
    guardX, guardY = startX, startY
    possiblePositions = defaultdict(list)

    while(getForwardTile(array, guardX, guardY, directions[facingIndex]) != None):
        # check forward tile, if # facing changes to the next direction.
        if getForwardTile(array, guardX, guardY, directions[facingIndex]) == '#':
            facingIndex = (facingIndex+1)%len(directions)
            continue
        
        # track possible positions
        possiblePositions[(guardX, guardY)].append(True)
        guardX = guardX + directions[facingIndex][0] 
        guardY = guardY + directions[facingIndex][1]

    return possiblePositions

def parseInput(filename):
    inputArray = []
    for line in fileinput.input(filename):
        inputArray.append(line.strip())
    return inputArray


lines = parseInput("input.txt")
# up right down left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
total = 0
startX, startY = findGuard(lines)
possiblePositions = getPossibleTiles(lines, startX, startY)

for x,y in possiblePositions.keys():

    visited_states = set()
    facingIndex = 0
    guardX, guardY = startX, startY

    if getCharXY(lines, x, y) in ['#', '^']:
        continue
    setCharXY(lines, x, y, '#')

    while(getForwardTile(lines, guardX, guardY, directions[facingIndex]) != None):
        # check forward tile, if # facing changes to the next direction.
        if getForwardTile(lines, guardX, guardY, directions[facingIndex]) == '#':
            # Only need to check if its hit a # from the same side
            if (guardX, guardY, facingIndex) in visited_states:
                total += 1
                break
            visited_states.add((guardX, guardY, facingIndex))
            facingIndex = (facingIndex+1)%len(directions)
            continue
        
        # move
        guardX = guardX + directions[facingIndex][0] 
        guardY = guardY + directions[facingIndex][1]

    setCharXY(lines, x, y, '.')

print(total)

