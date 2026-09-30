"""
A player class for the blackjack project
"""
class Player:

    def __init__(self, name, balance):
        self._name  = name
        self._balance = balance

    def bet(self, bet):
        if bet<=self._balance:
            self._balance-=bet
            print("Remaining balance is {}$".format(self._balance))
            return 1
        else:
            print("Not enough funds!")
            return -1

    def add_funds(self, amount):
        self._balance+=amount

    def get_balance(self):
        return self._balance

    def get_name(self):
        return self._name
    
    def __str__(self):
        return ('Player ' + self._name + ' has ' +str(self._balance) + '$')


if __name__ == '__main__':
    player = Player('gegata', 10000)
    print(player)
    player.bet(100)
    player.bet(100001)
    player.add_funds(1000)
    print(player)
    