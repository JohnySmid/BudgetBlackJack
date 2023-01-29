ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['pi', 'kr', 's', 'ka']
#    Pikes, Clovers, Hearts, Tiles

# suits = ['♠', '♣', '♥', '♦']



class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    #vráti reprezentaci objektu jako string
    def __repr__(self):
        return f'{self.rank}{self.suit}'
