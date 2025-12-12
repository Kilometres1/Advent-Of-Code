import re
freshID = []#ids of fresh items
availableIDs = []#ids of all available items
finalIDs = []#the final fresh list
IDbreak = 0
total = 0
allIDs = []
allIDs.append(0)
file = open("Day 5/realData.txt","r")
for line in file.read().split("\n"):
    if line == "":#looking at the gap between them
        break
    else:#looking at the ranges
        ranges = line.split("-")
        freshID.append(ranges)
n = 0
for i in freshID:
    print(n)
    #print("freshID:",i)
    for j in range(int(i[0]),int(i[1])+1):
        #print(j)
        allIDs.sort()
        for k in allIDs:
            #print("checking",k)
            if j == k:
                break
            elif k == allIDs[-1]:
                allIDs.append(j)
                #print("not found, adding",j)

        
    

    allIDs = list(dict.fromkeys(allIDs))#remove duplicates
    n += 1
#print(allIDs)
print(len(allIDs)-1)
#print(freshID)
#print(availableIDs)