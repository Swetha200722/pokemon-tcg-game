import random
from .card import CardType


class Deck:

    MAX_CARDS = 60
    MAX_SAME_CARD = 4

    def __init__(self, name):

        self.name = name
        self.cards = []

    # ==============================
    # ADD CARD
    # ==============================

    def add_card(self, card):

        if card is None:
            return False

        if len(self.cards) >= self.MAX_CARDS:
            print("Deck is full.")
            return False

        same_card_count = sum(
            1
            for c in self.cards
            if c.card_id == card.card_id
        )

        # Energy cards can have more than 4 copies
        if (
            card.card_type != CardType.ENERGY
            and same_card_count >= self.MAX_SAME_CARD
        ):
            print("Maximum copies reached.")
            return False

        self.cards.append(card)

        return True

    # ==============================
    # REMOVE CARD
    # ==============================

    def remove_card(self, card_id):

        for card in self.cards:

            if card.card_id == card_id:

                self.cards.remove(card)

                return card

        return None

    # ==============================
    # SHUFFLE
    # ==============================

    def shuffle(self):

        random.shuffle(self.cards)

    # ==============================
    # DRAW
    # ==============================

    def draw(self):

        if not self.cards:
            return None

        return self.cards.pop(0)

    def draw_cards(self, number):

        drawn_cards = []

        if number <= 0:
            return drawn_cards

        for _ in range(number):

            card = self.draw()

            if card is None:
                break

            drawn_cards.append(card)

        return drawn_cards

    # ==============================
    # SEARCH
    # ==============================

    def find_card(self, card_id):

        for card in self.cards:

            if card.card_id == card_id:
                return card

        return None

    def search_by_name(self, name):

        if not isinstance(name, str):
            return []

        return [
            card
            for card in self.cards
            if name.lower() in card.name.lower()
        ]

    # ==============================
    # COUNT
    # ==============================

    def count_cards(self):

        return len(self.cards)

    def count_card(self, card_id):

        return sum(
            1
            for card in self.cards
            if card.card_id == card_id
        )

    # ==============================
    # DECK STATUS
    # ==============================

    def is_empty(self):

        return len(self.cards) == 0

    def is_full(self):

        return len(self.cards) == self.MAX_CARDS

    # ==============================
    # VALIDATION
    # ==============================

    def validate(self):

        if len(self.cards) != self.MAX_CARDS:
            return False

        return True

    # ==============================
    # DISPLAY
    # ==============================

    def display(self):

        print("-------------------------")
        print("DECK INFORMATION")
        print("-------------------------")

        print(f"Deck Name: {self.name}")
        print(f"Total Cards: {len(self.cards)}")

        print("\nCards:")

        for index, card in enumerate(self.cards, start=1):

            print(
                f"{index}. "
                f"{card.name} "
                f"({card.card_type.value})"
            )

    # ==============================
    # CLEAR DECK
    # ==============================

    def clear(self):

        self.cards.clear()

    # ==============================
    # STRING REPRESENTATION
    # ==============================

    def __str__(self):

        return (
            f"{self.name} "
            f"({len(self.cards)}/"
            f"{self.MAX_CARDS} cards)"
        )

    def __repr__(self):

        return (
            f"Deck("
            f"name={self.name!r}, "
            f"cards={len(self.cards)})"
        )