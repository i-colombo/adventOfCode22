def visibilityMap(forest_map: list) -> list:
    visibility_map = []
    for i in range(len(forest_map)):
        visibility_map.insert(i, [])
        for j in range(len(forest_map[i])):
            visibility_map[i].insert(j, visibilityOf(forest_map, i, j))
    return visibility_map

def visibilityOf(forest_map: list, row: int, column: int) -> int:
    if row == 0 or row == len(forest_map) - 1:
        return 1
    if column == 0 or column == len(forest_map[row]) - 1:
        return 1

    if isVisibleFromUp(forest_map, row, column) or \
        isVisibleFromLeft(forest_map, row, column) or \
            isVisibleFromRight(forest_map, row, column) or \
                isVisibleFromDown(forest_map, row, column):
                    return 1
    return 0
    
def isVisibleFromUp(forest_map: list, row: int, column: int) -> bool:
    current_tree_height = forest_map[row][column]
    for i in reversed(range(row)):
        if forest_map[i][column] >= current_tree_height:
            return False
    return True

def isVisibleFromLeft(forest_map: list, row: int, column: int) -> bool:
    current_tree_height = forest_map[row][column]
    trees_to_compare = forest_map[row][:column]
    for tree in reversed(trees_to_compare):
        if tree >= current_tree_height:
            return False
    return True

def isVisibleFromRight(forest_map: list, row: int, column: int) -> bool:
    current_tree_height = forest_map[row][column]
    trees_to_compare = forest_map[row][column + 1:]
    for tree in trees_to_compare:
        if tree >= current_tree_height:
            return False
    return True

def isVisibleFromDown(forest_map: list, row: int, column: int) -> bool:
    current_tree_height = forest_map[row][column]
    for i in range(row + 1, len(forest_map)):
        if forest_map[i][column] >= current_tree_height:
            return False
    return True

def countMap(visibility_map: list) -> int:
    total = 0
    for row in visibility_map:
        for elem in row:
            total += elem
    return total

def printMap(map:list):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end=' ')
        print()


def scenicMap(forest_map: list) -> list:
    scenic_map = []
    for i in range(len(forest_map)):
        scenic_map.insert(i, [])
        for j in range(len(forest_map[i])):
            scenic_map[i].insert(j, scenicOf(forest_map, i, j))
    return scenic_map

def scenicOf(forest_map: list, row: int, column: int) -> int:
    if row == 0 or row == len(forest_map) - 1:
        return 0
    if column == 0 or column == len(forest_map[row]) - 1:
        return 0

    return scenicFromUp(forest_map, row, column) * scenicFromLeft(forest_map, row, column) * scenicFromRight(forest_map, row, column) * scenicFromDown(forest_map, row, column)

def scenicFromUp(forest_map: list, row: int, column: int) -> int:
    current_tree_height = forest_map[row][column]
    tree_view_count = 0
    for i in reversed(range(row)):
        tree_view_count += 1
        if forest_map[i][column] >= current_tree_height:
            break
    return tree_view_count

def scenicFromLeft(forest_map: list, row: int, column: int) -> int:
    current_tree_height = forest_map[row][column]
    trees_to_compare = forest_map[row][:column]
    tree_view_count = 0
    for tree in reversed(trees_to_compare):
        tree_view_count += 1
        if tree >= current_tree_height:
            break
    return tree_view_count

def scenicFromRight(forest_map: list, row: int, column: int) -> int:
    current_tree_height = forest_map[row][column]
    trees_to_compare = forest_map[row][column + 1:]
    tree_view_count = 0
    for tree in trees_to_compare:
        tree_view_count += 1
        if tree >= current_tree_height:
            break
    return tree_view_count

def scenicFromDown(forest_map: list, row: int, column: int) -> int:
    current_tree_height = forest_map[row][column]
    tree_view_count = 0
    for i in range(row + 1, len(forest_map)):
        tree_view_count += 1
        if forest_map[i][column] >= current_tree_height:
            break
    return tree_view_count

def maxMap(visibility_map: list) -> int:
    max_value = 0
    for row in visibility_map:
        max_row = max(row)
        if max_row > max_value:
            max_value = max_row
    return max_value
