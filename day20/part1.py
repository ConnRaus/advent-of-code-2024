from collections import deque

def parseInput(filename):
    with open(filename, 'r') as file:
        maze = [list(line.rstrip('\n')) for line in file]
    return maze

def getStartEnd(maze):
    start = end = None
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)
    return start, end

def isInBounds(pos, maze):
    x,y = pos
    return 0 <= y < len(maze) and 0 <= x < len(maze[0])

def getNeighbors(pos, maze):
    x, y = pos
    neighbors = []
    directions = [(0,-1), (1,0), (0,1), (-1,0)]  # NESW
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if isInBounds((nx, ny), maze):
            if maze[ny][nx] in ('.', 'E'):
                neighbors.append((nx, ny))
    return neighbors

def bfs(maze, start, end):
    queue = deque()
    queue.append(start)
    visited = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for neighbor in getNeighbors(current, maze):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    # Reconstruct path
    path = []
    at = end
    while at != start:
        path.append(at)
        at = visited[at]
    path.append(start)
    path.reverse()
    return path

def createDistanceDict(path):
    distanceMap = {pos: step for step, pos in enumerate(path)}
    return distanceMap

def printMaze(maze):
    for row in maze:
        print(''.join(row))

def checkShortcuts(pos, distanceDict):
    if pos not in path:
        print("Shortcuts can only be checked from points on the path")
        return None
    
    directions = [(0,-2), (2,0), (0,2), (-2,0)]  # NESW
    savings = [0 for _ in directions]
    x,y = pos
    for i,(dx,dy) in enumerate(directions):
        nx, ny = x+dx, y+dy
        if isInBounds((nx, ny), maze):
            if (nx, ny)  in distanceDict.keys():
                savings[i] = distanceDict[(nx,ny)] - distanceDict[pos] - 2
    return savings


filename = 'input.txt'
maze = parseInput(filename)
start, end = getStartEnd(maze)
path = bfs(maze, start, end)

distanceDict = createDistanceDict(path)

total = 0
for pos in path:
    for num in checkShortcuts(pos, distanceDict):
        if num >= 100:
            total+=1
print(total)