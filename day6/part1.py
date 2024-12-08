import fileinput

def getCharXY(array, x, y):
    return array[y][x]

def setCharXY(array, x, y, newChar):
    copyStr = list(array[y])
    copyStr[x] = newChar
    array[y] = "".join(copyStr)

def findGuard(array):
    searchFor = ['^', 'v', '>', '<']
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if getCharXY(array, x, y) in searchFor:
                return x, y

def getForwardTile(array, x, y, direction):
    if y+direction[1] < 0 or y+direction[1] >= len(array) or x+direction[0] < 0 or x+direction[0] >= len(array[0]): return None
    return array[y+direction[1]][x+direction[0]]

filename = "./input.txt"

lines = []
for line in fileinput.input(filename):
    lines.append(line.strip())

# up right down left
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
facingIndex = 0
guardX, guardY = findGuard(lines)


while(getForwardTile(lines, guardX, guardY, directions[facingIndex]) != None):
    # check forward tile, if # facing changes to the next direction.
    if getForwardTile(lines, guardX, guardY, directions[facingIndex]) == '#':
       facingIndex = (facingIndex+1)%len(directions)
       continue
    
    # if not a # then place an X at our current position and move toward facing
    setCharXY(lines, guardX, guardY, 'X')
    guardX = guardX + directions[facingIndex][0] 
    guardY = guardY + directions[facingIndex][1]

setCharXY(lines, guardX, guardY, 'X')

xCount = 0
for line in lines:
    xCount += line.count('X')
print(xCount)