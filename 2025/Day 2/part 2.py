import re
currentNum = 0
total = 0
prevNum = 0
file = open("Day 2/realData.txt","r")
for line in file.read().split(","):
    #print(line)
    rangeVals = line.split("-")
    currentNum = int(rangeVals[0])
    finalNum = int(rangeVals[1])
    #print(currentNum)
    #print(rangeVals[1])
    while True:
        
        for i in range(1,int(len(str(currentNum))/2)+1):
            regex = ".{" + str(i) +"}"
            x = re.findall(regex,str(currentNum))
            #print(x)
            identical = 0
            
            for j in range(0,len(x)):
                if x[0] == x[j]:
                    identical = identical + 1
            if len(x) == len(str(currentNum)) / i:
                if identical == len(str(currentNum))/i:
                    #print(currentNum)
                    if currentNum != prevNum:
                        prevNum = currentNum
                        total = total + currentNum
            
                #print(currentNum)


        if currentNum == finalNum:
            break
        
        currentNum = currentNum + 1
    #break
print(total)