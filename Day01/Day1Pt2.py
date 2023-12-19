#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################################

numbersList = []
finalList = []

file1 = open("input.txt", "r+")
file2 = open("testInput.txt", "r+")
fileReadList = (str(file1.readlines())).replace("'", "").replace("[", "").replace("]", "").replace("\\n", "").replace(" ", "").split(",")

for string in fileReadList:
    oneInd1 = string.find("one")
    twoInd1 = string.find("two")
    threeInd1 = string.find("three")
    fourInd1 = string.find("four")
    fiveInd1 = string.find("five")
    sixInd1 = string.find("six")
    sevenInd1 = string.find("seven")
    eightInd1 = string.find("eight")
    nineInd1 = string.find("nine")
    
    oneInd2 = string.rfind("one")
    twoInd2 = string.rfind("two")
    threeInd2 = string.rfind("three")
    fourInd2 = string.rfind("four")
    fiveInd2 = string.rfind("five")
    sixInd2 = string.rfind("six")
    sevenInd2 = string.rfind("seven")
    eightInd2 = string.rfind("eight")
    nineInd2 = string.rfind("nine")
    
    indexList1 = [oneInd1, twoInd1, threeInd1, fourInd1, fiveInd1, sixInd1, sevenInd1, eightInd1, nineInd1]
    indexList2 = [oneInd2, twoInd2, threeInd2, fourInd2, fiveInd2, sixInd2, sevenInd2, eightInd2, nineInd2]

    newStr = string

    counter1 = 0

    for item1 in indexList1:
        counter1 += 1
        if item1 != -1:
            newStr = newStr[0:item1] + str(counter1) + newStr[item1+1:]

    counter2 = 0

    for item2 in indexList2:
        counter2 += 1 
        if item2 != -1:
            newStr = newStr[0:item2] + str(counter2) + newStr[item2+1:]

    finalList.append(newStr)

for item in finalList:
    itemNums = "".join(val for val in item if val.isnumeric())
    itemNumsTrunc = itemNums[0] + itemNums[-1]
    numbersList.append(int(itemNumsTrunc))

print(sum(numbersList))

########################################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds!")
