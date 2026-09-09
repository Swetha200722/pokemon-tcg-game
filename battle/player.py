class Player:

    def __init__(self, name):

        self.name = name

        self.active = None
        self.bench = []

        self.deck = []
        self.hand = []
        self.discard = []

        self.prizes_remaining = 6

    def set_active(self, pokemon):
        self.active = pokemon

    def add_to_bench(self, pokemon):

        if len(self.bench) >= 5:
            return False

        self.bench.append(pokemon)
        return True

    def draw_card(self):

        if not self.deck:
            return None

        card = self.deck.pop()
        self.hand.append(card)

        return card

    def has_available_pokemon(self):

        if self.active is not None:
            return True

        if len(self.bench) > 0:
            return True

        return False

    def choose_new_active(self):

        if not self.bench:
            return False

        self.active = self.bench.pop(0)

        return True