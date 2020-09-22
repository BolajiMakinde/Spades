# take in deck available to A.I
# output an intger corresponding to a select id in the deck
from spades import card_number as cn

def choose_Card(deck):
    lowest_Card = deck[0]
    for card in deck:
        '''
        The arrtubute nynumber is actually a string, not the actual value of
        the card. We have to use the dictionary card_number in the spades 
        in order to access it's actual value as an Integer type
        
        '''
        if deck[card.mynumber] < deck[lowest_Card.mynumber]:
            lowest_Card = card
    return lowest_Card.select_id

