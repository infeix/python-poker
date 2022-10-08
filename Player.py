# player.py

from dataclasses import dataclass

@dataclass
class Player:
    pessession: int = 0
    bet: int = 0
    current_bet: int = 0
    card_a: str = None
    card_b: str = None

    def cards(self):
        return (self.card_a or '  ') + " " + (self.card_b or '  ')

    def formated_pessession(self):
        return str(self.pessession).rjust(4)

    def formated_bet(self):
        return str(self.current_bet).rjust(4)

    def set_bet(self, amount: int, table):
        self.current_bet += amount
        self.bet += amount
        self.pessession -= amount
        table.add_to_pot(amount)

    def win_the_pot(self, table):
        self.pessession += table.win_the_pot()