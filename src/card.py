from random import randint


class Card:
    def __init__(self, meaning, suit):
        self.meaning = meaning
        self.suit = suit

    def __lt__(self, other):
        return self.meaning < other.meaning

    def __le__(self, other):
        return self.meaning <= other.meaning

    def __eq__(self, other):
        return self.meaning == other.meaning

    def __ne__(self, other):
        return self.meaning != other.meaning

    def __gt__(self, other):
        return self.meaning > other.meaning

    def __ge__(self, other):
        return self.meaning >= other.meaning

    def get_meaning(self):
        return self.meaning

    def get_suit(self):
        return self.suit

    @staticmethod
    def random_card(used_cards):
        new_card = Card(randint(0, 12), randint(0, 3))
        while new_card in used_cards:
            new_card = Card(randint(0, 12), randint(0, 3))
        return new_card
