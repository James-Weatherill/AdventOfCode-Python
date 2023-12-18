#! /opt/homebrew/bin/python3

from time import time
from math import lcm

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput3.txt", "r")
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

counterList = []

indexOfAs = []

BXAPath = "BXA"
KBAPath = "KBA"
VTAPath = "VTA"
AAAPath = "AAA"
HMAPath = "HMA"
HLAPath = "HLA"

for i in range(1, len(fixedList)):
    if fixedList[i][0][2] == "A":
        indexOfAs.append(i)

counter = 0
leftOrRight = 0

while BXAPath[2] != "Z":
    BXAPath = fixedList[indexOfAs[0]][1][fixedList[0][leftOrRight]]
    for i in range(len(fixedList)):
        if fixedList[i][0] == BXAPath:
            indexOfAs[0] = i
    counter += 1
    leftOrRight += 1
    if leftOrRight == len(fixedList[0]):
        leftOrRight = 0
counterList.append(counter)

counter = 0
leftOrRight = 0

while KBAPath[2] != "Z":
    KBAPath = fixedList[indexOfAs[1]][1][fixedList[0][leftOrRight]]
    for i in range(len(fixedList)):
        if fixedList[i][0] == KBAPath:
            indexOfAs[1] = i
    counter += 1
    leftOrRight += 1
    if leftOrRight == len(fixedList[0]):
        leftOrRight = 0
counterList.append(counter)

counter = 0
leftOrRight = 0

while VTAPath[2] != "Z":
    VTAPath = fixedList[indexOfAs[2]][1][fixedList[0][leftOrRight]]
    for i in range(len(fixedList)):
        if fixedList[i][0] == VTAPath:
            indexOfAs[2] = i
    counter += 1
    leftOrRight += 1
    if leftOrRight == len(fixedList[0]):
        leftOrRight = 0
counterList.append(counter)

counter = 0
leftOrRight = 0

while AAAPath[2] != "Z":
    AAAPath = fixedList[indexOfAs[3]][1][fixedList[0][leftOrRight]]
    for i in range(len(fixedList)):
        if fixedList[i][0] == AAAPath:
            indexOfAs[3] = i
    counter += 1
    leftOrRight += 1
    if leftOrRight == len(fixedList[0]):
        leftOrRight = 0
counterList.append(counter)

counter = 0
leftOrRight = 0

while HMAPath[2] != "Z":
    HMAPath = fixedList[indexOfAs[4]][1][fixedList[0][leftOrRight]]
    for i in range(len(fixedList)):
        if fixedList[i][0] == HMAPath:
            indexOfAs[4] = i
    counter += 1
    leftOrRight += 1
    if leftOrRight == len(fixedList[0]):
        leftOrRight = 0
counterList.append(counter)

counter = 0
leftOrRight = 0

while HLAPath[2] != "Z":
    HLAPath = fixedList[indexOfAs[5]][1][fixedList[0][leftOrRight]]
    for i in range(len(fixedList)):
        if fixedList[i][0] == HLAPath:
            indexOfAs[5] = i
    counter += 1
    leftOrRight += 1
    if leftOrRight == len(fixedList[0]):
        leftOrRight = 0
counterList.append(counter)

print(lcm(counterList[0], counterList[1], counterList[2], counterList[3], counterList[4], counterList[5]))

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

