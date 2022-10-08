from Table import Table
from Player import Player
from Deck import Deck

t = Table()

hannes = Player(1000)
t.add_player(hannes)
for _ in range(9):
    t.add_player(Player(1000))
t.move_dealer()
t.get_blinds()

hannes.set_bet(50,t)


#                 Q! T?   Q! T?   Q! T?
#                 [1000]  [1000]  [1000]
#                /´1000´´´´´´´``````````\
#               /                        \
# Q! T? [1000] |                          | [1000] Q! T?
#              |   Q+  T!  K?  4>  J?     |
# Q! T? [   0] |1000                  1000| [1000] Q! T?
#               \                        /
#                \_1000____1000____1000_/
#                 [   0]  [   0]  [   0]
#                 Q! T?           Q! T?
#                         Q! T?

d = Deck()

d.give_player_cards(t)

d.give_flop_cards(t)

d.give_turn_card(t)

d.give_river_card(t)

t.paint()

# store Players Situation for KI decision
# Was sind meine Karten?
# Bin ich in einer guten Position?
  # Wie viele Spieler sind vor mir?
  # Wie viele Spieler kommen nach mir?
  # Was wurde vor mir gemacht?
# Wie groß sind die blindes? Wie groß ist der POT? -> Was kann ich setzen?
# Wie hoch ist die Wahrscheinlichkeit auf einen Sieg? -> Sollte ich setzen?

# bot?! O_o
class Card:
  def __init__(self, card):
    self.number = 
def replace_for_sort(cards, reverse=0):
  new_cards = []
  if reverse == 1:
    for card in cards:
      new_card = card
      new_card = new_card.replace("B", "T")
      new_card = new_card.replace("C", "J")
      new_card = new_card.replace("D", "Q")
      new_card = new_card.replace("E", "K")
      new_card = new_card.replace("F", "A")
      new_cards.append(new_card)
  else:
    for card in cards:
      new_card = card
      new_card = new_card.replace("T", "B")
      new_card = new_card.replace("J", "C")
      new_card = new_card.replace("Q", "D")
      new_card = new_card.replace("K", "E")
      new_card = new_card.replace("A", "F")
      new_cards.append(new_card)
  return new_cards

def value_of_cards(cards):
    print(cards)
    cards = replace_for_sort(cards)
    cards.sort()

    for card in cards:

    print(cards)

def compare(cards_a, cards_b, community):
    for i in community:
      cards_a.append(i)
      cards_b.append(i)
    value_a = value_of_cards(cards_a)
    value_b = value_of_cards(cards_b)

cards_a = ["A>", "K>"]
cards_b = ["2>", "K?"]
community = ["T>", "J>", "Q>"]

compare(cards_a, cards_b, community)


# cards vs. cards

# randomize game

# check if game were plaied

  # calculate winner
  # increase counter
  # store hash of the game