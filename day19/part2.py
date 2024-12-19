import fileinput

def parseInput(filename):
    targetTowels = []
    for i,line in enumerate(fileinput.input(filename)):
        if i == 0:
            # reverse by key length so largest chunks checked first
            towelSegments = sorted([segment.strip() for segment in line.strip().split(',')], key=len)[::-1]
        elif line.strip() == '':
            continue
        else:
            targetTowels.append(line.strip())
    return towelSegments, targetTowels

def getTargetUsingSegments(segments, target, segmentList=None):
    # create dictionary
    if segmentList == None:
        segmentList = {}
    # return segment from dictionary if in list
    if target in segmentList:
        return segmentList[target]
    # target has been met
    if len(target) == 0:
        return 1
    total = 0
    for segment in segments:
        if target.startswith(segment):
            ways = getTargetUsingSegments(segments, target[len(segment):], segmentList)
            total += ways # dont return immediately to count all ways
    # didnt work
    segmentList[target] = total
    return total

segments, targets = parseInput('input.txt')

total = 0
for target in targets:
    total += getTargetUsingSegments(segments, target)
print(total)