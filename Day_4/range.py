class Range:
    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    @classmethod
    def fromString(cls, range: str) -> 'Range':
        # Expected format to be "start-stop", eg: 2-5
        range_values = range.split("-")
        return Range(int(range_values[0]), int(range_values[1]))

    def fullyContains(self, otherRange: 'Range') -> bool:
        return \
            self.start <= otherRange.start <= self.stop and \
            self.start <= otherRange.stop <= self.stop
    
