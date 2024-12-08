import re

with open('input.txt', 'r') as file:
    inputText = file.read()

# finditer has a .group() which is the found string and a .span() which is a tuple of the beginning and end position
mulMatches = re.finditer(r"mul[(][0-9]+,[0-9]+[)]", inputText)
matchDoDont = re.finditer(r"do[(][)]|don't[(][)]", inputText)

# make matchDoDont a list instead of a stupid useless iterator thing
listDoDont = []
for match in matchDoDont:
    listDoDont.append([match.group(), match.span()[0]]) # stupid thing had to be 0 instead of 1, match and dodont pos were equal before
                                                        # because I was checking the ending of don't() against the beginning of mult()
enabled = True
total = 0
for match in mulMatches:
    # if we passed a do() or don't() change the flag accordingly
    if listDoDont and match.span()[0] > listDoDont[0][1]:
        if(listDoDont[0][0] == "do()"):
            enabled = True
        elif(listDoDont[0][0] == "don't()"):
            enabled = False
        listDoDont.pop(0)

    # after setting flag if needed do same thing as part 1 but now with 800 .group() things making it look ugly
    if enabled:
        num1 = re.search(r"[0-9]+", match.group()).group()
        num2 = re.search(r"[0-9]+", match.group()[match.group().find(',')::]).group() # holy crap this looks bad
        total += int(num1) * int(num2)

print(total)
