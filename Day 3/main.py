from rucksackFunctions import *

with open("/Users/ignacio.colombo/desarrollo/adventscode/3rd/input.txt") as file:
    priorities_sum = 0
    for line in file:
        rucksack = line.strip()
        
        repeated_item_priority = itemPriority(repeatedItem(splitRucksack(rucksack)))
        
        priorities_sum += repeated_item_priority
    print(f"Part1 :: Total priority sum: {priorities_sum}")


