import os
from time import time

########################################

start_time = time()

########################################

path_name = os.path.join(os.path.dirname(__file__), "..", "assets", "input1.txt")
# path_name = os.path.join(os.path.dirname(__file__), "..", "assets", "input2.txt")

with open(path_name, "r") as file:
    IDs = file.read().split(",")
    IDs[-1] = IDs[-1].strip()

IDs_split = [[int(first), int(last)] for first, last in [ID.split("-") for ID in IDs]]

invalid_sum = 0

for ID_first, ID_last in IDs_split:
    for ID in range(ID_first, ID_last + 1):
        ID_str = str(ID)
        ID_str_len = len(ID_str)

        if ID_str_len % 2 == 0:
            if ID_str[: ID_str_len // 2] == ID_str[ID_str_len // 2 :]:
                invalid_sum += ID

print(f"\nThe sum of all invalid IDs is: {invalid_sum}\n")

########################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
