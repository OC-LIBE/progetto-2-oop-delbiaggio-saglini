from modules.card import Card
from modules.deck import Deck

class Points:
    def __init__(self):
        self.punteggio = 0
        self.punteggio_da_raggiungere = 400

    def riconoscimento_mani(self,carte_mano):
        scala_carte = sorted(card.card_scores[1] for card in carte_mano)
        semi_carte =[card.suit for card in carte_mano]

        value_counts = {v: scala_carte.count(v) for v in set(scala_carte)}

        is_flush = len(set(semi_carte)) == 1 and len(set(scala_carte)) == 5
        if is_flush:
            self.punteggio = 100
        is_straight = len(set(scala_carte)) == 5 and scala_carte[4]-scala_carte[0] == 4
        if is_straight:
            self.punteggio = 120
        is_royal = is_flush and scala_carte == [10,11,11,12,13]
        if is_royal:
            self.punteggio = 200
        is_straightflush = is_flush and is_straight
        if is_straightflush:
            self.punteggio = 250
        is_pair = 2 in value_counts.values()
        if is_pair:
            self.punteggio = 20
        is_theeofakind = 3 in value_counts.values()
        if is_theeofakind:
            self.punteggio = 50
        is_fourofakind = 4 in value_counts.values()
        if is_fourofakind:
            self.punteggio = 100
        is_fullhouse = sorted(value_counts.values()) == [2,3]
        if is_fullhouse:
            self.punteggio = 70
        is_doublepair = list(value_counts.values()).count(2) == 2
        if is_doublepair:
            self.punteggio = 40
        else:
            self.punteggio = 10
        print(value_counts)