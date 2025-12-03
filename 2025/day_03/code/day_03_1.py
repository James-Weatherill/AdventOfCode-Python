import os
from time import time

########################################

start_time = time()

########################################

path_name = os.path.join(os.path.dirname(__file__), "..", "assets", "input1.txt")
# path_name = os.path.join(os.path.dirname(__file__), "..", "assets", "input2.txt")

with open(path_name, "r") as file:
    batteries = [line.strip() for line in file.readlines()]

num_check_order = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]

best_pair_sum = 0

for battery in batteries:
    cur_best = 0
    cur_found = False

    for num_check in num_check_order:
        for index_1 in range(len(battery) - 1):
            if battery[index_1] != num_check:
                continue
            for index_2 in range(index_1 + 1, len(battery)):
                current = int(battery[index_1] + battery[index_2])

                if current > cur_best:
                    cur_best = current
                    cur_found = True

            if cur_found:
                break
        if cur_found:
            best_pair_sum += cur_best
            break

print(f"\nThe sum of the best pair of batteries is: {best_pair_sum}\n")

########################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
