from enum import Enum

# class syntax
class ExpectedResultType(Enum):
    WIN = 'X'
    DRAW = 'Y'
    LOSE = 'Z'

    @staticmethod
    def from_value(value):
        if value in ('X'):
            return ExpectedResultType.WIN
        elif value in ('Y'):
            return ExpectedResultType.DRAW
        else:
            return ExpectedResultType.LOSE
