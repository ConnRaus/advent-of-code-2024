import fileinput

def parseInput(filename):
    robotList = []
    for line in fileinput.input(filename):
        line = line.strip().split(' ')

        xStart = int(line[0][2:line[0].index(',')])
        yStart = int(line[0][line[0].index(',')+1:])
        xVel = int(line[1][2:line[1].index(',')])
        yVel = int(line[1][line[1].index(',')+1:])

        robotList.append([xStart, yStart, xVel, yVel])

    return robotList

class Robot:
    def __init__(self, xStart, yStart, xVel, yVel):
        self.x = xStart
        self.y = yStart
        self.xVel = xVel
        self.yVel = yVel

    def __str__(self):
        return f"pos: ({self.x} {self.y}) vel: ({self.xVel} {self.yVel})"

    def move(self, width, height):
        newX = (self.x + self.xVel)%width
        newY = (self.y + self.yVel)%height
        self.x, self.y = newX, newY

    def determineQuadrant(self, width, height):
        centerX = int(width/2)
        centerY = int(height/2)
        # quadrants go 
        #  0 1
        #  2 3
        if self.x < centerX:
            # either quadrant 0 or 2
            if self.y < centerY:
                return 0
            elif self.y > centerY:
                return 2
        elif self.x > centerX:
            if self.y < centerY:
                return 1
            elif self.y > centerY:
                return 3
        return None

def visualizeGrid(robotList, width, height):
    grid = [[0 for _ in range(0,width)] for _ in range(0, height)]
    for robot in robotList:
        grid[robot.y][robot.x] += 1
    
    for line in grid:
        print(''.join(str(c) if c != 0 else '.' for c in line))
            

inputList = parseInput('input.txt')
# width, height = 11, 7
width, height = 101, 103

robotList = []
# Create robots
for list in inputList:
   xStart, yStart, xVel, yVel = list[0], list[1], list[2], list[3]
   robotList.append(Robot(xStart, yStart, xVel, yVel))

# Move all robots
for i in range(1, 101):
    for robot in robotList:
        robot.move(width, height)

# After moving, total quadrant robots
quadTotals = [0,0,0,0]
for robot in robotList:
    quadrant = robot.determineQuadrant(width, height)
    if quadrant != None:
        quadTotals[quadrant] += 1


visualizeGrid(robotList, width, height)

total = quadTotals[0]*quadTotals[1]*quadTotals[2]*quadTotals[3]
print(total)