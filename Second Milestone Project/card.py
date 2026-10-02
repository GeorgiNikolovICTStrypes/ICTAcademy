"""
A simple card class
"""

class Card:

    def __init__(self, suit, rank):
        """
        Args:
          suit (string): The suit of the card (Aces, Hearts, Diamonds, Clubs)
          rank (string): The rank of the card (Ace, King, Queen, Jack or 10-2s)
        Create a card object
        """
        self._suit = suit
        self._rank = rank

    def __str__(self):
        """
        Prints a card object
        Output:
          (string) of sort rank + of + suit
        """
        return (self._rank + ' of ' + self._suit)

    def get_value(self):
        """
        Evaluates a card given using its rank
        Output:
          (int) the value of the card according to blackjack rules
        """
        if self._rank == 'Ace':
            return 11
        if self._rank == 'King' or self._rank == 'Queen' or self._rank == 'Jack':
            return 10
        
        return int(self._rank)


if __name__ == '__main__':
    test = Card('Diamonds', 'King')
    print(test.get_value())
    print(test)
