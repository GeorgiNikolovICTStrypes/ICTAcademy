"""
A simple card class
"""

class Card:

    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank

    def __str__(self):
        return (self._rank + ' of ' + self._suit)

    def get_value(self):
        if self._rank == 'Ace':
            return 11
        if self._rank == 'King' or self._rank == 'Queen' or self._rank == 'Jack':
            return 10
        
        return int(self._rank)


if __name__ == '__main__':
    test = Card('Diamonds', 'King')
    print(test.get_value())
    print(test)
