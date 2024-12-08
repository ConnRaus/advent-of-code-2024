import re

with open('input.txt', 'r') as file:
    inputText = file.read()

matches = re.findall("mul[(][0-9]+,[0-9]+[)]", inputText)

total = 0

for match in matches:
    num1 = re.search(r"[0-9]+", match).group()
    num2 = re.search(r"[0-9]+", match[match.find(',')::]).group()
    
    total += int(num1)*int(num2)

print(total)

