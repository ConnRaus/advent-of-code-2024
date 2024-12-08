def validateReport(report):

    incvals = [1, 2, 3]
    decvals = [-1, -2, -3]
    biggersmaller = report[1]-report[0]
    
    if len(set(report)) != len(report):
        return 0

    for i in range(1, len(report)):
        if biggersmaller >= 1:
            if report[i] - report[i-1] not in incvals:
                return 0
        if biggersmaller < 0:
            if report[i] - report[i-1] not in decvals:
                return 0
    return 1


import fileinput

filename = './input.txt'

reports = []
for line in fileinput.input(filename):
    reports.append([int(num) for num in line.split()])

count = 0

for report in reports:
    
    if validateReport(report):
        count+=1
        continue

    for index in range(0,len(report)):
        newreport = report[0:index] + report[index+1::]
        if validateReport(newreport):
            count+=1
            break


print(count)


