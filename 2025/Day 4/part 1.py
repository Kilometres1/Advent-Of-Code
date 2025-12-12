import re
paper = []
adjacentPaper = 0
accesablePaper = 0


def cellCheck(cellX, cellY):
    #print(paper[cellY-1][cellX])
    if paper[cellY][cellX] == "@":
        return 1
    else:
        return 0


file = open("Day 4/realData.txt","r")
for line in file.read().split("\n"):
    paper.append(re.findall(".",line))
rowLen = len(line)
columnLen = len(paper)
j = 0
#print(paper)
for row in paper:
    
    for i in range(0,len(row)):
        adjacentPaper = 0
        
        if j > 0 and j < columnLen-1 and i > 0 and i < rowLen-1:#1
            #print("checking 1")
            adjacentPaper = adjacentPaper + cellCheck(i-1,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i-1,j)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j)
            adjacentPaper = adjacentPaper + cellCheck(i-1,j+1)
            adjacentPaper = adjacentPaper + cellCheck(i,j+1)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j+1)
        elif j == 0 and i > 0 and i < rowLen-1:#2
            #print("checking 2")
            adjacentPaper = adjacentPaper + cellCheck(i-1,j)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j)
            adjacentPaper = adjacentPaper + cellCheck(i-1,j+1)
            adjacentPaper = adjacentPaper + cellCheck(i,j+1)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j+1)
        elif j > 0 and j < columnLen-1 and i == rowLen-1:#3
            #print("checking 3")
            adjacentPaper = adjacentPaper + cellCheck(i-1,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i-1,j)
            adjacentPaper = adjacentPaper + cellCheck(i-1,j+1)
            adjacentPaper = adjacentPaper + cellCheck(i,j+1)
        elif j == columnLen-1 and i > 0 and i < rowLen-1:#4
            #print("checking 4")
            adjacentPaper = adjacentPaper + cellCheck(i-1,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i-1,j)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j)
        elif j > 0 and j < columnLen-1 and i == 0:#5
            #print("checking 5")
            adjacentPaper = adjacentPaper + cellCheck(i,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j-1)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j)
            adjacentPaper = adjacentPaper + cellCheck(i,j+1)
            adjacentPaper = adjacentPaper + cellCheck(i+1,j+1)

        #elif (j == 0 and i == 0) or (j == 0 and i == rowLen-1) or (j == columnLen-1 and i == 0) or (j == columnLen-1 and i == rowLen-1):
            #print("checking corners",cellCheck(i,j))
            #if cellCheck(i,j) == 1:
                #accesablePaper = accesablePaper + 1
        

        if adjacentPaper < 4 and cellCheck(i,j) == 1:
            #print("accesable!")
            accesablePaper = accesablePaper + 1 
    j = j + 1
print(accesablePaper)











