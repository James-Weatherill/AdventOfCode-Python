#! /opt/homebrew/bin/python3

from time import time

startTime = time()

########################################

fixedList = []
file1 = open("input.txt", "r")
file2 = open("testInput.txt", "r")
fileReadList = file1.readlines()
for i in range(len(fileReadList)):
    colonIndex = fileReadList[i].find(":")
    fixedList.append(fileReadList[i].replace("\n", "").replace(fileReadList[i][0:colonIndex+2], "").replace(" | ", "|").replace("  1", " 01").replace("  2", " 02").replace("  3", " 03").replace("  4", " 04").replace("  5", " 05").replace("  6", " 06").replace("  7", " 07").replace("  8", " 08").replace("  9", " 09").replace(" 1 ", "01 ").replace(" 2 ", "02 ").replace(" 3 ", "03 ").replace(" 4 ", "04 ").replace(" 5 ", "05 ").replace(" 6 ", "06 ").replace(" 7 ", "07 ").replace(" 8 ", "08 ").replace(" 9 ", "09 "))
for i in range(len(fixedList)):
    fixedList[i] = fixedList[i].split("|")
for i in range(len(fixedList)):
    for j in range(len(fixedList[i])):
        fixedList[i][j] = fixedList[i][j].split(" ")
for i in range(len(fixedList)):
    fixedList[i].append(i+1)

########################################

numberOfWinsPerCard = []
allScratchcards = []

for i in range(len(fixedList)):
    counter = 0
    for item in fixedList[i][1]:
        if item in fixedList[i][0]:
            counter += 1

    numberOfWinsPerCard.append(counter)

for i in range(1,len(numberOfWinsPerCard)+1):
    allScratchcards.append([i])

for i in range(len(allScratchcards)):
    if numberOfWinsPerCard[i] > 0:
        for j in range(1, numberOfWinsPerCard[i]+1):
            for k in range(len(allScratchcards[i])):
                allScratchcards[i+j].append(allScratchcards[i+j][0])


allScratchcards = sum(allScratchcards, [])

print(len(allScratchcards))

########################################

finishTime = time()

print(f"\nThe code took: {finishTime-startTime} seconds, to run")

