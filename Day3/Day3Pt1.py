#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = file2.readlines()
for lst in fileReadList:
    fixedList.append(lst.replace("\n", ""))

########################################

numsIndex = []
fixedNumsIndex = []

for i in range(len(fixedList)):
    for j in range(len(fixedList[i])):
        if (fixedList[i])[j].isnumeric():
            numsIndex.append([i,[j]])

for i in range(len(numsIndex)-1):
    if ((numsIndex[i])[1])[-1] == ((numsIndex[i+1])[1])[-1]-1:
        fixedNumsIndex.append((numsIndex[i])[0] )

#for i in range(len(fixedList)):
#    for j in range(len(fixedList[i])):
#        if (fixedList[i])[j].isnumeric() == False and (fixedList[i])[j] != ".":


print(fixedNumsIndex) 

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds to run!")

