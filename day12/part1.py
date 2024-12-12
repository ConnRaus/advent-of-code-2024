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
    # returns perimeter
    x, y = pos
    if not isInBounds((x, y), getDimensions(grid)):
        return 1

    letter = grid[y][x]
    if letter != searchLetter:
        return 1
    if (x,y) in regionDict[regionNum]:
        return 0

    # if it made it past those it should be a new same letter for the region
    regionDict[regionNum].append((x, y))
    unusedSpots.remove((x, y))

    result = 0
    neighbors = [(0,-1),(1,0),(0,1),(-1,0)]
    for dx, dy in neighbors:
        result += bfsNeighbors((x+dx, y+dy), searchLetter)
    
    return result


grid = parseInput('input.txt')

# Collection of characters to check which arent in a region yet
unusedSpots = []
for y,line in enumerate(grid):
    for x,char in enumerate(line):
        unusedSpots.append((x,y))

regionDict = defaultdict(list)

totalPrice = 0
regionNum = 0 # Letters can appear multiple times, keep track of regions with an index number instead
while(len(unusedSpots) > 0):
    # Get one of the spots thats not yet in a region
    searchPos = unusedSpots[0]
    searchLetter = grid[searchPos[1]][searchPos[0]]

    # Calculate the perimeter with BFS and save the region coords
    perimeter = bfsNeighbors((searchPos), searchLetter)
    # Regions are saved with their coords, so number of entries = area
    area = len(regionDict[regionNum])

    totalPrice += area*perimeter

    regionNum+=1

print(totalPrice)
