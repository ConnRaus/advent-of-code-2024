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

def visualizeAllPaths(cameFrom, current, start, maze, visited):    
    if current[:2] == start[:2]:
        return  # Stop at the start state

    if current in visited:
        return  # Avoid revisiting states

    visited.add(current)  # Mark as visited

    x, y, _ = current
    if maze[y][x] == '.':  # Avoid overwriting markers
        maze[y][x] = 'X'

    for parent in cameFrom.get(current, []):
        visualizeAllPaths(cameFrom, parent, start, maze, visited)

def sumTotalTraveled(maze):
    total = 0
    for row in maze:
        for char in row:
            if char in ['X', 'S', 'E']:
                total += 1
    return total



def findAllShortestPaths(maze, start, end):
    directions = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], 'E'))  # cost, x, y, direction

    costSoFar = {(start[0], start[1], 'E'): 0}
    cameFrom = {}  # Store state → list of parents
    minCost = float('inf')
    endStates = []  # Track all end states with minimal cost

    while pq:
        currentCost, x, y, direction = heapq.heappop(pq)

        # If we reach the end
        if (x, y) == end:
            if currentCost < minCost:
                minCost = currentCost
                endStates = [(x, y, direction)]
            elif currentCost == minCost:
                endStates.append((x, y, direction))
            continue

        # Explore actions
        for action in ['MOVE', 'LEFT', 'RIGHT']:
            if action == 'MOVE':
                dx, dy = directions[direction]
                newX, newY = x + dx, y + dy
                newCost = currentCost + 1

                if canMove(maze, (newX, newY)):
                    state = (newX, newY, direction)
                    if state not in costSoFar or newCost <= costSoFar[state]:
                        costSoFar[state] = newCost
                        if state not in cameFrom:
                            cameFrom[state] = []
                        cameFrom[state].append((x, y, direction))
                        heapq.heappush(pq, (newCost, newX, newY, direction))

            elif action in ['LEFT', 'RIGHT']:
                newDirection = turn(direction, action)
                newCost = currentCost + 1000
                state = (x, y, newDirection)

                if state not in costSoFar or newCost <= costSoFar[state]:
                    costSoFar[state] = newCost
                    if state not in cameFrom:
                        cameFrom[state] = []
                    cameFrom[state].append((x, y, direction))
                    heapq.heappush(pq, (newCost, x, y, newDirection))

    return minCost, endStates, cameFrom


# Main
maze = parseInput("input.txt")
start = findStart(maze)
end = findEnd(maze)

minCost, endStates, cameFrom = findAllShortestPaths(maze, start, end)
visited = set()
for endState in endStates:
    visualizeAllPaths(cameFrom, endState, (start[0], start[1], 'E'), maze, visited)

printMaze(maze)
print(sumTotalTraveled(maze))