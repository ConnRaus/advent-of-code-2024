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
    # Set robot counts on grid
    grid = [[0 for _ in range(0,width)] for _ in range(0, height)]
    for robot in robotList:
        grid[robot.y][robot.x] += 1
    
    for line in grid:
        print(''.join(str(c) if c != 0 else '.' for c in line))


def find_robots_in_line(robotList, width, height, n):
    # Put robots on grid
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for robot in robotList:
        grid[robot.y][robot.x] += 1

    # Check rows and columns for n robots in a line
    for y in range(height):
        for x in range(width - (n-1)): 
            if all(grid[y][x + i] == 1 for i in range(n)):
                return True

    return False
            

inputList = parseInput('input.txt')
# width, height = 11, 7
width, height = 101, 103

robotList = []
# Create robots
for list in inputList:
   xStart, yStart, xVel, yVel = list[0], list[1], list[2], list[3]
   robotList.append(Robot(xStart, yStart, xVel, yVel))

    
# NEED TO FIND CHRISTMAS TREE FOR PART 2, USE YOUR EYES TO LOOK
# Potential trees will be shown to you, press enter to go to the next one if its not a tree

i=1
while(True):
    if i%1000 == 0:
        print("Passing iteration", i)

    # Move
    for robot in robotList:
        robot.move(width, height)

    # Look for christmas tree potential spots, 10 robots in a line?
    if find_robots_in_line(robotList, width, height, 10):
        visualizeGrid(robotList, width, height)
        print("ITERATION", i)
        input("Press ENTER to continue search") # hit enter to go to next configuration
    
    i+=1