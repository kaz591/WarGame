#video 86  de 2022 Complete Python Bootcamp From Zero to Hero in Python
#creacion del juego WAR
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {"Two": 2, 'Three' :3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace' :14}

class Card():
    """Class to create cards. i.e Seven of clubs"""
    def __init__(self,rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " +self.suit

class Deck :
    """Class to create the 52 card deck using the Card class too"""
    def __init__ (self) :
        self.all_cards = [ ]
        for suit in suits :
            for rank in ranks :
                # Create the Card Object
                created_card = Card( rank , suit )
                self.all_cards.append ( created_card )
    def shuffle(self):
        random.shuffle(self.all_cards )
    def deal_one(self):
        return self.all_cards.pop()

class Player():
    """Creates new players and their hands"""
    def __init__(self,name):
        self.name = name
        self.cards =[]
    def remove_one(self):
        return self.cards.pop(0)
    def add_cards(self, new_cards):
        if isinstance(new_cards,list):    #list of multiple cards
            self.cards.extend(new_cards)
        else:                             #for a single card
            self.cards.append(new_cards)
    def __str__(self):
        return f"Player {self.name} has {len(self.cards)} cards."

new_deck = Deck()
new_deck.shuffle()

player_one = Player("Santi")
player_two = Player("Dani")

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

print(player_one)
print(player_two)

game_on = True
round_num= 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.cards) == 0:
        print("Player one is out of cards, Player two wins this game!")
        game_on = False
        break
    if len(player_two.cards) == 0:
        print("Player two is out of cards, Player one wins this game!")
        game_on = False
        break
    #start a new round
    player_one_played = []
    player_one_played.append(player_one.remove_one())

    player_two_played = []
    player_two_played.append(player_two.remove_one())

    print(f"Player one played, {player_one_played[-1]}")
    print(f"Player two played, {player_two_played[-1]}")

    at_war = True
    while at_war:
        if player_one_played[-1].value > player_two_played[-1].value:
            player_one.add_cards(player_one_played)
            player_one.add_cards(player_two_played)
            at_war = False
            print("Player one earns the cards")
        elif player_two_played[-1].value > player_one_played[-1].value:
            player_two.add_cards(player_two_played)
            player_two.add_cards(player_one_played)
            print("Player two earns the cards")
            at_war = False
        else:
            print("WAR!")

            if len (player_one.cards) < 3:
                print("Player one unable to declare war")
                print("PLAYER two wins!")
                game_on= False
                break

            elif len (player_two.cards) < 3:
                print("Player TWO unable to declare war")
                print("PLAYER ONE WINS!")
                game_on= False
                break
            else:
                for num in range (3):
                    player_one_played.append(player_one.remove_one())
                    player_two_played.append(player_two.remove_one())
