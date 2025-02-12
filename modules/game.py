from modules.card import Card
from modules.deck import Deck
from modules.player import Player
number_of_decks = 1

class Game:
    def __init__(self):
        self.player1 = Player()

    def game_start(self):
        deck = Deck(number_of_decks)
        deck.shuffle()
        self.player1.pesca_carte(deck)