from modules.card import Card
from modules.deck import Deck
from modules.hand import Hand

class Player:
    def __init__(self):
        self.selected_cards = []
        self.hand = Hand()


    def pesca_carte(self,deck):
        card = deck.draw()
        self.hand.add(card)
    def select_card(self,card):
        self.selected_cards.append(card)
       #print(card)

    def remove_card(self,deck):
        for card in self.selected_cards:
            self.hand.delete(card)
            self.pesca_carte(deck)
        self.selected_cards = []
