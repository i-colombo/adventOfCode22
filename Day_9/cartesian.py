def move(point: tuple, movement: str) -> tuple:
    if movement == 'U':
        return (point[0], point[1] + 1)
    elif movement == 'D':
        return (point[0], point[1] - 1)
    elif movement == 'R':
        return (point[0] + 1, point[1])
    elif movement == 'L':
        return (point[0] - 1, point[1])

def moveCloserTo(source_point: tuple, target_point: tuple) -> tuple:
    vector_distance = vectorDistanceBetween(source_point, target_point)
    new_x = source_point[0] + distanceToReduce(vector_distance[0])
    new_y = source_point[1] + distanceToReduce(vector_distance[1])
    return (new_x, new_y)

def distanceToReduce(current_distance: int) -> int:
    if current_distance == 0:
        return 0
    elif current_distance < 0:
        return -1
    else:
        return 1

def vectorDistanceBetween(point: tuple, anotherPoint: tuple) -> tuple:
    return (anotherPoint[0] - point[0], anotherPoint[1] - point[1])

def areTouching(point: tuple, anotherPoint: tuple) -> bool:
    distance = scalarDistanceBetween(point, anotherPoint)
    return distance < 2 or (distance == 2 and not areInline(point, anotherPoint))

def areInline(point: tuple, anotherPoint: tuple) -> bool:
    return point[0] == anotherPoint[0] or point[1] == anotherPoint[1]

def scalarDistanceBetween(point: tuple, anotherPoint: tuple) -> int:
    return abs(point[0] - anotherPoint[0]) + abs(point[1] - anotherPoint[1])

