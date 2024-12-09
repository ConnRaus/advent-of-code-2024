# Get single line input
def parseInput(filename):
    with open(filename, 'r') as file:
        inputText = file.read()
    return inputText.strip()
fileStr = parseInput('input.txt')

def getEndChunk(lst, startVal):
    # Find the last chunk of the same numbers and return indices
    # Find last number that isn't a '.'
    ptr = startVal
    while ptr > 0 and lst[ptr] == '.':
        ptr-=1
    endIndex = ptr+1

    # Find chunk of same values
    while ptr > 0 and lst[ptr] == lst[endIndex-1]:
        ptr-=1
    startIndex = ptr+1

    # print(startIndex, endIndex, lst[startIndex:endIndex])
    return startIndex, endIndex

def findOpenSpot(lst, size, checkTo):
    ptr = 0
    while ptr < checkTo:
        startIndex = 0
        endIndex = 0

        while blocks[ptr] != '.':
            if ptr >= checkTo - 1:
                # print("NO SPOT FOUND")
                return None, None  # Ensure tuple is returned
            ptr += 1
        startIndex = ptr

        while ptr < checkTo and blocks[ptr] == '.':
            ptr += 1
        endIndex = ptr

        if endIndex - startIndex >= size:
            # print("FOUND SPOT", startIndex, endIndex, lst[startIndex:endIndex])
            return startIndex, endIndex

    # print("NO SPOT FOUND")
    return None, None  # Ensure tuple is returned



# Use single line input to build actual filesystem
blocks = []
for i,c in enumerate(fileStr):
    value = str(int(i/2)) if i % 2 == 0 else '.'
    for _ in range(int(c)):
        blocks.append(value) 
# print(blocks)

# Find chunk of right numbers (9,9,9, etc)
left = 0
right = len(blocks)-1
while left < right:
    startIdxNums, endIdxNums = getEndChunk(blocks, right)
    openStart, openEnd = findOpenSpot(blocks, endIdxNums-startIdxNums, startIdxNums)

    # print('left', left, 'right', right)
    if openStart == None or openEnd == None:
        right = startIdxNums-1
        continue
    else:
        left = blocks.index('.') # 30% optimization, theres probably a faster way to set left bound though
        for i,num in enumerate(blocks[startIdxNums:endIdxNums]):
            blocks[openStart+i] = num
            blocks[startIdxNums+i] = '.'
        right = startIdxNums-1

# print(blocks)

# Calculate the checksum
checksum = 0
for i,c in enumerate(blocks):
    if c != '.':
        checksum += i*int(c) 

print(checksum)
