import fileinput

filename = './input.txt'

col1 = []
col2 = []
for line in fileinput.input(filename):
    col1.append(int(line.split()[0]))
    col2.append(int(line.split()[1]))

occurrences = dict()
for num in col2:
    occurrences[num] = occurrences.get(num, 0) + 1

similarityscore = 0
for num in col1:
    similarityscore += occurrences.get(num, 0) * num

print(similarityscore)