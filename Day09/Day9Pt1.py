#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = file1.readlines()
for item in fileReadList:
    fixedList.append(item.replace("\n", ""))
for i in range(len(fixedList)):
    fixedList[i] = fixedList[i].split(" ")
for i in range(len(fixedList)):
    for j in range(len(fixedList[i])):
        fixedList[i][j] = int(fixedList[i][j])
for i in range(len(fixedList)):
    fixedList[i] = [fixedList[i]]

########################################

def allNumsZero(inputList):
    allZero = True
    for i in range(len(inputList)):
        if inputList[i] != 0:
            allZero = False
            break
    if allZero:
        return True
    else:
        return False

def findNextSequence(inputList):
    tempList = []
    for i in range(len(inputList)-1):
        tempList.append(inputList[i+1] - inputList[i])
    return tempList

finalSum = 0

for i in range(len(fixedList)):

    while True:

        if allNumsZero(fixedList[i][-1]):
            break
        else:
            fixedList[i].append(findNextSequence(fixedList[i][-1]))

    fixedList[i] = fixedList[i][::-1]

for i in range(len(fixedList)):
    extrapolatedValue = 0
    for j in range(len(fixedList[i])):
        extrapolatedValue += fixedList[i][j][-1]
    finalSum += extrapolatedValue

print(finalSum)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

