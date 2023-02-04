class Hand:
    def __init__(self):
        """Inicializace prázdného seznamu karet v ruce."""
        self.cards = []

    def add_card(self, card):
        """Přidání karty do seznamu karet v ruce."""
        #print(f'karta: {card}')
        self.cards.append(card)

    # vraci hodnotu
    def get_value(self):
        """Výpočet hodnoty karet v ruce.

            Vrátí součet hodnot jednotlivých karet v ruce, zvažující esa jako 1 nebo 11 v závislosti na hodnotě ostatních karet.
        """
        value = 0
        num_aces = 0
        # projde to karty v ruce
        for card in self.cards:
            # jestli je to J Q K, tak +10
            if card.rank in ['J', 'Q', 'K']:
                value += 10
            # pokud eso, tak zatim +1
            elif card.rank == 'A':
                value += 1
                num_aces += 1
            # jinak +rank karty
            else:
                value += int(card.rank)

        # vice es v ruce
        # tj. jestli v ruka je min jak 21, pak hodnota esa je +10(+1 uz mame) = +11, jinak zustane hodnota +1
        while num_aces > 0 and value + 10 <= 21:
            value += 10
            num_aces -= 1
        return value

    def DEBUG_LISTCARDS(self):
        """Debugovací metoda výpisu karet v ruce."""
        for index, element in enumerate(self.cards):
            print(f"Element {element} is at index {index}")
