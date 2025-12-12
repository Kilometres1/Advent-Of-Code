import re
currentNum = 0
total = 0
file = open("Day 2/realData.txt","r")
for line in file.read().split(","):
    rangeVals = line.split("-")
    currentNum = int(rangeVals[0])
    finalNum = int(rangeVals[1])
    while True:
        if len(str(currentNum)) % 2 == 0:
            x = re.findall(".{1}",str(currentNum))
            y = 0
            z = 0
            firstHalf = 0
            secondHalf = 0
            for i in range(0,int(len(x)/2)):
                firstHalf = firstHalf + (int(x[i])*pow(10,y))
                y = y + 1
            for i in range(int(len(x)/2),int(len(x))):
                secondHalf = secondHalf + (int(x[i])*pow(10,z))
                z = z + 1
            if firstHalf == secondHalf:
                total = total + currentNum
        if currentNum == finalNum:
            break
        currentNum = currentNum + 1
print(total)