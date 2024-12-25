def parseInput(filename):
    savedInput = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines:
        appendThis = line.replace('\n', '').strip()
        if len(appendThis) != 0:
            savedInput.append(appendThis)
    return savedInput

locks = []
keys = []

def splitLocksKeys(input):
    while len(input) != 0:
        temp = []
        for _ in range(7):
            piece = input.pop(0)
            temp.append(piece)
        if temp[0] == '#####':
            locks.append(temp)
        else:
            keys.append(temp)
        
def convertToNumList(lockkey):
    temp = []
    for y in range(0,len(lockkey[0])):
        string = ''
        for x in range(0, len(lockkey)):
            string += lockkey[x][y]
        temp.append(string.count('#')-1)
    return temp


input = parseInput('input.txt')
splitLocksKeys(input)

lockNumbers = []
for lock in locks:
    lockNumbers.append(convertToNumList(lock))

keyNumbers = []
for key in keys:
    keyNumbers.append(convertToNumList(key))

def checkLockInKey(lock, key):
    for i in range(0,len(lock)):
        if lock[i] + key[i] > 5:
            return False
    return True

total = 0
for lock in lockNumbers:
    for key in keyNumbers:
        total += checkLockInKey(lock, key)
print(total)

