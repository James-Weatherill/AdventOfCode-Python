import os
from time import time

####################################

start_time = time()

####################################

file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input1.txt")
# file_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input2.txt")

with open(file_path, "r") as file:
    ranges, _ = file.read().split("\n\n")

# Fix ranges
ranges = ranges.split("\n")
ranges = [(int(rng.split("-")[0]), int(rng.split("-")[1])) for rng in ranges]
ranges = sorted(ranges, key = lambda rng: rng[0])

while True:
    start_len = len(ranges)

    for rng_ID in range(len(ranges) - 1):
        if ranges[rng_ID] is None or ranges[rng_ID + 1] is None:
            continue
        if ranges[rng_ID][1] >= ranges[rng_ID + 1][0] - 1:
            ranges[rng_ID] = (ranges[rng_ID][0], max(ranges[rng_ID][1], ranges[rng_ID + 1][1]))
            ranges[rng_ID + 1] = None

    ranges = [rng for rng in ranges if rng is not None]
    end_len = len(ranges)

    if start_len == end_len:
        break

num_of_fresh = sum((rng[1] - rng[0] + 1) for rng in ranges)

print(f"\nNumber of fresh IDs: {num_of_fresh}\n")

####################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
