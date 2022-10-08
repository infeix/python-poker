from dataclasses import dataclass, field
from typing import Dict, List

class Cards:
    card_a:str = None
    card_b:str = None

    def __init__(self, cards):
        self.card_a = cards[0:2]
        self.card_b = cards[3:5]


@dataclass
class Ai:
    position: int = 0
    pot_size: int = 0
    bets_preflop: List[int] = field(default_factory=list)
    bets_flop: List[int] = field(default_factory=list)
    bets_turn: List[int] = field(default_factory=list)
    bets_river: List[int] = field(default_factory=list)
    bets_before: List[int] = field(default_factory=list)
    player_before: int = 0
    player_after: int = 0
    my_cards: List[str] = field(default_factory=list)

    def calc_value(cards):
