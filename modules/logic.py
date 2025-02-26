from modules.card import Card
from modules.deck import Deck

class Logics:
    def riconoscimento_mani(self,carte_mano):
        scala_carte = sorted(card.card_scores[1] for card in carte_mano)
        semi_carte =[card.suit for card in carte_mano]

        value_counts = {v: scala_carte.count(v) for v in set(scala_carte)}
        suit_counts = {s: semi_carte.count(s) for s in set(semi_carte)}

        is_flush = len(set(semi_carte)) == 1 and len(set(scala_carte)) == 5
        is_straight = len(set(scala_carte)) == 5 and scala_carte[4]-scala_carte[0] == 4
        is_royal = is_flush and scala_carte == [10,11,11,12,13]
        is_straightflush = is_flush and is_straight
        is_pair = 2 in value_counts.values()
        is_theeofakind = 3 in value_counts.values()
        is_fourofakind = 4 in value_counts.values()
        is_fullhouse = sorted(value_counts.values()) == [2,3]
        is_doublepair = list(value_counts.values()).count(2) == 2
        
        print(scala_carte)
        print(value_counts)
        print(semi_carte)
        print(suit_counts)
