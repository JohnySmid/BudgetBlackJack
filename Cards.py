ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['pi', 'kr', 's', 'ka']
#    Pikes, Clovers, Hearts, Tiles
# suits = ['♠', '♣', '♥', '♦']



class Card:
    def __init__(self, rank, suit):
        """Inicializační metoda třídy Karta.

                :param rank: hodnota karty
                :type rank: str
                :param suit: barva karty
                :type suit: str
        """
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        """Vrátí řetězcovou reprezentaci objektu.

                :return: řetězcová reprezentace objektu
                :rtype: str
        """
        return f'{self.rank}{self.suit}'
