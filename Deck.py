import Cards
import random

class Deck:
    def __init__(self):
        # vytvori to balik se vsemi kartami z definovanych listu v Cards.py
        self.cards = [Cards.Card(rank, suit) for rank in Cards.ranks for suit in Cards.suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        #z konce listu popuje itemy
        return self.cards.pop()

    def DEBUG_PRINT_DECK(self):
        print(*self.cards, sep=" ")
