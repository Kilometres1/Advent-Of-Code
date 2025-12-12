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

    currentNum = currentNum + (int(line[1:])*direction)
    while currentNum > 99 or currentNum < 0:
        if currentNum > 99:
            currentNum = currentNum - 100
        elif currentNum < 0:
            currentNum = currentNum + 100
    if currentNum == 0:
        zeros = zeros + 1
        #print("FOUND 0")
    #print(line)
    print(currentNum)
print(zeros, "zeros found")