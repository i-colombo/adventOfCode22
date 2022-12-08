from rucksackFunctions import *

def testSplitRucksack():
    splitted = splitRucksack("vJrwpWtwJgWrhcsFMMfFFhFp")
    
    assert splitted[0] == "vJrwpWtwJgWr"
    assert splitted[1] == "hcsFMMfFFhFp"

def testRepeatedItem():
    item = repeatedItem(tuple(("vJrwpWtwJgWr", "hcsFMMfFFhFp")))
    
    assert item == "p"


def testItemPriority():
    assert itemPriority("p") == 16
    assert itemPriority("L") == 38

testSplitRucksack()
testRepeatedItem()
testItemPriority()


