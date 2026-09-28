"""
This is the main blackjack class
"""
from deck import Deck
from player import Player
import random

class BlackJack:

    def __init__(self, player):
        self.deck = Deck()
        self.player = player

    def play(self):
        used_cards = []
        unused_cards = self.deck
        
        while self.player._balance > 0:
            player_answer = input("Would u like to play a game of blackjack? [YES/NO]: ")
            while player_answer != 'YES' and  player_answer != 'NO':
                player_answer = input("Please enter a YES or NO ")
            if player_answer == 'YES':
                bet_amount = int(input(f"Place a bet. Your balance is {self.player._balance}. "))
                while bet_amount>self.player._balance:
                    bet_amount = int(input(f"Please place a valid bet. Your balance is {self.player._balance}."))
                
                if self.player.bet(bet_amount) == 1:
                    player_points = 0
                    dealer_points = 0
                    unused_cards.add_cards(used_cards)
                    unused_cards.shuffle_deck()
                    used_cards = []
                    print(unused_cards)
                    used_cards.append(unused_cards.draw_a_card())
                    player_points += used_cards[-1].get_value()
                    used_cards.append(unused_cards.draw_a_card())
                    dealer_points += used_cards[-1].get_value()
                    used_cards.append(unused_cards.draw_a_card())
                    player_points += used_cards[-1].get_value()
                    used_cards.append(unused_cards.draw_a_card())
                    dealer_points += used_cards[-1].get_value()
                    
                    print(unused_cards)
                    print(f"Your hand is: {used_cards[0].__str__()}, {used_cards[2].__str__()}. You have {player_points} points")
                    print(f"The dealers hand is: {used_cards[1].__str__()}, {used_cards[3].__str__()}. The dealer has {dealer_points} points")
                    while input("HIT OR STAND? ") == "HIT" and player_points<21:
                        card_added = unused_cards.draw_a_card()
                        used_cards.append(card_added)
                        player_points += card_added.get_value()
                        print(f"You draw {card_added.__str__()}. You have {player_points} points")

                    # Dealer Loop
                    while dealer_points<17:
                        card_added = unused_cards.draw_a_card()
                        used_cards.append(card_added)
                        dealer_points += card_added.get_value()
                        print(f"Dealer draws {card_added.__str__()}. The dealer has {dealer_points} points")

                    if player_points > 21:
                        print("BUST you went over 21. Better luck next time!")

                    elif dealer_points > 21:
                        print("The dealaer busted you win 2x your bet")
                        self.player.add_funds(2*bet_amount)

                    elif player_points == 21 and dealer_points == 21:
                        print("PUSH both you and the dealer got a blackjack! You get back your original bet ")
                        self.player.add_funds(bet_amount)

                    elif player_points == 21:
                        print("BLACKJACK you win 3x your bet!")
                        self.player.add_funds(3*bet_amount)

                    elif player_points < 21 and player_points>dealer_points:
                        print("You are closer to 21 than the dealer! You win 2x your bet")
                        self.player.add_funds(2*bet_amount)

                    else:
                        print("You lose! Better luck next time!")
        print(f"You walk out of the casino with {self.player._balance}$")
player = Player('gegata', 500)
game = BlackJack(player)
try:
    game.play()

except KeyboardInterrupt:
    print("Game ended using keyboard interrupt")
