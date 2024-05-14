from enum import Enum


class HandValues(Enum):
    High_card = 0
    Pair = 1
    Two_pairs = 2
    Three_of_a_kind = 3
    Straight = 4
    Flush = 5
    Full_house = 6
    Four_of_a_kind = 7
    Straight_flush = 8

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value
