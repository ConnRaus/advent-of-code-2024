def parseInput(filename):
    parsedLines = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        cleanline = line.replace('\n', '').strip()
        if len(cleanline) != 0:
            parsedLines.append(cleanline)
    return parsedLines

def splitLocksKeys(input):
    locks = []
    keys = []
    while len(input) != 0:
        block = []
        for _ in range(7):
            line = input.pop(0)
            block.append(line)

        if block[0] == '#####':
            locks.append(block)
        else:
            keys.append(block)

    return locks, keys
        
def convertToHeightList(lockkey):
    heightList = []
    for y in range(0,len(lockkey[0])):
        columnString = ''
        for x in range(0, len(lockkey)):
            columnString += lockkey[x][y]
        heightList.append(columnString.count('#')-1)
    return heightList

def doesKeyFitLock(lock, key):
    for i in range(0,len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True


input = parseInput('input.txt')
locks, keys = splitLocksKeys(input)

lockHeights = [convertToHeightList(lock) for lock in locks]
keyHeights = [convertToHeightList(key) for key in keys]

total = 0
for lock in lockHeights:
    for key in keyHeights:
        total += doesKeyFitLock(lock, key)
print(total)

