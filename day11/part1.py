# WARNING: Scary non-DP code that only works for a depth of like 35 below!!!

# Get single line input
def parseInput(filename):
    with open(filename, 'r') as file:
        inputText = file.read()
    return inputText.strip().split()


def blink(lst):
    # If stone has number 0, replace with stone with number 1.
    # If stone has a number with even number of digits, it is replaced by two stones. First half of the digits on left stone, second half of digits on right stone. 
        # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    # else stone is stone multiplied by 2024
    newLst = []
    for ele in lst:
        if ele == '0':
            newLst.append('1')
        elif len(ele)%2==0:
            firstHalf = ele[0:int(len(ele)/2)]
            secondHalf = ele[int(len(ele)/2):len(ele)]
            newLst.append(str(int(firstHalf)))
            newLst.append(str(int(secondHalf)))
        else: 
            newLst.append(str(int(ele)*2024))
    return newLst

numArray = parseInput('input.txt')
for i in range(0,25):
    print("Blink #", i+1)
    numArray = blink(numArray)

print(len(numArray))
