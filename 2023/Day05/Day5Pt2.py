#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = str(file1.readlines()).replace("\\n', '", ".").replace("..", "|").replace("['", "").replace("\\n']", "").replace(" map:", "").split("|")
for string in fileReadList:
    fixedList.append(string.split("."))
fixedList[0] = str(fixedList[0]).replace("['", "").replace("']", "").split(" ")
for i in range(1, len(fixedList)):
    for j in range(len(fixedList[i])):
        fixedList[i][j] = fixedList[i][j].split(" ")

########################################

def inRange(inputVal, testRange):
    if inputVal >= testRange[0] and inputVal <= testRange[1]:
        return True
    else:
        return False

seed2SoilRanges = []
soil2FertilizerRanges = []
fertilizer2WaterRanges = []
water2LightRanges = []
light2TemperatureRanges = []
temerature2HumidityRanges = []
humidity2LocationRanges = []
seedRanges = []

seedNum = 0
soilNum = 0
fertilizerNum = 0
waterNum = 0
lightNum = 0
temeratureNum = 0
humidityNum = 0
locationNum = 0
lowestLocation = 0
counter = -1

seedsTemp = fixedList[0][1:]
seeds = [int(x) for x in seedsTemp]
seed2Soil = fixedList[1][1:]
soil2Fertilizer = fixedList[2][1:]
fertilizer2Water = fixedList[3][1:]
water2Light = fixedList[4][1:]
light2Temperature = fixedList[5][1:]
temerature2Humidity = fixedList[6][1:]
humidity2Location = fixedList[7][1:]

exchangeLists = [humidity2Location, temerature2Humidity, light2Temperature, water2Light, fertilizer2Water, soil2Fertilizer, seed2Soil]
rangeLists = [humidity2LocationRanges, temerature2HumidityRanges, light2TemperatureRanges, water2LightRanges, fertilizer2WaterRanges, soil2FertilizerRanges, seed2SoilRanges, seedRanges]

for i in range(len(exchangeLists)):
    for j in range(len(exchangeLists[i])):
        for k in range(len(exchangeLists[i][j])):
            exchangeLists[i][j][k] = int(exchangeLists[i][j][k])

for i in range(0, len(seeds), 2):
    seedRanges.append([seeds[i], seeds[i] + seeds[i+1] - 1])

for i in range(len(exchangeLists)):
    for j in range(len(exchangeLists[i])):
        rangeLists[i].append([exchangeLists[i][j][0], exchangeLists[i][j][0] + exchangeLists[i][j][2] - 1])

while lowestLocation == 0:

    counter += 1
    locationNum = counter

    found = False
    rangeIndex = 0
    for lst in humidity2LocationRanges:
        if inRange(locationNum, lst):
            found = True
            rangeIndex = humidity2LocationRanges.index(lst)
            break
    if found:
        humidityNum = humidity2Location[rangeIndex][1] + (locationNum - humidity2Location[rangeIndex][0])
    else:
        humidityNum = locationNum

    found = False
    rangeIndex = 0
    for lst in temerature2HumidityRanges:
        if inRange(humidityNum, lst):
            found = True
            rangeIndex = temerature2HumidityRanges.index(lst)
            break
    if found:
        temeratureNum = temerature2Humidity[rangeIndex][1] + (humidityNum - temerature2Humidity[rangeIndex][0])
    else:
        temeratureNum = humidityNum

    found = False
    rangeIndex = 0
    for lst in light2TemperatureRanges:
        if inRange(temeratureNum, lst):
            found = True
            rangeIndex = light2TemperatureRanges.index(lst)
            break
    if found:
        lightNum = light2Temperature[rangeIndex][1] + (temeratureNum - light2Temperature[rangeIndex][0])
    else:
        lightNum = temeratureNum

    found = False
    rangeIndex = 0
    for lst in water2LightRanges:
        if inRange(lightNum, lst):
            found = True
            rangeIndex = water2LightRanges.index(lst)
            break
    if found:
        waterNum = water2Light[rangeIndex][1] + (lightNum - water2Light[rangeIndex][0])
    else:
        waterNum = lightNum

    found = False
    rangeIndex = 0
    for lst in fertilizer2WaterRanges:
        if inRange(waterNum, lst):
            found = True
            rangeIndex = fertilizer2WaterRanges.index(lst)
            break
    if found:
        fertilizerNum = fertilizer2Water[rangeIndex][1] + (waterNum - fertilizer2Water[rangeIndex][0])
    else:
        fertilizerNum = waterNum

    found = False
    rangeIndex = 0
    for lst in soil2FertilizerRanges:
        if inRange(fertilizerNum, lst):
            found = True
            rangeIndex = soil2FertilizerRanges.index(lst)
            break
    if found:
        soilNum = soil2Fertilizer[rangeIndex][1] + (fertilizerNum - soil2Fertilizer[rangeIndex][0])
    else:
        soilNum = fertilizerNum

    found = False
    rangeIndex = 0
    for lst in seed2SoilRanges:
        if inRange(soilNum, lst):
            found = True
            rangeIndex = seed2SoilRanges.index(lst)
            break
    if found:
        seedNum = seed2Soil[rangeIndex][1] + (soilNum - seed2Soil[rangeIndex][0])
    else:
        seedNum = soilNum

    for ranges in seedRanges:
        if inRange(seedNum, ranges):
            lowestLocation = counter

print(lowestLocation)

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run!\n")

