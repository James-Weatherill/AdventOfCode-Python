import os
from time import time

########################################

start_time = time()

########################################

def inaccessible_surroundings(row, col, warehouse, warehouse_rows, warehouse_cols):
    inaccessible_count = 0

    check_points = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                    (row, col - 1)    ,                 (row, col + 1)    ,
                    (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]

    for row, col in check_points:
        if row < 0 or row >= warehouse_rows or col < 0 or col >= warehouse_cols:
            continue
        elif warehouse[row][col] == "@":
            inaccessible_count += 1

    return inaccessible_count

def str_replace_char(string, index, new_char):
    return string[:index] + new_char + string[index + 1:]

file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input1.txt")
# file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input2.txt")

with open(file_path, "r") as file:
    warehouse = file.read().splitlines()

warehouse_rows = len(warehouse)
warehouse_cols = len(warehouse[0])

accessible_rolls = 0

while True:
    roll_accessed = False

    for row_index in range(warehouse_rows):
        for col_index in range(warehouse_cols):
            C = warehouse[row_index][col_index]
            if C == "@":
                temp_surrounding_rolls = 0

                if inaccessible_surroundings(row_index, col_index, warehouse, warehouse_rows, warehouse_cols) < 4:
                    roll_accessed = True
                    warehouse[row_index] = str_replace_char(warehouse[row_index], col_index, ".")
                    accessible_rolls += 1

    if not roll_accessed:
        break

print(f"\nNumber of accessible rolls is: {accessible_rolls}\n")

########################################

finish_time = time()

print(f"The code took {finish_time - start_time} seconds to run\n")
