#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = str(file1.readlines()).replace("['", "").replace("']", "").replace("'", "").replace("\\n", "").replace(" 1", ".1").replace(" 2", ".2").replace(" 3", ".3").replace(" 4", ".4").replace(" 5", ".5").replace(" 6", ".6").replace(" 7", ".7").replace(" 8", ".8").replace(" 9", ".9").replace(" ", "").split(",")
for lst in fileReadList:
    fixedList.append((lst.split("."))[1:])
for i in range(len(fixedList)):
    for j in range(len(fixedList[i])):
        fixedList[i][j] = int(fixedList[i][j])

########################################

raceLengths = fixedList[0]
raceRecords = fixedList[1]

multipliedPossibilities = 1

for i in range(len(raceLengths)):
    counter = 0
    windLength = 0
    remainingTime = raceLengths[i]
    while remainingTime >= 0:
        if windLength*remainingTime > raceRecords[i]:
            counter += 1
        windLength += 1
        remainingTime -= 1
    
    if counter != 0:
        multipliedPossibilities *= counter
        
print(multipliedPossibilities)


########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")
