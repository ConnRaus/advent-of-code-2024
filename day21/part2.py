from collections import defaultdict

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

def makeKeypadMap(keypad):
    keypadMap = dict()
    for y, row in enumerate(keypad):
        for x, c in enumerate(row):
            keypadMap[c] = (x,y)
    return keypadMap

keypadMap = makeKeypadMap(numericKeypad)
# got rid of dpadmap, started using letters always after
# getting annoyed when to use letters and when to use positions

def getKeypadInputs(start, end):
    x, y = keypadMap[start]
    ex, ey = keypadMap[end]

    directions = ''
    while (x, y) != (ex, ey):
        # left move
        if x > ex:
            if y == 3 and ex == 0:
                # Hit X so move all the way vertically
                directions += '^' * (y - ey)  
                y = ey
            else:
                directions += '<'
                x -= 1
        # up move
        elif y > ey:
            directions += '^'
            y -= 1
        # move down
        elif y < ey:
            if x == 0 and ey == 3:
                # Hits X so move horizontal all the way
                directions += '>' * (ex - x)  
                x = ex
            else:
                directions += 'v'
                y += 1
        # move right
        elif x < ex:
            directions += '>'
            x += 1
    return directions


# Changed getDpadInputs() to a manual table after fighting with bugs
dpadInputs = {
    ('A', '^'): '<A',
    ('A', '>'): 'vA',
    ('A', 'v'): '<vA',
    ('A', '<'): 'v<<A',
    ('^', 'A'): '>A',
    ('^', '>'): 'v>A',
    ('^', '<'): 'v<A',
    ('^', 'v'): 'vA',
    ('v', 'A'): '^>A',
    ('v', '>'): '>A',
    ('v', '<'): '<A',
    ('v', '^'): '^A',
    ('>', 'A'): '^A',
    ('>', '^'): '<^A',
    ('>', 'v'): '<A',
    ('>', '<'): '<<A',
    ('<', 'A'): '>>^A',
    ('<', '^'): '>^A',
    ('<', 'v'): '>A',
    ('<', '>'): '>>A'
}

def moveDpad():
    # Create a copy of current button press counts to process them
    buttonPressesCopy = dict(buttonPresses)
    
    for code, count in buttonPressesCopy.items():
        current = 'A'  # Always start at button 'A'
        for toButton in code:
            if current == toButton:
                direction = 'A' 
            else:
                direction = dpadInputs[(current, toButton)]
            current = toButton
            buttonPresses[direction] += count  # Add sequence
        buttonPresses[code] -= count  # Remove from original
    return


codes = parseInput('input.txt')  # Read keypad codes from the file
total = 0 
for code in codes:
    # Memoize button presses
    buttonPresses = defaultdict(int)

    current = 'A'  
    for target in code:
        directions = getKeypadInputs(current, target)
        current = target
        directions += 'A' # end sequence
        buttonPresses[directions] += 1  # memoize sequence
    # print([(x,y) for x,y in buttonPresses.items()])
    # now we have the inputs we need to type to get '029A' on the numpad

    # use the d-pads to type that input, then those inputs, then those...
    for _ in range(25):
        moveDpad()

    # calculate result for each code and add to total
    result = 0
    for codeSegment, count in buttonPresses.items():
        result += len(codeSegment) * count
    codeValue = int(code[0:3])
    total += result * codeValue

print(total)
