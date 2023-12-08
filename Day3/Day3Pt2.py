#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = file1.readlines()
for lst in fileReadList:
    fixedList.append(lst.replace("\n", ""))

########################################

symbolIndex = []
numIndex = []
fixedNums = []
surroundingStar = []
longNums = []

ans = 0


def findNum(item):

    if len(item[1])>1:
        num = int((fixedList[item[0]])[(item[1])[0]:(item[1])[-1]+1])

    else:
        num = int((fixedList[item[0]])[(item[1])[0]])

    return num


for i in range(len(fixedList)):

    for j in range(len(fixedList[i])):

        if (fixedList[i])[j] == "*":
            symbolIndex.append([i,[j]])


for lst in symbolIndex:

    row = lst[0]
    col = (lst[1])[0]
    surroundingStar.append([[row-1, [col-1]], [row, [col-1]], [row+1, [col-1]], [row-1, [col]], [row+1, [col]], [row-1, [col+1]], [row, [col+1]], [row+1, [col+1]]])


for i in range(len(fixedList)):

    for j in range(len(fixedList[i])):

        if (fixedList[i])[j].isnumeric():
            numIndex.append([i,[j]])


for i in range(len(numIndex)):

    curRow = (numIndex[i])[0]
    curNum = ((numIndex[i])[-1])[-1]

    nextNum = 0
    nextNextNum = 0
    nextnextnextnum = 0


    if i+1 < len(numIndex):
        nextNum = ((numIndex[i+1])[-1])[-1]

    if i+2 < len(numIndex):
        nextNextNum = ((numIndex[i+2])[-1])[-1]

    if i+3 < len(numIndex):
        nextnextnextnum = ((numIndex[i+3])[-1])[-1]


    if curNum == nextNum-1 and nextNum == nextNextNum-1 and nextNextNum == nextnextnextnum-1 and (fixedList[curRow])[curNum-1].isnumeric() == False:
        fixedNums.append([curRow, [curNum, nextnextnextnum]])

    elif curNum == nextNum-1 and nextNum == nextNextNum-1 and (fixedList[curRow])[curNum-1].isnumeric() == False:
        fixedNums.append([curRow, [curNum, nextNextNum]])

    elif curNum == nextNum-1 and (fixedList[curRow])[curNum-1].isnumeric() == False:
        fixedNums.append([curRow, [curNum, nextNum]])

    elif (fixedList[curRow])[curNum-1].isnumeric() == False:
        fixedNums.append([curRow, [curNum]])


for num in fixedNums:

    if len(num[1])>1:
        longNums.append([num[0], list(range((num[1])[0], (num[1])[1]+1))])

    else:
        longNums.append(num)
    


for allStarIndexes in surroundingStar:

    numberOfSurroundingNumbers = 0
    foundNums = []

    for singularStarIndex in allStarIndexes:

        for longNumber in longNums:

            numberRowIndex = longNumber[0]

            for numberColumnIndex in longNumber[1]:

                if [numberRowIndex, [numberColumnIndex]] == singularStarIndex and longNumber not in foundNums:
                    numberOfSurroundingNumbers += 1
                    foundNums.append(longNumber)
                    break

    if numberOfSurroundingNumbers == 2:
        ans += (findNum(foundNums[0])*findNum(foundNums[1]))

print(ans)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds to run!")

