import Cards
import random

class Deck:
    def __init__(self):
        """Inicializace balíčku s všemi kartami z definovaných seznamů v Cards.py."""
        self.cards = [Cards.Card(rank, suit) for rank in Cards.ranks for suit in Cards.suits]

    def shuffle(self):
        """Zamíchání karet v balíčku."""
        random.shuffle(self.cards)

    def deal(self):
        """Rozdání karty z balíčku.

            Vrátí poslední kartu z balíčku a odebere ji z něj.
        """
        return self.cards.pop()

    def DEBUG_PRINT_DECK(self):
        """Debugovací metoda výpisu karet v balíčku."""
        print(*self.cards, sep=" ")
