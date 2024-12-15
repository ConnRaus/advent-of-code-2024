import fileinput

def parseInput(filename):
    gridLines = []
    directionString = ''
    directionsPart = False

    for line in fileinput.input(filename):
        if line.strip() == '':
            directionsPart = True
            continue
        if not directionsPart:
            gridLines += [[c for c in line.strip()]]
        if directionsPart:
            directionString += ''.join(line.strip())
    
    return gridLines, directionString

def getRobotPosition(grid):
    for i,line in enumerate(grid):
        if '@' in line:
            return line.index('@'), i 
    return None

def canMove(grid, pos, direction):
    # direction is like (0,1) etc
    dx, dy = direction
    x, y = pos
    nextBlock = grid[y+dy][x+dx]

    if nextBlock == '#':
        return 0
    if nextBlock == '.':
        return 1
    if nextBlock == 'O':
        return canMove(grid, (x+dx, y+dy), direction)

def printGrid(grid):
    for line in grid:
        print(''.join(line))

grid, directionString = parseInput('input.txt')
robotX, robotY = getRobotPosition(grid)

for c in directionString:
    chars = ['^', 'v', '<', '>']
    directions = [(0,-1), (0,1), (-1,0), (1,0)]
    dx, dy = directions[chars.index(c)]

    if canMove(grid, (robotX, robotY), (dx, dy)):
        nextBlock = grid[robotY+dy][robotX+dx]

        grid[robotY][robotX] = '.'
        robotX += dx
        robotY += dy
        if nextBlock == 'O':
            ptrX, ptrY = robotX, robotY
            while grid[ptrY][ptrX] != '.':
                ptrX += dx
                ptrY += dy
            grid[ptrY][ptrX] = 'O'
        grid[robotY][robotX] = '@'

printGrid(grid)

def calculateGPSScore(grid):
    total = 0
    for y,line in enumerate(grid):
        for x,c in enumerate(line):
            if c == 'O':
                total += y*100 + x
    return total

print(calculateGPSScore(grid))