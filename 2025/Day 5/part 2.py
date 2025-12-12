freshID = []#ids of fresh items
interRange = [0,0]
total = 0
allIDs = []
file = open("Day 5/realData.txt","r")
for line in file.read().split("\n"):
    if line != "":
        ranges = line.split("-")
        interRange[0] = int(ranges[0])
        interRange[1] = int(ranges[1])
        freshID.append(interRange[:])
    else:
        break
freshID.sort(key=lambda x: x[0])
allIDs.append(freshID[0])
freshID.pop(0)
for j in freshID:
    i = allIDs[-1]
    if i == j:
        continue
    elif j[0] >= i[0] and j[1] <= i[1]:
        continue
    elif j[0] <= i[1] or j[0] == i[1]+1:
        i[1] = j[1]
    elif j[0] > i[1]+1:
        allIDs.append(j)
for i in allIDs:
    total += (i[1] - i[0])+1
print(total)
