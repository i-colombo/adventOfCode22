from pathlib import Path
from forestfunctions import *

path = Path(__file__).with_name('input.txt')
forest_map = []
with path.open() as file:
    for line in file:
        row = [int(tree_height) for tree_height in line.strip()]
        forest_map.append(row)

visibility_map = visibilityMap(forest_map)

total_visible_trees = countMap(visibility_map)

print(f"Part 1 :: Total visible trees: {total_visible_trees}")

######################  PART 2 ###################################

scenic_map = scenicMap(forest_map)

max_scenic_score = maxMap(scenic_map)

print(f"Part 2 :: Max scenic score: {max_scenic_score}")
