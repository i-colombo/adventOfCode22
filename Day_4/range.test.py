from range import Range

def testFromString():
    range = Range.fromString("1-5")
    assert range.start == 1
    assert range.stop == 5

def testFullyContains():
    assert Range(1,6).fullyContains(Range(2,6))


