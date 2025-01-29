from modules.card import Card
from modules.deck import Deck

class Hand:
    def __init__(self):
        self.mano:list[Card] = []

    def add(self,card):
        self.mano.append(card)


        