import heapq

def parseInput(filename):
    with open(filename, "r") as file:
        lines = [list(line.strip()) for line in file]
    return lines

def printMaze(maze):
    for row in maze:
        print(''.join(row))

def findStart(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                return (x, y)
    return None

def findEnd(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'E':
                return (x, y)
    return None

def inBounds(maze, pos):
    x, y = pos
    return 0 <= x < len(maze[0]) and 0 <= y < len(maze)

def canMove(maze, pos):
    x, y = pos
    return inBounds(maze, pos) and maze[y][x] != '#'

def turn(direction, action):
    directions = ['N', 'E', 'S', 'W']
    idx = directions.index(direction)
    if action == 'LEFT':
        return directions[(idx - 1) % 4]
    elif action == 'RIGHT':
        return directions[(idx + 1) % 4]

def visualizePath(cameFrom, start, end, maze):
    current = end  # end is (x, y, direction)
    while current != start:
        x,y,_ = current
        maze[y][x] = 'X'  # Place the arrow
        current = cameFrom[current]  # Move to the previous state
    x,y,_ = current
    maze[y][x] = 'X'


def findShortestPath(maze, start, end):
    directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}

    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 'E'))  # cost, x, y, direction
    costSoFar = {(start[0], start[1], 'E'): 0} # Start East
    cameFrom = {}

    while pq:
        currentCost, x, y, direction = heapq.heappop(pq)

        # If reach end
        if (x, y) == end:
            visualizePath(cameFrom, (start[0], start[1], 'E'), (x, y, direction), maze)
            return currentCost

        # Test possibilities
        for action in ['MOVE', 'LEFT', 'RIGHT']:
            if action == 'MOVE':
                dx, dy = directions[direction]
                newX, newY = x + dx, y + dy
                newCost = currentCost + 1

                if canMove(maze, (newX, newY)):
                    state = (newX, newY, direction)
                    if state not in costSoFar or newCost < costSoFar[state]:
                        costSoFar[state] = newCost
                        cameFrom[state] = (x, y, direction)
                        heapq.heappush(pq, (newCost, newX, newY, direction))

            elif action in ['LEFT', 'RIGHT']:
                newDirection = turn(direction, action)
                newCost = currentCost + 1000
                state = (x, y, newDirection)

                if state not in costSoFar or newCost < costSoFar[state]:
                    costSoFar[state] = newCost
                    cameFrom[state] = (x, y, direction)
                    heapq.heappush(pq, (newCost, x, y, newDirection))

    return float('inf')  # If no path is found

# Main
maze = parseInput("input.txt")
start = findStart(maze)
end = findEnd(maze)

cost = findShortestPath(maze, start, end)
printMaze(maze)
print(cost)