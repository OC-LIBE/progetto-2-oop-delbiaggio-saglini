from modules.card import Card
from modules.deck import Deck

class Hand:
    def __init__(self):
        self.carte:list[Card] = []

    def add(self,card):
        self.carte.append(card)
    def delete(self,card):
        self.carte.remove(card)