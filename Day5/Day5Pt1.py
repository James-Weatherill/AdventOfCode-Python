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
finalSeedNum = 0

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
    seeds.append(int(seedStr[i]))

for lst in exchangeLists:
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = int(lst[i][j])
    lst = sorted(lst, key=lambda x: x[1])

for i in range(len(exchangeLists)):
    for lst in exchangeLists[i]:
        rangeLists[i].append([lst[1], lst[1]+lst[2]-1])

for seedNum in seeds:

    found = False
    theRange = 1
    for lst in seedRanges:
        if between(seedNum, lst):
            theRange = lst
            found = True
            break
    if found:
        coordinates = seedRanges.index(theRange)
        soilNum = seed2Soil[coordinates][0] + (seedNum - seed2Soil[coordinates][1])
    else:
        soilNum = seedNum

    found = False
    theRange = 1
    for lst in soilRanges:
        if between(soilNum, lst):
            theRange = lst
            found = True
            break
    if found:
        coordinates = soilRanges.index(theRange)
        fertilizerNum = soil2Fertilizer[coordinates][0] + (soilNum - soil2Fertilizer[coordinates][1])
    else:
        fertilizerNum = soilNum

    found = False
    theRange = 1
    for lst in fertilizerRanges:
        if between(fertilizerNum, lst):
            theRange = lst
            found = True
            break
    if found:
        coordinates = fertilizerRanges.index(theRange)
        waterNum = fertilizer2Water[coordinates][0] + (fertilizerNum - fertilizer2Water[coordinates][1])
    else:
        waterNum = fertilizerNum

    found = False
    theRange = 1
    for lst in waterRanges:
        if between(waterNum, lst):
            theRange = lst
            found = True
            break
    if found:
        coordinates = waterRanges.index(theRange)
        lightNum = water2Light[coordinates][0] + (waterNum - water2Light[coordinates][1])
    else:
        lightNum = waterNum

    found = False
    theRange = 1
    for lst in lightRanges:
        if between(lightNum, lst):
            theRange = lst
            found = True
            break
    if found:
        coordinates = lightRanges.index(theRange)
        temperatureNum = light2Temperature[coordinates][0] + (lightNum - light2Temperature[coordinates][1])
    else:
        temperatureNum = lightNum

    found = False
    theRange = 1
    for lst in temperatureRanges:
        if between(temperatureNum, lst):
            theRange = lst
            found = True
            break
    if found:
        coordinates = temperatureRanges.index(theRange)
        humidityNum = temperature2Humidity[coordinates][0] + (temperatureNum - temperature2Humidity[coordinates][1])
    else:
        humidityNum = temperatureNum

    found = False
    theRange = 1
    for lst in humidityRanges:
        if between(humidityNum, lst):
            theRange = lst
            found = True
            break
    if found:
        coordinates = humidityRanges.index(theRange)
        locationNum = humidity2Location[coordinates][0] + (humidityNum - humidity2Location[coordinates][1])
    else:
        locationNum = humidityNum

    if lowestLocation > locationNum:
        lowestLocation = locationNum
        finalSeedNum = seedNum

print(f"\nThe lowest location number for any of the seeds is: {lowestLocation}")
print(f"The seed number that relates to this location is:   {finalSeedNum}")

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!\n")

