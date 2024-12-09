# Get single line input
def parseInput(filename):
    with open(filename, 'r') as file:
        inputText = file.read()
    return inputText.strip()
fileStr = parseInput('input.txt')

# Use single line input to build actual filesystem
blocks = []
for i,c in enumerate(fileStr):
    value = str(int(i/2)) if i % 2 == 0 else '.'
    for _ in range(int(c)):
        blocks.append(value) 

# Go through each character that isnt a . on the end, and each character that is a dot from the beginning will be swapped with it
rightPtr = len(blocks)-1
leftPtr = 0

while(leftPtr < rightPtr):
    while blocks[rightPtr] == '.':
        rightPtr -= 1
    while blocks[leftPtr] != '.':
        leftPtr += 1
    blocks[leftPtr], blocks[rightPtr] = blocks[rightPtr], blocks[leftPtr]
blocks[leftPtr], blocks[rightPtr] = blocks[rightPtr], blocks[leftPtr]

# Calculate the checksum
checksum = 0
for i,c in enumerate(blocks):
    if c != '.':
        checksum += i*int(c) 

print(checksum)