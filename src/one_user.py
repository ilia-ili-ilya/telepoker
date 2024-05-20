from src.card import Card
from src.combination import Combination


class OneUser:
    def __init__(self, count_of_players):
        self.count_of_players = count_of_players
        self.personal_cards = []
        self.community_cards = []

    def add_personal_cards(self, card1, card2):
        self.personal_cards.append(card1)
        self.personal_cards.append(card2)

    def add_card(self, card):
        self.community_cards.append(card)

    def find_probability(self):
        if len(self.personal_cards) > 2 or len(self.community_cards) > 5:
            return -1
        else:
            ans = 0
            for _ in range(5000):
                personal_cards = list(self.personal_cards)
                community_cards = list(self.community_cards)
                other_players_cards = []
                other_players_cards_in_one_list = []
                while len(personal_cards) < 2:
                    personal_cards.append(Card.random_card(personal_cards + community_cards))
                while len(community_cards) < 5:
                    community_cards.append(Card.random_card(personal_cards + community_cards))
                for i in range(1, self.count_of_players):
                    other_players_cards.append([])
                    while len(other_players_cards[-1]) < 2:
                        new_card = Card.random_card(personal_cards + community_cards + other_players_cards_in_one_list)
                        other_players_cards[-1].append(new_card)
                        other_players_cards_in_one_list.append(new_card)
                our_comb = Combination(personal_cards + community_cards).find_the_hand_val_for_7()
                others_combs = []
                for i in range(1, self.count_of_players):
                    others_combs.append(
                        Combination(other_players_cards[i - 1] + community_cards).find_the_hand_val_for_7())
                if our_comb > max(others_combs):
                    ans += 1
                elif our_comb == max(others_combs):
                    ans += 0.5
        return ans / 5000
