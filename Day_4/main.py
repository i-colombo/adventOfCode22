from range import Range
from pathlib import Path

path = Path(__file__).with_name('input.txt')
with path.open() as file:
    fully_contained_assignments = 0
    for line in file:
        pair_assignment = line.strip()
        ranges = pair_assignment.split(",")
        first_elf_range = Range.fromString(ranges[0])
        second_elf_range = Range.fromString(ranges[1])
        
        if first_elf_range.fullyContains(second_elf_range) or second_elf_range.fullyContains(first_elf_range):
            fully_contained_assignments += 1
    print(f"Part1 :: Total number of fully contained assignments: {fully_contained_assignments}")
