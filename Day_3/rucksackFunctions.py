def splitRucksack(rucksack: str) -> tuple:
    rucksack_len = len(rucksack)
    rucksack_half_len = int(rucksack_len / 2)
    first_compartment = rucksack[:rucksack_half_len]
    second_compartment = rucksack[rucksack_half_len:]

    return tuple((first_compartment, second_compartment))

def repeatedItemWithinRucksack(getRucksackTuple: tuple) -> str:
    first_compartment = getRucksackTuple[0]
    second_compartment = getRucksackTuple[1]

    for itemType in first_compartment:
        if itemType in second_compartment:
            return itemType

def itemPriority(item: str) -> int:
    return ord(item) - 96 if item.islower() else ord(item) - 38

def repeatedItemCrossRucksacks(rucksack_group: list) -> str:
    rucksack_items_setList = [set(rucksack) for rucksack in rucksack_group]
    repeated_items = set.intersection(*rucksack_items_setList)
    return repeated_items.pop()

