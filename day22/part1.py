import fileinput
import sys
sys.setrecursionlimit(100000)

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

def getNthNum(n, iterations):
    # print(n)
    if iterations == 0:
        return n
    n = nextSecret(n)
    return getNthNum(n, iterations-1)

nums = parseInput("input.txt")

total = 0
for num in nums:
    total += getNthNum(num, 2000)
print(total)