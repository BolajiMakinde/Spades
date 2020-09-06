# take in deck available to A.I
# output an intger corresponding to a select id in the deck

from spades import *

def choose_Card(deck):
    lowest_Card = deck[0]
    for card in deck:
        if card.mynumber < lowest_Card.mynumber:
            lowest_Card = card
    return lowest_Card.select_id
