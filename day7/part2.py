import fileinput
from collections import defaultdict
from itertools import product

def parseInput(filename):
    numberDict = defaultdict(list)
    for line in fileinput.input(filename):
        afterSplit = line.split(":")
        nums = [int(x) for x in afterSplit[1].strip().split()]
        numberDict[int(afterSplit[0])].append(nums)
    return numberDict

numberDict = parseInput("input.txt")

operators = ['+', '*', '||']
total = 0

for answer in numberDict.keys():
    for nums in numberDict[answer]:
        operatorCombinations = [x for x in product(operators, repeat=len(nums)-1)]
        for comboList in operatorCombinations:
            tempSum = nums[0]
            equationString = str(tempSum)

            for i in range(0, len(comboList)):
                operator = comboList[i]
                
                if operator == '+':
                    tempSum += nums[i+1]
                if operator == '*':
                    tempSum *= nums[i+1]
                if operator == '||':
                    tempSum = int(str(tempSum) + str(nums[i+1]))

                equationString += operator + str(nums[i+1])

            if tempSum == answer:
                print('', answer, 'valid with equation', equationString)
                total += answer
                break

print(total)