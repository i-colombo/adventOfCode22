from range import Range

def testFromString():
    range = Range.fromString("1-5")
    assert range.start == 1
    assert range.stop == 5

def testContains():
    range = Range(1,6)
    assert range.contains(1)
    assert range.contains(4)
    assert range.contains(6)
    assert not range.contains(8)

def testFullyContains():
    assert Range(1,6).fullyContains(Range(2,6))
    assert not Range(1,6).fullyContains(Range(2,8))

def testOverlaps():
    assert Range(3,7).overlaps(Range(2,8))
    assert Range(2,8).overlaps(Range(3,7))
    assert Range(1,5).overlaps(Range(5,7))
    assert not Range(2,5).overlaps(Range(6,8))

testFromString()
testContains()
testFullyContains()
testOverlaps()


