#! /opt/homebrew/bin/python3

from time import time
from copy import deepcopy as copy

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = file1.readlines()
for item in fileReadList:
    fixedList.append(list(item.replace("\n", "")))
nextFixedList = copy(fixedList)

########################################

allIndexes = []
allCombinations = []

ans = 0
counter = 0

spacing = 0
for i in range(len(fixedList)):
    allFullStops = True
    starList = []
    for j in range(len(fixedList[i])):
        if fixedList[i][j] != ".":
            allFullStops = False
            break
    if allFullStops:
        for thing in fixedList[i]:
            starList.append("*")
        nextFixedList.insert(i+spacing+1, starList)
        spacing += 1

finalFixedList = copy(nextFixedList)

spacing = 0
for j in range(len(nextFixedList[0])):
    allFullStops = True
    for i in range(len(nextFixedList)):
        if nextFixedList[i][j] != "." and nextFixedList[i][j] != "*":
            allFullStops = False
            break
    if allFullStops:
        for i in range(len(finalFixedList)):
            finalFixedList[i].insert(j+spacing+1, "*")
        spacing += 1

for i in range(len(finalFixedList)):
    for j in range(len(finalFixedList[i])):
        if finalFixedList[i][j] == "#":
            allIndexes.append([i, j])
            counter += 1
            finalFixedList[i][j] = counter

for i in range(len(allIndexes)-1):
    for j in range(i+1, len(allIndexes)):
        allCombinations.append([allIndexes[i], allIndexes[j]])

for lst in allCombinations:

    starCount = 0

    startRow = lst[0][0]
    startCol = lst[0][1]
    endRow = lst[1][0]
    endCol = lst[1][1]

    curRow = lst[0][0]
    curCol = lst[0][1]

    while curRow != endRow:
        if curRow < endRow:
            curRow += 1
        else:
            curRow -= 1
        if finalFixedList[curRow][curCol] == "*":
            starCount += 1

    while curCol != endCol:
        if curCol < endCol:
            curCol += 1
        else:
            curCol -= 1
        if finalFixedList[curRow][curCol] == "*":
            starCount += 1

    initialDistance = abs(startRow-endRow) + abs(startCol-endCol)
    extraSteps = starCount * 999_998
    totalDistance = initialDistance + extraSteps

    ans += totalDistance

print(ans)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

