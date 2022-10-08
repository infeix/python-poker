# Table.py

from dataclasses import dataclass, field
from typing import Dict, List
from Player import Player
from constants import *
from utils import *

#           [1000]  [1000]  [1000]
#          /´1000´´´´´´´``````````\
#         /                        \
# [1000] |                          | [1000]
#        |   Q+  T!  K?  4>  J?     |
# [   0] |1000                  1000| [1000]
#         \                        /
#          \_1000____1000____1000_/
#           [   0]  [   0]  [   0]
#
#                   Q! T?

@dataclass
class Table:
    places: Dict[int, Player] = field(default_factory=dict)
    dealer: int = 0
    pot: int = 0
    small_blind = 1
    big_blind = 2
    paint_all_players = 0
    cards: List[str] = field(default_factory=list)

    def __str__(self):
        empty_table = EMPTY_TABLE
        new_empty_table = empty_table
        # Player
        for place in self.places:
            position = PLAYER_POSITIONS[place]
            player = self.places[place]
            new_empty_table = new_empty_table[:position] + player.formated_pessession() + new_empty_table[position+4:]
        # Dealer
        position = DEALER_POSITIONS[self.dealer]
        new_empty_table = new_empty_table[:position] + '#' + new_empty_table[position+1:]
        # Bets
        for place in self.places:
            position = BET_POSITIONS[place]
            player = self.places[place]
            if player.current_bet > 0:
                new_empty_table = new_empty_table[:position] + player.formated_bet() + new_empty_table[position+4:]
        # Player Cards
        if self.paint_all_players == 1:
            for place in self.places:
                position = PLAYER_CARD_POSITIONS[place]
                player = self.places[place]
                if player:
                    new_empty_table = new_empty_table[:position] + player.cards() + new_empty_table[position+5:]
        else:
            position = PLAYER_CARD_POSITIONS[0]
            player = self.places[0]
            if player:
                new_empty_table = new_empty_table[:position] + player.cards() + new_empty_table[position+5:]
        # Table Cards
        for index in range(len(self.cards)):
                position = TABLE_CARD_POSITIONS[index]
                card = self.cards[index]
                if card:
                    new_empty_table = new_empty_table[:position] + card + new_empty_table[position+2:]
        else:
            position = PLAYER_CARD_POSITIONS[0]
            player = self.places[0]
            if player:
                new_empty_table = new_empty_table[:position] + player.cards() + new_empty_table[position+5:]
        # Pot
        position = POT_POSITION
        new_empty_table = new_empty_table[:position] + str(self.pot).rjust(6) + new_empty_table[position+6:]
        return new_empty_table

    def paint(self):
        clearConsole()
        print(str(self))

    def add_player(self, player: Player):
        for place in range(10):
            if not place in self.places:
                self.places[place] = player
                break

    def move_dealer(self, step: int = 1):
        self.dealer += step

    def add_to_pot(self, amount):
        self.pot += amount

    def win_the_pot(self):
        win = self.pot
        self.pot = 0
        return win

    def small_blind_place(self):
        return self.dealer + 1

    def big_blind_place(self):
        return self.dealer + 2

    def get_blinds(self):
        small_b_player = self.places[self.small_blind_place()]
        small_b_player.set_bet(self.small_blind, self)
        big_b_player = self.places[self.big_blind_place()]
        big_b_player.set_bet(self.big_blind, self)
