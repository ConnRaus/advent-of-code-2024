from functools import cache

def parseInput(filename):
    with open(filename, 'r') as file:
        codes = [line.strip() for line in file]
    return codes

numericKeypad = [
    ['7','8','9'],
    ['4','5','6'],
    ['1','2','3'],
    ['X','0','A']
]

dPad = [
    ['X','^','A'],
    ['<','v','>']
]

def makeKeypadMap(keypad):
    keypadMap = dict()
    for y, row in enumerate(keypad):
        for x, c in enumerate(row):
            keypadMap[c] = (x,y)
    return keypadMap

keypadMap = makeKeypadMap(numericKeypad)
dpadMap = makeKeypadMap(dPad)

def getKeypadInputs(start, end):
    # current (x1,y1), target (x2,ey), missing button (nx,ny)
    x, y = start
    ex, ey = end

    directions = ''
    while (x, y) != (ex, ey):
        
        # avoid missing button at (0,3)
        if x == 0 and ey == 3:
            directions += '>'
            x += 1
        if y == 3 and ex == 0:
            y -= 1
            directions += '^'
        
        # left move
        if x > ex:
            directions += '<'
            x -= 1
        # up move
        elif y > ey:
            directions += '^'
            y -= 1
        # move down
        elif y < ey:
            directions += 'v'
            y += 1
        # move right
        elif x < ex:
            directions += '>'
            x += 1
    # Append 'A' after reaching the button
    return directions + 'A', (x, y)

@cache
def getDpadInputs(start, end):
    movements = ''
    x, y = start
    ex, ey = end

    if numericKeypad[y][x] == 'X':
        raise Exception("CANT GO THERE")

    if y == 0 and ex == 0:
        # go vertical then horizontal
        while y < ey:
            y+=1
            movements += 'v'
        while x != ex:
            if x < ex:
                x += 1
                movements += '>'
            else:
                x -= 1
                movements += '<'     
    else:
        # go horizontal then vertical
        while x != ex:
            if x < ex:
                x += 1
                movements += '>'
            else:
                x -= 1
                movements += '<'
        while y != ey:
            if y < ey:
                y += 1
                movements += 'v'
            if y > ey:
                y -= 1
                movements += '^'
    return movements+'A'

@cache
def moveDpad(code):
    current = dpadMap['A']
    dpadInputs = ''
    for toButton in code:
        if current == dpadMap[toButton]:
            direction = 'A'
        else:
            direction = getDpadInputs(current, dpadMap[toButton])
        current = dpadMap[toButton]
        dpadInputs += direction
    return dpadInputs


codes = parseInput('input.txt')
total = 0
for code in codes:
    numpadInputs = ''
    pos = keypadMap['A'] # start at 'A' on numpad
    for char in code:
        newInput, pos = getKeypadInputs(pos, keypadMap[char])
        numpadInputs+=newInput
    # print(numpadInputs)
    # now we have the inputs we need to type to get '029A' on the numpad

    # use the d-pads to type that input, then those inputs, then those...
    result = numpadInputs
    for _ in range(2):
        result = moveDpad(result)
    print(code, result)

    codeValue = int(code[0:3])
    total += codeValue * len(result)

print(total)