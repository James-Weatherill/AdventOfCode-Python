#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################################

numbersList = []

file = open("input.txt", "r+")
fileReadList = (str(file.readlines())).replace("'", "").replace("[", "").replace("]", "").replace("\\n", "").replace(" ", "").split(",")

for item in fileReadList:
    itemNums = "".join(val for val in item if val.isnumeric())
    itemNumsTrunc = itemNums[0] + itemNums[-1]
    numbersList.append(int(itemNumsTrunc))

print(sum(numbersList))

########################################################

finishTime = time()

print(f"The code took: {finishTime-startTime} seconds!")
