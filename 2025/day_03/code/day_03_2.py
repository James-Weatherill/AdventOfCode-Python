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

best_twelve_sum = 0

for battery in batteries:
    cur_found = False

    for num_check_1 in num_check_order:
        for index_1 in range(len(battery) - 11):
            if battery[index_1] == num_check_1:
                for num_check_2 in num_check_order:
                    for index_2 in range(index_1 + 1, len(battery) - 10):
                        if battery[index_2] == num_check_2:
                            for num_check_3 in num_check_order:
                                for index_3 in range(index_2 + 1, len(battery) - 9):
                                    if battery[index_3] == num_check_3:
                                        for num_check_4 in num_check_order:
                                            for index_4 in range(index_3 + 1, len(battery) - 8):
                                                if battery[index_4] == num_check_4:
                                                    for num_check_5 in num_check_order:
                                                        for index_5 in range(index_4 + 1, len(battery) - 7):
                                                            if battery[index_5] == num_check_5:
                                                                for num_check_6 in num_check_order:
                                                                    for index_6 in range(index_5 + 1, len(battery) - 6):
                                                                        if battery[index_6] == num_check_6:
                                                                            for num_check_7 in num_check_order:
                                                                                for index_7 in range(index_6 + 1, len(battery) - 5):
                                                                                    if battery[index_7] == num_check_7:
                                                                                        for num_check_8 in num_check_order:
                                                                                            for index_8 in range(index_7 + 1, len(battery) - 4):
                                                                                                if battery[index_8] == num_check_8:
                                                                                                    for num_check_9 in num_check_order:
                                                                                                        for index_9 in range(index_8 + 1, len(battery) - 3):
                                                                                                            if battery[index_9] == num_check_9:
                                                                                                                for num_check_10 in num_check_order:
                                                                                                                    for index_10 in range(index_9 + 1, len(battery) - 2):
                                                                                                                        if battery[index_10] == num_check_10:
                                                                                                                            cur_found = True
                                                                                                                            break
                                                                                                                    if cur_found:
                                                                                                                        break
                                                                                                                if cur_found:
                                                                                                                    break
                                                                                                        if cur_found:
                                                                                                            break
                                                                                                    if cur_found:
                                                                                                        break
                                                                                            if cur_found:
                                                                                                break
                                                                                        if cur_found:
                                                                                            break
                                                                                if cur_found:
                                                                                    break
                                                                            if cur_found:
                                                                                break
                                                                    if cur_found:
                                                                        break
                                                                if cur_found:
                                                                    break
                                                        if cur_found:
                                                            break
                                                    if cur_found:
                                                        break
                                            if cur_found:
                                                break
                                        if cur_found:
                                            break
                                if cur_found:
                                    break
                            if cur_found:
                                break
                    if cur_found:
                        break
                if cur_found:
                    break
        if cur_found:
            cur_found = False
            for num_check_11 in num_check_order:
                for index_11 in range(index_10 + 1, len(battery) - 1):
                    if battery[index_11] == num_check_11:
                        for num_check_12 in num_check_order:
                            for index_12 in range(index_11 + 1, len(battery)):
                                if battery[index_12] == num_check_12:
                                    cur_found = True
                                    break
                            if cur_found:
                                break
                    if cur_found:
                        break
                if cur_found:
                    break
            best_twelve = int(battery[index_1] + battery[index_2]  + battery[index_3]  + battery[index_4] +
                              battery[index_5] + battery[index_6]  + battery[index_7]  + battery[index_8] +
                              battery[index_9] + battery[index_10] + battery[index_11] + battery[index_12])
            best_twelve_sum += best_twelve
            break

print(f"\nThe sum of the best twelve batteries is: {best_twelve_sum}\n")

########################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
