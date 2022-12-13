from pathlib import Path
from stacks import *

def printResultedStacks(stacks: dict, msg: str):
    all_top_crates = ""
    for stack in stacks:
        top_crate = stacks[stack].pop()
        all_top_crates += top_crate
        print(f"{msg} The top crate of stack: {stack} is: {top_crate}")
    print(f"{msg} All top crates: {all_top_crates}")


path = Path(__file__).with_name('input.txt')
with path.open() as file:
    stacks = initializeStacks()
    for line in file:
        movements = getNumberOfMovements(line)
        stack_from = getStackFrom(line)
        stack_to = getStackTo(line)

        moveFromTo(movements, stacks[stack_from], stacks[stack_to])
    
    printResultedStacks(stacks, "Part 1 ::")

print ("===========================")
# Part 2
with path.open() as file:
    stacks = initializeStacks()
    for line in file:
        movements = getNumberOfMovements(line)
        stack_from = getStackFrom(line)
        stack_to = getStackTo(line)

        moveKeepingOrderFromTo(movements, stacks[stack_from], stacks[stack_to])
    printResultedStacks(stacks, "Part 2 ::")
