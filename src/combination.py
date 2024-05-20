from src.card import Card
from src.hand_values import HandValues


class Combination:
    def __init__(self, cards):
        self.cards = cards

    def find_the_hand_val_for_5(self, selected_cards):
        selected_cards.sort()
        meanings = [selected_cards[i].get_meaning() for i in range(5)]
        suits = [selected_cards[i].get_suit() for i in range(5)]
        if (meanings == [meanings[0], meanings[0] + 1, meanings[0] + 2, meanings[0] + 3, meanings[0] + 4]) and (
                min(suits) == max(suits)):
            return (HandValues.straight_flush, selected_cards[4])
        elif meanings.count(meanings[2]) == 4:
            return (HandValues.four_of_a_kind, selected_cards[2])
        elif meanings.count(meanings[0] + meanings.count(meanings[4])) == 5:
            return (HandValues.full_house, selected_cards[2])
        elif min(suits) == max(suits):
            return (HandValues.flush, selected_cards[4])
        elif meanings == [meanings[0], meanings[0] + 1, meanings[0] + 2, meanings[0] + 3, meanings[0] + 4]:
            return (HandValues.straight, selected_cards[4])
        elif meanings.count(meanings[2]) == 3:
            return (HandValues.three_of_a_kind, selected_cards[2])
        elif len(set(meanings)) == 3:
            bst_card = Card(2, 1)
            for i in range(4):
                if meanings[i] == meanings[i + 1]:
                    bst_card = max(bst_card, selected_cards[i])
            return (HandValues.two_pairs, bst_card)
        elif len(set(meanings)) == 4:
            for i in range(4):
                if meanings[i] == meanings[i + 1]:
                    return (HandValues.pair, selected_cards[i])
        else:
            bst_card = Card(2, 1)
            for i in range(5):
                bst_card = max(bst_card, selected_cards[i])
            return (HandValues.high_card, bst_card)

    def find_the_hand_val_for_7(self):
        bst_hand_val = (HandValues.high_card, Card(0, 1))
        for i in range(7):
            for j in range(i):
                selected_cards = []
                for k in range(7):
                    if (k != i) and (k != j):
                        selected_cards.append(self.cards[k])
                bst_hand_val = max(bst_hand_val, self.find_the_hand_val_for_5(selected_cards))
        return bst_hand_val
