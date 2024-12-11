# Get single line input
def parseInput(filename):
    with open(filename, 'r') as file:
        inputText = file.read()
    lst = [int(x) for x in inputText.strip().split()]
    return lst

# memoize everything!!!
dpList = {}

def recursiveBlink(n, depth=0):
    if depth == 75:
        return 1
    
    if (n, depth) in dpList:
        return dpList[(n, depth)]
        
    if n == 0:
        # was just returning 1 for the longest time instead of recursing here... :(
        result = recursiveBlink(1, depth+1)
    elif len(str(n))%2==0:
        # yeah its ugly but i wanted integers and part 1 code was easy to just change to int and use n
        firstHalf = int(str(n)[0:int(len(str(n))/2)])
        secondHalf = int(str(n)[int(len(str(n))/2):len(str(n))]) 
        result = recursiveBlink(firstHalf, depth+1) + recursiveBlink(secondHalf, depth+1)
    else: 
        result = recursiveBlink(n*2024, depth+1)

    dpList[(n, depth)] = result
    return result

numArray = parseInput('input.txt')
totalSum = 0
for n in numArray:
    totalSum += recursiveBlink(n, 0)

print(totalSum)
