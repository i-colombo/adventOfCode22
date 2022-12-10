from rucksackFunctions import *

def testSplitRucksack():
    splitted = splitRucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    
    assert splitted[0] == "vJrwpWtwJgWr"
    assert splitted[1] == "hcsFMMfFFhFp"

def testRepeatedItemWithinRucksack():
    item = repeatedItemWithinRucksack(tuple(("vJrwpWtwJgWr", "hcsFMMfFFhFp")))
    
    assert item == "p"


def testItemPriority():
    assert itemPriority("p") == 16
    assert itemPriority("L") == 38

def testRepeatedItemCrossRucksacks():
    rucksack_group = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"]
    item = repeatedItemCrossRucksacks(rucksack_group)
    assert item == "r"

testSplitRucksack()
testRepeatedItemWithinRucksack()
testItemPriority()
testRepeatedItemCrossRucksacks()


