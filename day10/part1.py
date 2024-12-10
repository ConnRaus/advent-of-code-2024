import fileinput

def parseInput(filename):
    lines = []
    for line in fileinput.input(filename):
        tempLine = []
        for c in line.strip():
            tempLine.append(int(c))
        lines.append(tempLine)
    return lines

def getDimensions(heightMap):
    #x,y
    return len(heightMap[0]),len(heightMap)

def getStartingPositions(heightMap):
    startingPositions = []
    for i,hArray in enumerate(heightMap):
        for j,h in enumerate(hArray):
            if(h == 0): startingPositions.append((j,i))   
    return startingPositions

def isInMap(pos, dimensions):
    if pos[0] >= 0 and pos[0] < dimensions[0] and pos[1] >= 0 and pos[1] < dimensions[1]:
        return True
    return False

def printPos(heightMap, pos):
    if isInMap(pos, getDimensions(heightMap)): print('Position', pos[0], pos[1], 'is', heightMap[pos[1]][pos[0]])

def recursePaths(heightMap, pos, prevHeight=-1, foundNines=None):
    if foundNines is None:
        foundNines = set()
    
    # check to make sure in bounds:
    if not isInMap(pos, getDimensions(heightMap)):
        return 0
    
    currentX, currentY = pos
    currentHeight = heightMap[currentY][currentX]

    # check if its movable to
    if currentHeight-prevHeight != 1:
        return 0
    if currentHeight == 9:
        if pos in foundNines:
            return 0
        foundNines.add(pos)
        return 1

    # north east south west 
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    totalPaths = 0
    for dx, dy in directions:
        totalPaths+= recursePaths(heightMap, (currentX+dx, currentY+dy), currentHeight, foundNines)

    return totalPaths

heightMap = parseInput("./input.txt")
xDim,yDim = getDimensions(heightMap)
startPosList = getStartingPositions(heightMap)

total = 0
for startPos in startPosList:
    total += recursePaths(heightMap, startPos)
print(total)