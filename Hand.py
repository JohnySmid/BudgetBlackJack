class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        #print(f'karta: {card}')
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                value += 1
                num_aces += 1
            else:
                value += int(card.rank)

        # vice es v ruce
        while num_aces > 0 and value + 10 <= 21:
            value += 10
            num_aces -= 1
        return value

    def DEBUG_LISTCARDS(self):
        for index, element in enumerate(self.cards):
            print(f"Element {element} is at index {index}")