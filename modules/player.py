from modules.card import Card
from modules.deck import Deck
from modules.hand import Hand

class Player:
    def __init__(self):
        self.selected_cards_positions = []
        self.hand = Hand()


    def pesca_carte(self,deck):
        for i in range(0,8):
            card = deck.draw()
            self.hand.add(card)
        return self.hand
    def select_card(self,posizione):
        self.selected_cards_positions.append(posizione)

    def remove_card(self):
        for i in range(len(self.selected_cards_positions)):
            self.hand.remove(i)
        self.selected_cards_positions = []
