import fileinput

filename = './input.txt'

col1 = []
col2 = []
for line in fileinput.input(filename):
    col1.append(int(line.split()[0]))
    col2.append(int(line.split()[1]))

col1.sort()
col2.sort()

total = 0

for num1, num2 in zip(col1, col2):
    total += abs(num1 - num2)

print(total)