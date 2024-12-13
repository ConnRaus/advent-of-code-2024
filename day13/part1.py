import fileinput

def parseInput(filename):
    numHolder = []
    returnList = []
    for i,line in enumerate(fileinput.input(filename)):
        line = line.strip().split(',')
        lineType = i%4 
        
        if lineType == 0 or lineType == 1:
            num1 = int(line[0][line[0].index('+')+1:])
            num2 = int(line[1][line[1].index('+')+1:])
        elif lineType == 2:
            num1 = int(line[0][line[0].index('=')+1:])
            num2 = int(line[1][line[1].index('=')+1:])
        else:
            returnList.append(numHolder)
            numHolder = []
            continue
        numHolder.append(num1)
        numHolder.append(num2)
    # no blank line at end, need to add last section
    returnList.append(numHolder)
    return returnList


def cranmer(a, b, z1, c, d, z2):
    denominator = a*d-b*c
    if denominator == 0:
        return None
    
    x_numerator = z1 * d - z2 * b
    y_numerator = a * z2 - c * z1

    x = x_numerator / denominator
    y = y_numerator / denominator

    return x,y

nums = parseInput('input.txt')


answer = 0
for numList in nums:
    ax1, ay1, ax2, ay2, ansx, ansy = numList
    pushA, pushB = cranmer(ax1, ax2, ansx, ay1, ay2, ansy)
    threshold = 0.0000001
    if abs(pushA-int(pushA)) > threshold or abs(pushB-int(pushB)) > threshold or pushA > 100 or pushB > 100: 
        print("NOT VALID: ", numList, 'A Button', pushA, 'B Button', pushB)
    else: 
        pushA, pushB = int(pushA), int(pushB)
        answer += pushA * 3 + pushB

print(answer)
