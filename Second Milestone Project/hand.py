"""
A class to represent a hand of cards
"""

class Hand:
    def __init__(self):
        """
        Initialize an empty hand
        """
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Add a card object to the hand object
        """
        if card._rank == 'Ace':
            self.aces+=1
        self.cards.append(card)
        self.value += card.get_value()

    def adjust_for_aces(self):
        """
        Adjust the value of the hand if there are aces in the hand and the hand value is over 21,
        evaluate them to 1 until the value is no longer over 21
        """
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

    def show_cards(self, hide_one = False, who = "player"):
        """
        Args:
          hide_one(bool): True hides last card, False shows all cards
          who (string): Displays who's hand it is
        Shows the cards in the hand with the functionality to print the name of the player and to hide the last card.
        """
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
        