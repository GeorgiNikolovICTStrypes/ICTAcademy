"""
This is the main blackjack class
"""
from deck import Deck
from player import Player
import random
from hand import Hand
class BlackJack:

    def __init__(self, player):
        self.deck = Deck()
        self.player = player

    def play(self):
        self.deck = Deck()
        self.deck.shuffle_deck()
        
        while self.player._balance > 0:
            player_answer = input("Would u like to play a game of blackjack? [YES/NO]: ")
            while player_answer != 'YES' and  player_answer != 'NO':
                player_answer = input("Please enter a YES or NO ")
            if player_answer == 'YES':
                bet_amount = 0
                while True:
                    balance = player.get_balance()
                    try:
                        bet_amount = int(input("Please enter a bet! "))
                        
                        if bet_amount<balance:
                            break
                    except ValueError:
                        print(f"The bet must be an integer in the range [0,{balance}] ")

                player.bet(bet_amount)
                
                player_hand = Hand()
                dealer_hand = Hand()
                
                player_hand.add_card(self.deck.draw_a_card())
                dealer_hand.add_card(self.deck.draw_a_card())
                player_hand.add_card(self.deck.draw_a_card())
                dealer_hand.add_card(self.deck.draw_a_card())
                
                player_hand.show_cards()
                dealer_hand.show_cards(hide_one = True, who='dealer')
                while player_hand.value<21:
                    hit_or_stand = input("HIT OR STAND? [HIT/STAND] ")
                    if hit_or_stand == "STAND":
                        break
                    elif hit_or_stand == 'HIT':
                        player_hand.add_card(self.deck.draw_a_card())
                        player_hand.adjust_for_aces()
                        player_hand.show_cards()
                    else:
                        continue

                if player_hand.value<=21:
                    while dealer_hand.value<17:
                        dealer_hand.add_card(self.deck.draw_a_card())
                        dealer_hand.adjust_for_aces()
                        dealer_hand.show_cards(hide_one = True, who='dealer')
                    dealer_hand.show_cards(who = "Dealer")

                    if player_hand.value == 21 and dealer_hand.value == 21:
                        print("Its a push you gain your original bet")
                        player.add_funds(bet_amount)

                    if player_hand.value == 21:
                        print("Its a blackjack! You win 3x your bet")
                        player.add_funds(3*bet_amount)

                    if player_hand.value<21 and player_hand.value>dealer_hand.value:
                        print("You are closer to 21! You win 2x your bet")
                        player.add_funds(2*bet_amount)

                    if player_hand.value<21 and player_hand.value<dealer_hand.value:
                        print('The dealer is closer to 21! You lose your bet.')
                    
                else:
                    print("You bust! You lose your bet")
            else:
                break
                
        print(f"You walk out of the casino with {self.player._balance}$")

if __name__ == "__main__":        
    player = Player('gegata', 500)
    game = BlackJack(player)
    try:
        game.play()

    except KeyboardInterrupt:
        print("Game ended using keyboard interrupt")
