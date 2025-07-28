import os
from time import time

start_time = time()

########################################

def find_region_coords(input_file_lines):
    region_coords = {}
    region_names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in region_names:
        region_coords[char] = set()

    for row in range(len(input_file_lines)):
        for col in range(len(input_file_lines[row])):
            region_coords[input_file_lines[row][col]].add((row, col))

    return region_coords

def find_sectors(region_coords):
    sectors = {}

    for region in region_coords:
        sector_number = 0

        while len(region_coords[region]) > 0:
            sectors[(region, sector_number)] = set()
            intermediate_coords = []

            intermediate_coords.append(region_coords[region].pop())

            while len(intermediate_coords) > 0:
                current_coord = intermediate_coords[0]

                north_coord = (current_coord[0] - 1, current_coord[1])
                east_coord = (current_coord[0], current_coord[1] + 1)
                south_coord = (current_coord[0] + 1, current_coord[1])
                west_coord = (current_coord[0], current_coord[1] - 1)

                if north_coord in region_coords[region]:
                    intermediate_coords.append(north_coord)
                    region_coords[region].remove(north_coord)

                if east_coord in region_coords[region]:
                    intermediate_coords.append(east_coord)
                    region_coords[region].remove(east_coord)

                if south_coord in region_coords[region]:
                    intermediate_coords.append(south_coord)
                    region_coords[region].remove(south_coord)

                if west_coord in region_coords[region]:
                    intermediate_coords.append(west_coord)
                    region_coords[region].remove(west_coord)

                sectors[(region, sector_number)].add(intermediate_coords.pop(0))

            sector_number += 1

    return sectors

def find_sector_area_perimeter(sectors):
    sector_areas_perimeters = {}

    for sector in sectors:
        max_perimeter = len(sectors[sector]) * 4

        for coord in sectors[sector]:
            if (coord[0] - 1, coord[1]) in sectors[sector]:
                max_perimeter -= 1
            if (coord[0], coord[1] + 1) in sectors[sector]:
                max_perimeter -= 1
            if (coord[0] + 1, coord[1]) in sectors[sector]:
                max_perimeter -= 1
            if (coord[0], coord[1] - 1) in sectors[sector]:
                max_perimeter -= 1

        sector_areas_perimeters[sector] = (len(sectors[sector]), max_perimeter)

    return sector_areas_perimeters

# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test1.txt")
# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test2.txt")
# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test3.txt")
input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input.txt")

input_file = open(input_path, "r")
input_file_lines = [line.strip() for line in input_file]
input_file.close()

region_coords = find_region_coords(input_file_lines)

sectors = find_sectors(region_coords)

sector_areas_perimeters = find_sector_area_perimeter(sectors)

price = 0
for sector in sector_areas_perimeters:
    price += sector_areas_perimeters[sector][0] * sector_areas_perimeters[sector][1]

print(f"\nThe price of the sectors is: {price}\n")

########################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
