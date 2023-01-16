from pathlib import Path
from graphs import *

def uphillConnectionWeightCalculator(current_height: int, connection_height: int) -> int:
    if connection_height - current_height <= 1:
        return 1
    else:
        return 0

path = Path(__file__).with_name('input.txt')
height_map = []
start_vertex = 0
finish_vertex = 0
lower_elevation_indexes = []
with path.open() as file:
    map_str = [line.strip() for line in file.readlines()]
    for i, map_line in enumerate(map_str):
        height_map.insert(i, [0] * len(map_line))
        for j, map_item in enumerate(map_line):
            if map_item == 'S':
                height_map[i][j] = ord("a") - 97
                start_vertex = i * len(map_line) + j
                lower_elevation_indexes.append(start_vertex)
            elif map_item == 'E':
                height_map[i][j] = ord("z") - 97
                finish_vertex = i * len(map_line) + j
            else:
                height_map[i][j] = ord(map_item) - 97
                if map_item == 'a':
                    lower_elevation_indexes.append(i * len(map_line) + j)

adjacency_map = adjacencyMapFromHeightMap(height_map, uphillConnectionWeightCalculator)
min_distances = minimumDistancesStartingFrom(adjacency_map, start_vertex)

print(f"Part 1 :: Minimum steps to top: {min_distances[finish_vertex]}" )
