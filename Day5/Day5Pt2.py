#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
seeds = fixedList[0][1:]
seed2Soil = fixedList[1][1:]
soil2Fertilizer = fixedList[2][1:]
fertilizer2Water = fixedList[3][1:]
water2Light = fixedList[4][1:]
light2Temperature = fixedList[5][1:]
temerature2Humidity = fixedList[6][1:]
humidity2Location = fixedList[7][1:]

exchangeList = [seeds, seed2Soil, soil2Fertilizer, fertilizer2Water, water2Light, light2Temperature, temerature2Humidity, humidity2Location]

file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = str(file1.readlines()).replace("\\n', '", ".").replace("..", "|").replace("['", "").replace("\\n']", "").replace(" map:", "").split("|")
for string in fileReadList:
    fixedList.append(string.split("."))
fixedList[0] = str(fixedList[0]).replace("['", "").replace("']", "").split(" ")
for i in range(1, len(fixedList)):
    for j in range(len(fixedList[i])):
        fixedList[i][j] = fixedList[i][j].split(" ")

for i in range(len(seeds)):
    seeds[i] = int(seeds[i])

for i in range(1, len(exchangeList)):
    for j in range(len(exchangeList[i])):
        for k in range(len(exchangeList[i][j])):
            exchangeList[i][j][k] = int(exchangeList[i][j][k])

########################################



########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!\n")

