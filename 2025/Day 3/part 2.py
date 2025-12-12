total = 0
file = open("Day 3/realData.txt","r")
for line in file.read().split('\n'):
    recentNum = [0,0]#the highest number found, and the position it was found in
    joltage = 0
    for i in range(0,12):#for 12 digits
        remainingDigits = 11 - i
        for j in range(recentNum[1],len(line)-remainingDigits):#from the most recent number onwards to the end-however many digits are left
            if int(line[j]) > recentNum[0]:
                recentNum[0] = int(line[j])
                recentNum[1] = j+1
        joltage = joltage + (recentNum[0]*pow(10,remainingDigits))
        recentNum[0] = 0
    total = total + joltage
print(total)