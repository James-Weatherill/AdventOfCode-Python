import os
from time import time

########################################

start_time = time()

########################################

def line_parser(line):
    if line[0] == "R":
        return int(line[1:])
    else:
        return -int(line[1:])

file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input1.txt")
# file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input2.txt")

with open(file_path, "r") as file:
    file_read = file.read().splitlines()

cur_num = 50

zero_hits = 0

for line in file_read:
    change = line_parser(line)
    new_num = cur_num + change

    # New num wraps positively
    if new_num >= 100:
        while new_num >= 100:
            new_num -= 100
            zero_hits += 1
    # New num wraps negatively
    elif new_num <= -1:
        if cur_num == 0:
            zero_hits -= 1
        if (change + cur_num) % 100 == 0:
            zero_hits += 1
        while new_num <= -1:
            new_num += 100
            zero_hits += 1
    # New num lands exactly on zero (change is negative)
    elif new_num == 0:
        zero_hits += 1

    cur_num = new_num

print(f"\nThe number of times we hit zero is: {zero_hits}\n")

########################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
