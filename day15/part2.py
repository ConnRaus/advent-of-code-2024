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
            tempLine = []
            conversions = {'#':['#','#'], 'O':['[',']'], '.':['.','.'], '@':['@','.']}
            for c in line.strip():
                tempLine.extend(conversions[c])
            gridLines.append(tempLine)

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
    if nextBlock in '[]':
        if dy == 0:
            return canMove(grid, (x+dx, y+dy), direction)
        else:
            if nextBlock == '[':
                # need to check x+dx, and space to right of it because box is double wide x+1+dx
                return 1 if canMove(grid, (x+dx, y+dy), direction) + canMove(grid, (x+1+dx, y+dy), direction) == 2 else 0
            if nextBlock == ']':
                return 1 if canMove(grid, (x+dx, y+dy), direction) + canMove(grid, (x-1+dx, y+dy), direction) == 2 else 0
    
    print("canMove ERROR, returning None!")
    return None

# Not very happy with this function, theres gotta be a much simpler way to write this
# I would think i could subtract 1 from x if nextBlock is ']' and get rid of the whole 
# second half of the code but that gives an incorrect answer for whatever reason.
def findStack(grid, pos, direction):
    x,y = pos
    dx,dy = direction
    
    # if pushing on left side of box...
    if nextBlock == '[':
        if grid[y+dy][x] == '.' and grid[y+dy][x+1] == '.':
            # nothing on box
            return
        
        if grid[y+dy][x] == '[' and grid[y+dy][x+1] == ']':
            # box on box
            boxStack.add((x, y+dy, '['))
            boxStack.add((x+1, y+dy, ']'))
            findStack(grid, (x, y+dy), direction)
            return
        
        if grid[y+dy][x] == ']':
            # left box
            boxStack.add((x-1, y+dy, '['))
            boxStack.add((x, y+dy, ']'))
            findStack(grid, (x-1, y+dy), direction)

        if grid[y+dy][x+1] == '[':
            # right box
            boxStack.add((x+1, y+dy, '['))
            boxStack.add((x+2, y+dy, ']'))
            findStack(grid, (x+1, y+dy), direction)
        return
            
    # pushing on right side of box....
    elif nextBlock == ']':
        if grid[y+dy][x-1] == '.' and grid[y+dy][x] == '.':
            # nothing on box
            return
        
        if grid[y+dy][x-1] == '[' and grid[y+dy][x] == ']':
            # box on box
            boxStack.add((x-1, y+dy, '['))
            boxStack.add((x, y+dy, ']'))
            findStack(grid, (x, y+dy), direction)
            return
        
        if grid[y+dy][x-1] == ']':
            # left box
            boxStack.add((x-2, y+dy, '['))
            boxStack.add((x-1, y+dy, ']'))
            findStack(grid, (x-1, y+dy), direction)

        if grid[y+dy][x] == '[':
            # right box
            boxStack.add((x, y+dy, '['))
            boxStack.add((x+1, y+dy, ']'))
            findStack(grid, (x+1, y+dy), direction)
        return
    else:
        raise Exception(f"FINDSTACK({x},{y}) NOT A [ or ]")

def moveStack(grid, stack, direction):
    dx,dy = direction
    for x,y,c in stack:
        grid[y][x] = '.'
    for x,y,c in stack:
        grid[y+dy][x+dx] = c

def handleHorizontal(grid, pos):
    ptrX, ptrY = pos
    # moving left-right
    while grid[ptrY][ptrX] != '.':
        alternator = grid[ptrY][ptrX]
        ptrX += dx
        ptrY += dy
    # on the way back, put the boxes in
    while grid[ptrY][ptrX] != '@':
        if alternator == '[':
            grid[ptrY][ptrX] = '['
            alternator = ']'
        else:
            grid[ptrY][ptrX] = ']'
            alternator = '['
        ptrX-=dx
        ptrY-=dy

def printGrid(grid):
    for line in grid:
        print(''.join(line))

# ----------------------------------------------------- #

grid, directionString = parseInput('input.txt')
robotX, robotY = getRobotPosition(grid)

for c in directionString:
    # printGrid(grid)
    # print(c)
    # input()

    chars = ['^', 'v', '<', '>']
    directions = [(0,-1), (0,1), (-1,0), (1,0)]
    dx, dy = directions[chars.index(c)]

    if canMove(grid, (robotX, robotY), (dx, dy)):
        nextBlock = grid[robotY+dy][robotX+dx]

        grid[robotY][robotX] = '.'
        robotX, robotY = robotX+dx, robotY+dy
        grid[robotY][robotX] = '@'

        if nextBlock in '[]':
            ptrX, ptrY = robotX, robotY

            if dy == 0:
                handleHorizontal(grid, (ptrX, ptrY))
            else:
                boxStack = set()
                boxStack.add((ptrX, ptrY, nextBlock))
                if nextBlock == '[':
                    boxStack.add((ptrX+1, ptrY, ']'))
                else:
                    boxStack.add((ptrX-1, ptrY, '['))
                    
                findStack(grid, (ptrX, ptrY), (dx,dy))
                moveStack(grid, boxStack, (dx,dy))

        grid[robotY][robotX] = '@'
                    
printGrid(grid)

def calculateGPSScore(grid):
    total = 0
    for y,line in enumerate(grid):
        for x,c in enumerate(line):
            if c == '[':
                total += y*100 + x
    return total

print(calculateGPSScore(grid))