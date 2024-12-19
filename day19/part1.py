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
        return True
    for segment in segments:
        if target.startswith(segment):
            # recursively break down target over and over
            if getTargetUsingSegments(segments, target[len(segment):], segmentList):
                segmentList[target] = True
                return True
    # didnt work
    segmentList[target] = False
    return False

segments, targets = parseInput('input.txt')

total = 0
for target in targets:
    total += getTargetUsingSegments(segments, target)
print(total)