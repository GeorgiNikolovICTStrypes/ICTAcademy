"""
A player class for the blackjack project
"""
class Player:

    def __init__(self, name, balance):
        """
        Args:
          name (string): Player name
          balance (int): Player balance
        Create a player object instance with passed name and balance
        """
        self._name  = name
        self._balance = balance

    def bet(self, bet):
        """
        Args:
          bet (int): bet amount
        Place a bet thats within a users balance. If bet <= balance subtract that from balance else
        notify user
        """
        if bet<=self._balance:
            self._balance-=bet
            print("Remaining balance is {}$".format(self._balance))
            return 1
        else:
            print("Not enough funds!")
            return -1

    def add_funds(self, amount):
        """
        Args:
          amount (int): Amount of funds to add to balance
        Adds amount to balance
        """
        self._balance+=amount

    def get_balance(self):
        """
        Output:
          (int) balance of the player
        """
        return self._balance

    def get_name(self):
        """
        Output:
          (string) name of the player
        """
        return self._name
    
    def __str__(self):
        """
        Output:
         (string) in the format Player + name + has + balance + $
        """
        return ('Player ' + self._name + ' has ' +str(self._balance) + '$')


if __name__ == '__main__':
    player = Player('gegata', 10000)
    print(player)
    player.bet(100)
    player.bet(100001)
    player.add_funds(1000)
    print(player)
    