class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        #print(f'karta: {card}')
        self.cards.append(card)

    # vraci hodnotu
    def get_value(self):
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
        # tj. jestli v ruka je min jak 21, pak hodnota esa je +10, jinak +1
        while num_aces > 0 and value + 10 <= 21:
            value += 10
            num_aces -= 1
        return value

    def DEBUG_LISTCARDS(self):
        for index, element in enumerate(self.cards):
            print(f"Element {element} is at index {index}")
