from collections import deque

def initializeStacks():
    return dict([
        (1, deque(['S', "Z", "P", "D", "L", "B", "F", "C"])),
        (2, deque(["N", "V", "G", "P", "H", "W", "B"])),
        (3, deque(["F", "W", "B", "J", "G"])),
        (4, deque(["G", "J", "N", "F", "L", "W", "C", "S"])),
        (5, deque(["W", "J", "L", "T", "P", "M", "S", "H"])),
        (6, deque(["B", "C", "W", "G", "F", "S"])),
        (7, deque(["H", "T", "P", "M", "Q", "B", "W"])),
        (8, deque(["F", "S", "W", "T"])),
        (9, deque(["N", "C", "R"]))
    ])

def initializeStacksForTest():
    return dict([
        (1, deque(['Z', "N"])),
        (2, deque(["M", "C", "D"])),
        (3, deque(["P"]))
    ])

def getNumberOfMovements(line: str) -> int:
    # eg: "move 2 from 5 to 9", returns 2
    return int(line.split(" ")[1])

def getStackFrom(line: str) -> int:
    # eg: "move 2 from 5 to 9", returns 5
    return int(line.split(" ")[3])

def getStackTo(line: str) -> int:
    # eg: "move 2 from 5 to 9", returns 9
    return int(line.split(" ")[5])

def moveFromTo(movements: int, stack_from: deque, stack_to: deque):
    for _ in range(movements):
        value = stack_from.pop()
        stack_to.append(value)

def moveKeepingOrderFromTo(movements: int, stack_from: deque, stack_to: deque):
    ordered_values = []
    for _ in range(movements):
        ordered_values.insert(0, stack_from.pop())
    stack_to.extend(ordered_values)
