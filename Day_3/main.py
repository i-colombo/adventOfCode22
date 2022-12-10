from rucksackFunctions import *
from pathlib import Path

path = Path(__file__).with_name('input.txt')
with path.open() as file:
    priorities_sum = 0
    for line in file:
        rucksack = line.strip()
        
        repeated_item_priority = itemPriority(repeatedItemWithinRucksack(splitRucksack(rucksack)))
        
        priorities_sum += repeated_item_priority
    print(f"Part1 :: Total priority sum (within rucksack): {priorities_sum}")

with path.open() as file:
    priorities_sum = 0
    rucksack_group = []
    for line in file:
        rucksack = line.strip()
        rucksack_group.append(rucksack)

        if len(rucksack_group) == 3:
            repeated_item_priority = itemPriority(repeatedItemCrossRucksacks(rucksack_group))
            priorities_sum += repeated_item_priority
            rucksack_group = []
            
    print(f"Part2 :: Total priority sum (cross rucksack): {priorities_sum}")
