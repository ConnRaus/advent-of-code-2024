def parseInput(filename, numBytes=1024):
    with open(filename, "r") as file:
        returnSet = set()
        for i,line in enumerate(file):
            if i == numBytes:
                break
            x,y = [int(n) for n in line.strip().split(',')]
            returnSet.add((x,y))
    return returnSet

def printGrid(grid):
    for line in grid:
        print(''.join([str(c) for c in line]))

def bfs(grid, start, end):
    queue = [start]
    visited = set([start])
    parent = {start: None}
    
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        
        x, y = current
        neighbors = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)] # NESW
        for nx, ny in neighbors:
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                if grid[ny][nx] == 0 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current
    
    if end not in parent:
        return []  # no path found
    
    path = []
    node = end
    while node:
        path.append(node)
        node = parent[node]
    return path[::-1]  # reverse path

# inputStuff = ('input2.txt', 7, 12)
inputStuff = ('input.txt', 71, 1024)

fallingBlocks = parseInput(inputStuff[0], inputStuff[2])
# grid as described in problem is indexed 0-70 x 0-70
gridSize = inputStuff[1]
grid = [[0 for _ in range(gridSize)] for _ in range(gridSize)]

for x,y in fallingBlocks:
    grid[y][x] = 1

path = bfs(grid, (0,0), (gridSize-1, gridSize-1))
for x,y in path:
    grid[y][x] = '.'

printGrid(grid)
print(len(path)-1)