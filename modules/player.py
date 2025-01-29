from modules.card import Card
from modules.deck import Deck
from modules.hand import Hand

class Player:
    def __init__(self):
        self.selected_cards = []
        self.hand = Hand()


    def pesca_carte(self,deck):
        card = deck.draw()
        for i in range(1,8):
            self.hand.add(card)
        return self.hand


        