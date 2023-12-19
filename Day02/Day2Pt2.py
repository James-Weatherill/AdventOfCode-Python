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

powerList = []

for lst in fixedList:
    red = 0
    green = 0
    blue = 0
    for string in lst:
        if "red" in string:
            redInd = string.find("red")
            if red < int(string[redInd-3:redInd-1]):
                red = int(string[redInd-3:redInd-1])

        if "green" in string:
            greenInd = string.find("green")
            if green < int(string[greenInd-3:greenInd-1]):
                green = int(string[greenInd-3:greenInd-1]) 

        if "blue" in string:
            blueInd = string.find("blue")
            if blue < int(string[blueInd-3:blueInd-1]):
                blue = int(string[blueInd-3:blueInd-1]) 

    power = red*green*blue
    powerList.append(power)

print(sum(powerList))

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds to run!")

