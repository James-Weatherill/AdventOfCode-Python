#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput1.txt", "r")
file3 = open("testInput2.txt", "r")
fileReadList = str(file1.readlines()).replace("['", "").replace("']", "").replace(" '\\n',", "").replace("\\n', '", ".").replace("\\n", "").replace("(", "").replace(")", "").split(".")
fixedList.append(list(fileReadList[0]))
for i in range(1, len(fileReadList)):
    fixedList.append(fileReadList[i].split(" = "))
for i in range(len(fixedList[0])):
    if fixedList[0][i] == "L":
        fixedList[0][i] = 0
    elif fixedList[0][i] == "R":
        fixedList[0][i] = 1
for i in range(1, len(fixedList)):
    fixedList[i][1] = fixedList[i][1].split(", ")

########################################

def indexFinder(nextString):
    for lst in fixedList:
        if lst[0] == nextString:
            return fixedList.index(lst)

numberOfSteps = 0
leftOrRightIndex = 0
currentIndex = 0
nextIndex = 0

currentIndex = indexFinder("AAA")

while fixedList[currentIndex][0] != "ZZZ":

    leftOrRight = fixedList[0][leftOrRightIndex]
    nextIndex = indexFinder(fixedList[currentIndex][1][leftOrRight])
    currentIndex = nextIndex

    numberOfSteps += 1
    leftOrRightIndex += 1

    if leftOrRightIndex == len(fixedList[0]):
        leftOrRightIndex = 0

print(numberOfSteps)

########################################

finishTime = time()

print(f"The code took: {finishTime-startTime} seconds, to run!")

