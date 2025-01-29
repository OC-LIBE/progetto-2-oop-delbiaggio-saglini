from modules.card import Card
from modules.deck import Deck

class Logics:
    def riconoscimento_mani(carte_mano):
        scala_carte = sorted(card.card_scores[1] for card in carte_mano)
        semi_carte =[card.suit for card in carte_mano]