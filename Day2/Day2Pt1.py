#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r+")
file2 = open("testInput.txt", "r+")
fileReadList = file1.readlines()
for lst in fileReadList:
    fixedList.append(lst.replace("\n", "").replace(" 1 ", " 01 ").replace(" 2 ", " 02 ").replace(" 3 ", " 03 ").replace(" 4 ", " 04 ").replace(" 5 ", " 05 ").replace(" 6 ", " 06 ").replace(" 7 ", " 07 ").replace(" 8 ", " 08 ").replace(" 9 ", " 09 ").replace("; ", ";"))
for i in range(len(fixedList)):
    fixedList[i] = fixedList[i].replace(f"Game {str(i+1)}: ", "").split(";")

########################################

counter = 0
powerList = []

for i in range(len(fixedList)):
    listLength = len(fixedList[i])
    red = True
    green = True
    blue = True
    for j in range(listLength):
        if "red" in (fixedList[i])[j]:
            redInd = ((fixedList[i])[j]).find("red")
            if 12 < int(((fixedList[i])[j])[redInd-3:redInd-1]):
                red = False
                break
            else:
                red = True

        if "green" in (fixedList[i])[j]:
            greenInd = ((fixedList[i])[j]).find("green")
            if 13 < int(((fixedList[i])[j])[greenInd-3:greenInd-1]):
                green = False
                break
            else:
                green = True

        if "blue" in (fixedList[i])[j]:
            blueInd = ((fixedList[i])[j]).find("blue")
            if 14 < int(((fixedList[i])[j])[blueInd-3:blueInd-1]): 
                blue = False
                break
            else:
                blue = True

    if red and green and blue:
        counter += (i+1)

print(counter)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds to run!")

