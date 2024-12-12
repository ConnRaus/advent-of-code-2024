import fileinput
from collections import defaultdict

def parseInput(filename):
    lines = []
    for line in fileinput.input(filename):
        lines += [[c for c in line.strip()]]
    return lines

def getDimensions(grid):
    return len(grid[0]), len(grid)

def isInBounds(pos, dims):
    x, y = pos
    xMax, yMax = dims
    if x < 0 or x >= xMax or y < 0 or y >= yMax:
        return False
    return True

def bfsNeighbors(pos, searchLetter):
    x, y = pos
    if not isInBounds((x, y), getDimensions(grid)):
        # Out of bounds contributes 1 to perimeter
        return 1

    letter = grid[y][x]
    if letter != searchLetter:
        # Different letter also contributes to perimeter
        return 1
    if (x, y) in regionDict[regionNum]:
        # Already visited this cell in this region
        return 0

    # if it made it past those it should be a new same letter for the region
    regionDict[regionNum].append((x, y))
    unusedSpots.remove((x, y))

    result = 0
    neighbors = [(0,-1),(1,0),(0,1),(-1,0)]
    for dx, dy in neighbors:
        result += bfsNeighbors((x+dx, y+dy), searchLetter)
    
    return result

def bfsRegion(startPos, searchLetter, grid, unusedSpots, visited):
    # Create new region
    regionDict[regionNum] = []

    # Get perimeter
    perimeter = bfsNeighbors(startPos, searchLetter)
    regionCells = regionDict[regionNum]
    return regionCells, perimeter


grid = parseInput('input.txt')

# Collection of characters to check which arent in a region yet
unusedSpots = []
for y,line in enumerate(grid):
    for x,char in enumerate(line):
        unusedSpots.append((x,y))

regionDict = defaultdict(list)

regionNum = 0 # Letters can appear multiple times, keep track of regions with an index number instead
visited = set()
while unusedSpots:
    # Get one of the spots thats not yet in a region
    searchPos = next(iter(unusedSpots)) 
    searchLetter = grid[searchPos[1]][searchPos[0]]

    regionCells, perimeter = bfsRegion(searchPos, searchLetter, grid, unusedSpots, visited)
    regionNum += 1

def cornerCounter(shape, row, col):
    corners = 0
    for dx, dy in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        diagonalRow = row + dx
        diagonalCol = col + dy
        neighborOne = (row, col + dy)
        neighborTwo = (row + dx, col)

        if (diagonalRow, diagonalCol) in shape:
            if (neighborOne not in shape) and (neighborTwo not in shape):
                corners += 1
        else:
            # Diagonal is not part of shape
            if (neighborOne in shape) == (neighborTwo in shape):
                corners += 1
    return corners

totalPrice = 0
for region, posList in regionDict.items():
    shape = {(y, x) for (x, y) in posList}
    area = len(shape)
    corners = sum(cornerCounter(shape, r, c) for (r, c) in shape)
    # Number of corners is the same as number of sides
    totalPrice += area * corners

print(totalPrice)
