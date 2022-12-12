class Range:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    @classmethod
    def fromString(cls, range: str) -> 'Range':
        # Expected format to be "start-stop", eg: 2-5
        range_values = range.split("-")
        return Range(int(range_values[0]), int(range_values[1]))
    
    def contains(self, value: int) -> bool:
        return self.start <= value <= self.stop

    def fullyContains(self, otherRange: 'Range') -> bool:
        return self.contains(otherRange.start) and \
                self.contains(otherRange.stop)
    
    def overlaps(self, otherRange: 'Range') -> bool:
        return self.contains(otherRange.start) or \
                self.contains(otherRange.stop) or \
                otherRange.fullyContains(self)
    
