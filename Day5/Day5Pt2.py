#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = str(file2.readlines()).replace("\\n', '", ".").replace("..", "|").replace("['", "").replace("\\n']", "").replace(" map:", "").split("|")
for string in fileReadList:
    fixedList.append(string.split("."))
fixedList[0] = str(fixedList[0]).replace("['", "").replace("']", "").split(" ")
for i in range(1, len(fixedList)):
    for j in range(len(fixedList[i])):
        fixedList[i][j] = fixedList[i][j].split(" ")

########################################

def between(item, rangeList):
    if item >= rangeList[0] and item <= rangeList[1]:
        return True
    else:
        return False

lowestLocation = 1_000_000_000_000

soilNum = 0
fertilizerNum = 0
waterNum = 0
lightNum = 0
temperatureNum = 0
humidityNum = 0
locationNum = 0

seedsWithInstructions = []
seeds = []

seedRanges = []
soilRanges = []
fertilizerRanges = []
waterRanges = []
lightRanges = []
temperatureRanges = []
humidityRanges = []

seedStr = fixedList[0][1:]
seed2Soil = fixedList[1][1:]
soil2Fertilizer = fixedList[2][1:]
fertilizer2Water = fixedList[3][1:]
water2Light = fixedList[4][1:]
light2Temperature = fixedList[5][1:]
temperature2Humidity = fixedList[6][1:]
humidity2Location = fixedList[7][1:]

exchangeLists = [seed2Soil, soil2Fertilizer, fertilizer2Water, water2Light, light2Temperature, temperature2Humidity, humidity2Location]
rangeLists = [seedRanges, soilRanges, fertilizerRanges, waterRanges, lightRanges, temperatureRanges, humidityRanges]

for i in range(len(seedStr)):
    seedsWithInstructions.append(int(seedStr[i]))

for lst in exchangeLists:
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = int(lst[i][j])
    lst = sorted(lst, key=lambda x: x[1])

for i in range(len(exchangeLists)):
    for lst in exchangeLists[i]:
        rangeLists[i].append([lst[1], lst[1]+lst[2]-1])



print("")
print(seedsWithInstructions)
for lst in exchangeLists:
    print("")
    for subList in lst:
        print(subList)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!")

