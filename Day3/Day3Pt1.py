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

counter = 0


def findNum(item):

    if len(item[1])>1:
        num = int((fixedList[item[0]])[(item[1])[0]:(item[1])[1]+1])
    else:
        num = int((fixedList[item[0]])[(item[1])[0]])

    return num


def surrounding(item):

    tempList = []
    finalTempList = []
    if len(item[1])>1:
        newCoords = [item[0], list(range((item[1])[0], (item[1])[1] + 1))]
    else:
        newCoords = item

    for element in newCoords[1]:
        tempList.append([newCoords[0], [element]])

    for lst in tempList:
        if lst[0] != 0 and lst[0] != len(fixedList)-1 and (lst[1])[0] != 0 and (lst[1])[-1] != len(fixedList[0])-1: # any space in the middle

            finalTempList.append([lst[0]-1, [(lst[1])[0]+1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]-1]])

            finalTempList.append([lst[0], [(lst[1])[0]+1]])
            finalTempList.append([lst[0], [(lst[1])[0]-1]])
            
            finalTempList.append([lst[0]+1, [(lst[1])[0]+1]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]-1]])

        elif lst[0] == 0 and (lst[1])[0] == 0: # the top left

            finalTempList.append([lst[0], [(lst[1])[0]+1]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]+1]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]]])

        elif lst[0] == 0 and (lst[1])[-1] == len(fixedList[0])-1: # the top right
            
            finalTempList.append([lst[0], [(lst[1])[0]-1]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]-1]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]]])

        elif lst[0] == 0: # any space at the top that isn't a corner

            finalTempList.append([lst[0], [(lst[1])[0]-1]])
            finalTempList.append([lst[0], [(lst[1])[0]+1]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]-1]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]+1]])

        elif lst[0] == len(fixedList)-1 and (lst[1])[0] == 0: # the bottom left

            finalTempList.append([lst[0], [(lst[1])[0]+1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]+1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]]])

        elif lst[0] == len(fixedList)-1 and (lst[1])[-1] == len(fixedList[0])-1: # the bottom right

            finalTempList.append([lst[0], [(lst[1])[0]-1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]-1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]]])

        elif lst[0] == len(fixedList)-1: # any space at the bottom that isn't a corner

            finalTempList.append([lst[0], [(lst[1])[0]-1]])
            finalTempList.append([lst[0], [(lst[1])[0]+1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]-1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]+1]])

        elif (lst[1])[0] == 0: # any space on the left that isn't a corner

            finalTempList.append([lst[0]+1, [(lst[1])[0]]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]+1]])
            finalTempList.append([lst[0], [(lst[1])[0]+1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]+1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]]])

        elif (lst[1])[-1] == len(fixedList[0])-1: # any space on the right that isn't a corner

            finalTempList.append([lst[0]+1, [(lst[1])[0]]])
            finalTempList.append([lst[0]+1, [(lst[1])[0]-1]])
            finalTempList.append([lst[0], [(lst[1])[0]-1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]-1]])
            finalTempList.append([lst[0]-1, [(lst[1])[0]]])

    return finalTempList


for i in range(len(fixedList)):

    for j in range(len(fixedList[i])):

        if (fixedList[i])[j].isnumeric() == False and (fixedList[i])[j] != ".":
            symbolIndex.append([i,[j]])


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


for lst in fixedNums:

    for item in symbolIndex:

        if item in surrounding(lst):
            counter += findNum(lst)
            break


print(counter)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds to run!")

