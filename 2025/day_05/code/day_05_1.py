import os
from time import time

####################################

start_time = time()

####################################

# Lambda function
is_fresh = lambda ID, rng: rng[0] <= ID <= rng[1]

file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input1.txt")
# file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input2.txt")

with open(file_path, "r") as file:
    ranges, IDs = file.read().split("\n\n")

# Fix ranges
ranges = ranges.split("\n")
ranges = [(int(rng.split("-")[0]), int(rng.split("-")[1])) for rng in ranges]

# Fix IDs
IDs = [int(ID) for ID in IDs.split("\n")[:-1]]

num_of_fresh = 0

for ID in IDs:
    for rng in ranges:
        if is_fresh(ID, rng):
            num_of_fresh += 1
            break

print(f"\nNumber of fresh ingredients: {num_of_fresh}\n")

####################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
