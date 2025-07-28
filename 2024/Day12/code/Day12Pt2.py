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

def find_sector_area_sides(sectors):
    sector_area_sides = {}

    for sector in sectors:
        sector_corners = 0

        for coord in sectors[sector]:
            north_coord = (coord[0] - 1, coord[1])
            east_coord = (coord[0], coord[1] + 1)
            south_coord = (coord[0] + 1, coord[1])
            west_coord = (coord[0], coord[1] - 1)

            north_east_coord = (coord[0] - 1, coord[1] + 1)
            south_east_coord = (coord[0] + 1, coord[1] + 1)
            south_west_coord = (coord[0] + 1, coord[1] - 1)
            north_west_coord = (coord[0] - 1, coord[1] - 1)

            # External corners
            if north_coord not in sectors[sector] and east_coord not in sectors[sector]:
                sector_corners += 1
            if east_coord not in sectors[sector] and south_coord not in sectors[sector]:
                sector_corners += 1
            if south_coord not in sectors[sector] and west_coord not in sectors[sector]:
                sector_corners += 1
            if west_coord not in sectors[sector] and north_coord not in sectors[sector]:
                sector_corners += 1

            # Internal corners
            if north_coord in sectors[sector] and east_coord in sectors[sector] and north_east_coord not in sectors[sector]:
                sector_corners += 1
            if east_coord in sectors[sector] and south_coord in sectors[sector] and south_east_coord not in sectors[sector]:
                sector_corners += 1
            if south_coord in sectors[sector] and west_coord in sectors[sector] and south_west_coord not in sectors[sector]:
                sector_corners += 1
            if west_coord in sectors[sector] and north_coord in sectors[sector] and north_west_coord not in sectors[sector]:
                sector_corners += 1

        sector_area_sides[sector] = (len(sectors[sector]), sector_corners)

    return sector_area_sides

# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test1.txt")
# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test2.txt")
# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test3.txt")
# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test4.txt")
# input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "test5.txt")
input_path = os.path.join(os.path.dirname(__file__), "..", "assets", "input.txt")

input_file = open(input_path, "r")
input_file_lines = [line.strip() for line in input_file]
input_file.close()

region_coords = find_region_coords(input_file_lines)

sectors = find_sectors(region_coords)

sector_area_sides = find_sector_area_sides(sectors)

total_price = 0
for sector, (area, sides) in sector_area_sides.items():
    total_price += area * sides

print(f"\nThe total price is: {total_price}\n")
        
########################################

finish_time = time()

print(f"The code took: {finish_time - start_time} seconds to run\n")
