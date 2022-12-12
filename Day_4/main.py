from assignmentFunctions import *
from pathlib import Path

path = Path(__file__).with_name('input.txt')
with path.open() as file:
    fully_contained_assignments = 0
    for line in file:
        pair_assignment = line.strip()
        
        if areFullyContainedRanges(splitAssignmentIntoRanges(pair_assignment)):
            fully_contained_assignments += 1
    print(f"Part1 :: Total number of fully contained assignments: {fully_contained_assignments}")
