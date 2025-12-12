direction = 1
currentNum = 50
zeros = 0

file = open("Day 1/realData.txt","r")
for line in file.read().split('\n'):
    lineLen = len(line)
    for j in range(0, len(line)):
        if j == 0:#if its the first character of a line,
            if line[j] == "L":#and if its left, direction is negative, or right and its positive
                direction = -1
            else:
                direction = 1
    if line == "":
        break

    print(currentNum)
    for i in range(0,int(line[1:])):
        if line[0] == "L":
            currentNum = currentNum - 1
            if currentNum == -1:
                currentNum = 99
        elif line[0] == "R":
            currentNum = currentNum + 1
            if currentNum == 100:
                currentNum = 0
        if currentNum == 0:
            zeros = zeros + 1
print(zeros, "zeros found")