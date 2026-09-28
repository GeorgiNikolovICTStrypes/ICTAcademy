"""
A deck class for the black jack game
"""
from card import Card
import random
class Deck:

    def __init__(self):
        ranks = ['2','3','4','5','6','7','8','9','10','King', 'Queen', 'Jack', 'Ace']
        suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']

        self._deck = [Card(suit, rank) for rank in ranks for suit in suits]

    def __str__(self):
        res = "Cards in deck:\n"
        for card in self._deck:
            res += card.__str__()+'\n'
        return res
    
    def shuffle_deck(self):
        random.shuffle(self._deck)

    def get_deck_as_a_list(self):
        return self._deck

    def draw_a_card(self):
        return self._deck.pop(0)

    def add_cards(self, cards):
        self._deck = self._deck+cards
if __name__ == '__main__':
    deck = Deck()
    print(deck)
