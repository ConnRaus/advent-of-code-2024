# add all numbers X to hashmap as keys, all numbers Y (must be printed after) as values
import fileinput
from collections import defaultdict
import math

filename = './input.txt'

xyPairs = []
lists = []

hitSplit = False
for line in fileinput.input(filename):
    if not line.strip():
        hitSplit = True
        continue        
    if not hitSplit:
        xyPairs.append([int(x) for x in line.strip().split("|")])
    else:
        lists.append([int(x) for x in line.strip().split(",")])

pairDict = defaultdict(list)
for a,b in xyPairs:
    pairDict[a].append(b)

total = 0
for list in lists:
    valid = True
    for i,num in enumerate(list):
        for num2 in list[i+1::]: 
            if not pairDict.get(num) or num2 not in pairDict.get(num):
                valid = False
    if valid:
        total += list[math.floor(len(list)/2)]

print(total)
