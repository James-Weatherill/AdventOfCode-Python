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

IDs_split = [(int(first), int(last)) for first, last in [ID.split("-") for ID in IDs]]

invalid_sum = 0

for ID_first, ID_last in IDs_split:
    for ID in range(ID_first, ID_last + 1):
        ID_str = str(ID)
        ID_str_len = len(ID_str)


        for current_chunk_length in range(ID_str_len // 2, 0, -1):
            if ID_str_len % current_chunk_length == 0:
                repeat_found = True

                chunk = ID_str[:current_chunk_length]

                for chunk_index in range(1, ID_str_len // current_chunk_length):
                    if ID_str[chunk_index * current_chunk_length : (chunk_index + 1) * current_chunk_length] != chunk:
                        repeat_found = False
                        break

                if repeat_found:
                    invalid_sum += ID
                    break

print(f"\nThe sum of all invalid IDs is: {invalid_sum}\n")

########################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
