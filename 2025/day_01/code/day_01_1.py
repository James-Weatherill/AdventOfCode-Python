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

zeros_counter = 0

for line in file_read:
    cur_num = (cur_num + line_parser(line)) % 100

    if cur_num == 0:
        zeros_counter += 1

print(f"\nThe number of times we hit zero is: {zeros_counter}\n")

########################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
