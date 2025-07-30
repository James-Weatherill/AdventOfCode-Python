import os
from time import time

start_time = time()

########################################

def process_input(input_path):
    with open(input_path, "r") as file:
        machines = [line.split("\n") for line in file.read().split("\n\n")]

    machines[-1] = machines[-1][:-1]

    for machine_no in range(len(machines)):
        A_colon_space_loc = machines[machine_no][0].index(": ")
        A_comma_space_loc = machines[machine_no][0].index(", ")

        B_colon_space_loc = machines[machine_no][1].index(": ")
        B_comma_space_loc = machines[machine_no][1].index(", ")

        PRIZE_colon_space_loc = machines[machine_no][2].index(": ")
        PRIZE_comma_space_loc = machines[machine_no][2].index(", ")

        A_X = int(machines[machine_no][0][A_colon_space_loc + 3:A_comma_space_loc])
        A_Y = int(machines[machine_no][0][A_comma_space_loc + 3:])

        B_X = int(machines[machine_no][1][B_colon_space_loc + 3:B_comma_space_loc])
        B_Y = int(machines[machine_no][1][B_comma_space_loc + 3:])

        PRIZE_X = int(machines[machine_no][2][PRIZE_colon_space_loc + 4:PRIZE_comma_space_loc])
        PRIZE_Y = int(machines[machine_no][2][PRIZE_comma_space_loc + 4:])

        machines[machine_no] = ((A_X, A_Y), (B_X, B_Y), (PRIZE_X, PRIZE_Y))

    return machines

def find_prizes_and_tokens(machines):
    prizes_no = 0
    tokens_no = 0

    for machine_no in range(len(machines)):
        equation_1 = (machines[machine_no][0][0], machines[machine_no][1][0], machines[machine_no][2][0])
        equation_2 = (machines[machine_no][0][1], machines[machine_no][1][1], machines[machine_no][2][1])

        multiplier_1 = equation_2[0]
        multiplier_2 = equation_1[0]

        equation_1 = (equation_1[0] * multiplier_1, equation_1[1] * multiplier_1, equation_1[2] * multiplier_1)
        equation_2 = (equation_2[0] * multiplier_2, equation_2[1] * multiplier_2, equation_2[2] * multiplier_2)

        B = (equation_1[2] - equation_2[2]) / (equation_1[1] - equation_2[1])
        A = (equation_1[2] - equation_1[1] * B) / equation_1[0]

        if B % 1 != 0 or A % 1 != 0:
            B = 0
            A = 0
        else:
            B = int(B)
            A = int(A)

            prizes_no += 1
            tokens_no += (A * 3) + B

    return prizes_no, tokens_no

# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test1.txt")
input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input.txt")

machines = process_input(input_path)

prizes_no, tokens_no = find_prizes_and_tokens(machines)

print(f"\nNumber of prizes: {prizes_no}, Total tokens: {tokens_no}\n")

########################################

finish_time = time()

print(f"The code took {finish_time - start_time} seconds to run\n")
