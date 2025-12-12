import re
freshID = []
availableIDs = []
finalIDs = []
IDbreak = 0
total = 0
file = open("Day 5/realData.txt","r")

for line in file.read().split("\n"):
    if IDbreak != 0:#looking at the IDs
        availableIDs.append(int(re.findall(".+",line,re.S)[0]))
    else:
        if line == "":
            IDbreak = 1
        else:
            ranges = line.split("-")
            freshID.append(ranges)  
availableIDs.sort()
freshID.sort()
for j in availableIDs:
    for k in freshID:
        if j >= int(k[0]) and j <= int(k[1]):
            finalIDs.append(k)
            total += 1
            break
print(total)