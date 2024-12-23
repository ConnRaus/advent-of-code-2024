import fileinput

def parseInput(filename):
    nums = []
    for line in fileinput.input(filename):
        nums.append(int(line.strip()))
    return nums

def mix(n, m):
    return n ^ m

def prune(n):
    return n%16777216

def nextSecret(n):
    # step 1
    result = n*64
    n = mix(n, result)
    n = prune(n)
    # step 2
    result = int(n/32)
    n = mix(n, result)
    n = prune(n)
    # step 3
    result = n*2048
    n = mix(n, result)
    n = prune(n)
    return n

def getNumList(n, iterations):
    returnList = []
    # print(n)
    i = 0
    while i < iterations:
        returnList.append(n%10)
        n = nextSecret(n)
        i+=1
    return returnList

def getDiffList(numList):
    return [numList[i+1] - numList[i] for i in range(len(numList)-1)]

def getSets(diffList):
    potentialSets = set()
    for i in range(3, len(diffList)):
        ele1, ele2, ele3, ele4 = diffList[i-3], diffList[i-2], diffList[i-1], diffList[i]
        potentialSets.add((ele1, ele2, ele3, ele4))
    return potentialSets

# add every set to a lookup dictionary to speed things up
def createDict(diffList):
    d = dict()
    for i in range(3, len(diffList)):
        fourSet = (diffList[i-3], diffList[i-2], diffList[i-1], diffList[i])
        if fourSet not in d:
            d[fourSet] = i
    return d
        

nums = parseInput("input.txt")
numLists = []
diffLists = []
diffDicts = []
possibleSets = set()

# add all potential sets and values to a big set and dictionary to check
for n in nums:
    numList = getNumList(n, 2000+1) # off by 1 error if use just 2000
    diffList = getDiffList(numList)
    diffDict = createDict(diffList)

    numLists.append(numList)
    diffLists.append(diffList)
    diffDicts.append(diffDict)
    
    possibleSets = possibleSets.union(getSets(diffList))

# for every possible set, check it
masterTotal = 0
for setNum,s in enumerate(possibleSets):
    print(f"Set# {setNum}/{len(possibleSets)} - {setNum/len(possibleSets)*100:.2f}%")
    total = 0
    for i,diffDict in enumerate(diffDicts):
        foundIndex = diffDict.get(s)
        if foundIndex != None:
            total += numLists[i][foundIndex+1]
    masterTotal = max(masterTotal, total)

print(masterTotal)

