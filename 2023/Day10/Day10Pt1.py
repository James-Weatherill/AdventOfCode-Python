#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

file1 = open("input.txt", "r")
file2 = open("testInput1.txt", "r")
file3 = open("testInput2.txt", "r")
fixedList = file1.readlines()
for i in range(len(fixedList)):
    fixedList[i] = list(fixedList[i].replace("\n", ""))

########################################

def connectsToTile(tileLocation, surroundingCoord):

    symbolOnSurroundingTile = fixedList[surroundingCoord[0]][surroundingCoord[1]]
    symbolOnMainTile = fixedList[tileLocation[0]][tileLocation[1]]

    if surroundingCoord[0] == tileLocation[0]-1 and (symbolOnMainTile == "|" or symbolOnMainTile == "L" or symbolOnMainTile == "J" or symbolOnMainTile == "S") and (symbolOnSurroundingTile == "|" or symbolOnSurroundingTile == "7" or symbolOnSurroundingTile == "F"):
        return True

    elif surroundingCoord[0] == tileLocation[0]+1 and (symbolOnMainTile == "|" or symbolOnMainTile == "7" or symbolOnMainTile == "F" or symbolOnMainTile == "S") and (symbolOnSurroundingTile == "|" or symbolOnSurroundingTile == "L" or symbolOnSurroundingTile == "J"):
        return True

    elif surroundingCoord[1] == tileLocation[1]-1 and (symbolOnMainTile == "-" or symbolOnMainTile == "J" or symbolOnMainTile == "7" or symbolOnMainTile == "S") and (symbolOnSurroundingTile == "-" or symbolOnSurroundingTile == "L" or symbolOnSurroundingTile == "F"):
        return True

    elif surroundingCoord[1] == tileLocation[1]+1 and (symbolOnMainTile == "-" or symbolOnMainTile == "L" or symbolOnMainTile == "F" or symbolOnMainTile == "S") and (symbolOnSurroundingTile == "-" or symbolOnSurroundingTile == "J" or symbolOnSurroundingTile == "7"):
        return True
    
    else:
        return False

def findSurroundingTiles(inputTile):
    tempList = []
    row = inputTile[0]
    col = inputTile[1]
    numOfRow = len(fixedList)-1
    numOfCol = len(fixedList[0])-1

    if row != 0 and row != numOfRow and col != 0 and col != numOfCol:
        tempList = [[row-1, col], [row, col-1], [row, col+1], [row+1, col]]
    elif row == 0 and col == 0:
        tempList = [[row, col+1], [row+1, col]]
    elif row == 0 and col == numOfCol:
        tempList = [[row, col-1], [row+1, col]]
    elif row == 0:
        tempList = [[row, col-1], [row, col+1], [row+1, col]]
    elif row == numOfRow and col == 0:
        tempList = [[row-1, col], [row, col+1]]
    elif row == numOfRow and col == numOfCol:
        tempList = [[row-1, col], [row, col-1]]
    elif row == numOfRow:
        tempList = [[row-1, col], [row, col-1], [row, col+1]]
    elif col == 0:
        tempList = [[row-1, col], [row, col+1], [row+1, col]]
    elif col == numOfCol:
        tempList = [[row-1, col], [row, col-1], [row+1, col]]

    return tempList


# file1 SLocation
SLocation = [49, 96]
# file1 surroundingS
surroundingS = [[48, 96], [49, 95], [49, 97], [50, 96]]

# file2 SLocation
#SLocation = [1, 1]
# file2 surroundingS
#surroundingS = [[0, 1], [1, 0], [1, 2], [2, 1]]

# file3 SLocation
#SLocation = [2, 0]
# file3 surroundingS
#surroundingS = [[1, 0], [2, 1], [3, 0]]

allTilesInPath = [SLocation]

for lst in surroundingS:
    if connectsToTile(SLocation, lst):
        allTilesInPath.append(lst)
        break

while True:
    currentTile = allTilesInPath[-1]
    currentLength = len(allTilesInPath)

    surroundingTiles = findSurroundingTiles(currentTile)

    for lst in surroundingTiles:
        if connectsToTile(currentTile, lst) and lst not in allTilesInPath:
            allTilesInPath.append(lst)

    newLength = len(allTilesInPath)

    if currentLength == newLength:
        break

print(len(allTilesInPath)//2)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

