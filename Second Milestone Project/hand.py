"""
A class to represent a hand of cards
"""

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        if card._rank == 'Ace':
            self.aces+=1
        self.cards.append(card)
        self.value += card.get_value()

    def adjust_for_aces(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

    def show_cards(self, hide_one = False, who = "player"):
        message = f"Here is the {who}'s hand! "
        if not hide_one:
            message += f"The value of the hand is {self.value}"
            print(message)
            for card in self.cards:
                print(card)
            
        else:
            message += f"The value of the hand is {self.value-self.cards[-1].get_value()}"
            print(message)
            for card in self.cards[:-1]:
                print(card)
        