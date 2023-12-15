#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = str(file1.readlines()).replace("['", "").replace("']", "").replace("'", "").replace("\\n", "").replace(" ", "").split(",")
for string in fileReadList:
    colonIndex = string.find(":")
    fixedList.append(string[(colonIndex+1):])
for i in range(len(fixedList)):
    fixedList[i] = int(fixedList[i])

########################################

startNum = 0
endNum = fixedList[0]

counter = 0

while startNum <= 23414239:
    if startNum*endNum > fixedList[1]:
        counter += 1
    startNum += 1
    endNum -= 1

print(counter*2)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

