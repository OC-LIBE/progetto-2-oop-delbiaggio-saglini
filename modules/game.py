from modules.card import Card
from modules.deck import Deck
from modules.player import Player
number_of_decks = 1

class Game:
    def __init__(self):
        self.player1 = Player()
        self.deck = Deck(number_of_decks)

    def game_start(self):
        self.deck.shuffle()
        for i in range(0,8):
            self.player1.pesca_carte(self.deck)