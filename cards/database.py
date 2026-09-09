from .card import CardType, Rarity


class CardDatabase:

    def __init__(self):

        self.cards = {}

    # ==============================
    # ADD CARD
    # ==============================

    def add_card(self, card):

        if card is None:
            return False

        if card.card_id in self.cards:
            print("Card ID already exists.")
            return False

        self.cards[card.card_id] = card

        return True

    # ==============================
    # REMOVE CARD
    # ==============================

    def remove_card(self, card_id):

        if card_id not in self.cards:
            return None

        return self.cards.pop(card_id)

    # ==============================
    # GET CARD
    # ==============================

    def get_card(self, card_id):

        return self.cards.get(card_id)

    # ==============================
    # SEARCH BY NAME
    # ==============================

    def search_by_name(self, name):

        if not isinstance(name, str):
            return []

        return [
            card
            for card in self.cards.values()
            if name.lower() in card.name.lower()
        ]

    # ==============================
    # FILTER BY TYPE
    # ==============================

    def filter_by_type(self, card_type):

        if not isinstance(card_type, CardType):
            return []

        return [
            card
            for card in self.cards.values()
            if card.card_type == card_type
        ]

    # ==============================
    # FILTER BY RARITY
    # ==============================

    def filter_by_rarity(self, rarity):

        if not isinstance(rarity, Rarity):
            return []

        return [
            card
            for card in self.cards.values()
            if card.rarity == rarity
        ]

    # ==============================
    # CARD COUNT
    # ==============================

    def count_cards(self):

        return len(self.cards)

    def count_by_type(self, card_type):

        return len(
            self.filter_by_type(card_type)
        )

    def count_by_rarity(self, rarity):

        return len(
            self.filter_by_rarity(rarity)
        )

    # ==============================
    # CHECK CARD
    # ==============================

    def contains(self, card_id):

        return card_id in self.cards

    # ==============================
    # GET ALL CARDS
    # ==============================

    def get_all_cards(self):

        return list(self.cards.values())

    # ==============================
    # DISPLAY ALL CARDS
    # ==============================

    def show_all_cards(self):

        if not self.cards:
            print("Database is empty.")
            return

        for card in self.cards.values():

            print(
                card.card_id,
                "|",
                card.name,
                "|",
                card.card_type.value
            )

    # ==============================
    # DISPLAY CARD
    # ==============================

    def show_card(self, card_id):

        card = self.get_card(card_id)

        if card is None:
            print("Card not found.")
            return False

        card.display()

        return True

    # ==============================
    # CLEAR DATABASE
    # ==============================

    def clear(self):

        self.cards.clear()

    # ==============================
    # STRING REPRESENTATION
    # ==============================

    def __str__(self):

        return (
            f"CardDatabase("
            f"{len(self.cards)} cards)"
        )

    def __repr__(self):

        return (
            f"CardDatabase("
            f"cards={len(self.cards)})"
        )