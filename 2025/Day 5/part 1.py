import re
freshID = []#ids of fresh items
availableIDs = []#ids of all available items
finalIDs = []#the final fresh list
IDbreak = 0
total = 0

file = open("Day 5/realData.txt","r")
i = 0
for line in file.read().split("\n"):
    if IDbreak != 0:#looking at the IDs
        availableIDs.append(int(re.findall(".+",line,re.S)[0]))
    else:
        if line == "":#looking at the gap between them
            IDbreak = i
        else:#looking at the ranges
            ranges = line.split("-")
            freshID.append(ranges)
            
            
    i += 1


#print(freshID)
#print(availableIDs)


availableIDs.sort()
#finalIDs = availableIDs.copy()
freshID.sort()
#print(freshID)
#fixedFreshID = list(dict.fromkeys(freshID))#remove duplicates
for j in availableIDs:
    #print("looking at availble ID",j)
    for k in freshID:
        #print("looking at fresh range",k)
        if j >= int(k[0]) and j <= int(k[1]):
            #print("match!")
            finalIDs.append(k)
            total += 1
            break

#print(fixedFreshID)
#print(availableIDs)
#print(finalIDs)
print(total)