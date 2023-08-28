#Blackjack python game

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self):
        self.cards = [Card(suit,rank) for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs'] for rank in range(1,14)]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)
        self.score += card.rank

class Dealer(Player):
    def __init__(self):
        super().__init__()
    
    def shown_card(self):
        return self.hand[0]

class BjGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start_game(self):
        self.player.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

    def hit(self):
        new_card = self.deck.deal()
        self.player.add_card(new_card)
        return new_card

    def check_bj(self, player):
        return player.score == 21 and len(player.hand) == 2
    
    def check_bust(self, player):
        return player.score > 21
    
    def compare(self):
        if self.check_bust(self.player):
            return "Dealer"
        elif self.check_bust(self.dealer):
            return "Player"
        elif self.player.score > self.dealer.score:
            return "Player"
        elif self.dealer.score > self.player.score:
            return "Dealer"
        else:
            return "Tie"

game = BjGame()
game.start_game()

print("Player's hand: ", [f'{card.rank} of {card.suit}' for card in game.player.hand])
print("Dealer's shown card: ", [f'{game.dealer.shown_card().rank} of {game.dealer.shown_card().suit}.', 'the other card is face down.'])

if game.check_bj(game.player):
    print("Player wins with a Blackjack!")
else:
    while True:
        decision = input("Would you like to hit or stand? ")
        if decision.lower() == "hit":
            new_card = game.deck.deal()
            game.player.add_card(new_card)
            print("Player was dealt:", f'{new_card.rank}')
            print ("Player's hand: ", [f'{card.rank} of {card.suit}' for card in game.player.hand])
            if game.check_bust(game.player):
                print("Player bust.")
                break
        elif decision.lower() =="stand":
            while game.dealer.score < 17:
                new_card = game.deck.deal()
                game.dealer.add_card(new_card)
            print("Dealer's hand: ", [f'{card.rank} of{card.suit}' for card in game.dealer.hand])
            winner = game.compare()
            print(f'{winner} wins this hand!')
            break
