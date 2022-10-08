# Deck.py

from dataclasses import dataclass, field
from typing import List
from constants import *
import random

@dataclass
class Deck:
    cards: List[str] = field(default_factory=list)
    def __init__(self):
        self.cards = CARDS.copy()
        random.shuffle(self.cards)

    def give_player_cards(self, table):
        for place in table.places:
            player = table.places[place]
            player.card_a = self.cards.pop()
        for place in table.places:
            player = table.places[place]
            player.card_b = self.cards.pop()

    def give_flop_cards(self, table):
        table.cards.append(self.cards.pop())
        table.cards.append(self.cards.pop())
        table.cards.append(self.cards.pop())

    def give_turn_card(self, table):
        table.cards.append(self.cards.pop())

    def give_river_card(self, table):
        table.cards.append(self.cards.pop())
