total = 0
file = open("Day 3/realData.txt","r")
for line in file.read().split('\n'):
    lineLen = len(line)
    highestTen = [0,0]
    highestDigit = [0,0]
    print(line)
    for j in range(0,len(line)):#picking tens
        currentNum = int(line[j])
        if currentNum > highestTen[0]:
            if j < len(line)-1:
                highestTen[0] = currentNum
                highestTen[1] = j
    for j in range(0,len(line)):#picking digits
        currentNum = int(line[j])    
        if currentNum > highestDigit[0]:
            if j > highestTen[1]:
                highestDigit[0] = currentNum
                highestDigit[1] = j
    total = total + int(str(highestTen[0])+str(highestDigit[0]))
print(total)