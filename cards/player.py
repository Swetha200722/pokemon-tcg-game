from .pokemon import PokemonCard
from .energy import EnergyCard
from .trainer import TrainerCard


class Player:

    MAX_BENCH_SIZE = 5
    PRIZE_CARD_COUNT = 6

    def __init__(self, name, deck):

        self.name = name
        self.deck = deck

        self.hand = []
        self.active_pokemon = None
        self.bench = []
        self.discard_pile = []
        self.prize_cards = []

    # ==============================
    # DRAW CARDS
    # ==============================

    def draw_card(self):

        card = self.deck.draw()

        if card:
            self.hand.append(card)
            return card

        return None

    def draw_cards(self, number):

        drawn_cards = []

        if number <= 0:
            return drawn_cards

        for _ in range(number):

            card = self.draw_card()

            if card is None:
                break

            drawn_cards.append(card)

        return drawn_cards

    # ==============================
    # HAND MANAGEMENT
    # ==============================

    def show_hand(self):

        print(f"\n{self.name}'s Hand:")
        print("-------------------------")

        if not self.hand:
            print("Hand is empty.")
            return

        for index, card in enumerate(self.hand):

            print(
                f"{index}. "
                f"{card.name} "
                f"({card.card_type.value})"
            )

    def add_to_hand(self, card):

        if card is None:
            return False

        self.hand.append(card)

        return True

    def remove_from_hand(self, card):

        if card not in self.hand:
            return False

        self.hand.remove(card)

        return True

    def hand_size(self):

        return len(self.hand)

    # ==============================
    # ACTIVE POKEMON
    # ==============================

    def set_active_pokemon(self, pokemon):

        if not isinstance(pokemon, PokemonCard):
            return False

        if pokemon not in self.hand:
            return False

        # If an active Pokemon already exists,
        # move it to the bench if possible.
        if self.active_pokemon is not None:

            if len(self.bench) >= self.MAX_BENCH_SIZE:
                return False

            self.bench.append(self.active_pokemon)

        self.hand.remove(pokemon)
        self.active_pokemon = pokemon

        return True

    def get_active_pokemon(self):

        return self.active_pokemon

    def retreat_active_pokemon(self, pokemon):

        if self.active_pokemon is None:
            return False

        if pokemon not in self.bench:
            return False

        if not self.active_pokemon.can_retreat():
            return False

        old_active = self.active_pokemon

        self.bench.remove(pokemon)
        self.bench.append(old_active)

        self.active_pokemon = pokemon

        return True

    # ==============================
    # BENCH
    # ==============================

    def add_to_bench(self, pokemon):

        if not isinstance(pokemon, PokemonCard):
            return False

        if pokemon not in self.hand:
            return False

        if len(self.bench) >= self.MAX_BENCH_SIZE:
            print("Bench is full.")
            return False

        self.hand.remove(pokemon)
        self.bench.append(pokemon)

        return True

    def remove_from_bench(self, pokemon):

        if pokemon not in self.bench:
            return False

        self.bench.remove(pokemon)

        self.hand.append(pokemon)

        return True

    def bench_size(self):

        return len(self.bench)

    # ==============================
    # ENERGY ATTACHMENT
    # ==============================

    def attach_energy(self, energy, pokemon):

        if not isinstance(energy, EnergyCard):
            return False

        if energy not in self.hand:
            return False

        if pokemon != self.active_pokemon and pokemon not in self.bench:
            return False

        self.hand.remove(energy)

        pokemon.attach_energy(energy)

        return True

    # ==============================
    # TRAINER CARD
    # ==============================

    def use_trainer(self, trainer, target=None):

        if not isinstance(trainer, TrainerCard):
            return False

        if trainer not in self.hand:
            return False

        result = trainer.use(self, target)

        self.hand.remove(trainer)
        self.discard_pile.append(trainer)

        return result

    # ==============================
    # DISCARD PILE
    # ==============================

    def discard_card(self, card):

        if card not in self.hand:
            return False

        self.hand.remove(card)
        self.discard_pile.append(card)

        return True

    def discard_pokemon(self, pokemon):

        if pokemon in self.bench:

            self.bench.remove(pokemon)
            self.discard_pile.append(pokemon)

            return True

        if pokemon == self.active_pokemon:

            self.active_pokemon = None
            self.discard_pile.append(pokemon)

            return True

        return False

    def show_discard_pile(self):

        print("\nDiscard Pile:")
        print("-------------------------")

        if not self.discard_pile:
            print("Discard pile is empty.")
            return

        for index, card in enumerate(
            self.discard_pile,
            start=1
        ):

            print(
                f"{index}. "
                f"{card.name} "
                f"({card.card_type.value})"
            )

    # ==============================
    # PRIZE CARDS
    # ==============================

    def set_prize_cards(
        self,
        number=PRIZE_CARD_COUNT
    ):

        if number <= 0:
            return False

        self.prize_cards.clear()

        for _ in range(number):

            card = self.deck.draw()

            if card is None:
                break

            self.prize_cards.append(card)

        return True

    def take_prize(self):

        if not self.prize_cards:
            return None

        card = self.prize_cards.pop()

        self.hand.append(card)

        return card

    def prize_count(self):

        return len(self.prize_cards)

    # ==============================
    # ATTACK
    # ==============================

    def attack(self, attack, opponent):

        if self.active_pokemon is None:
            print("No active Pokemon.")
            return False

        if opponent is None:
            return False

        if opponent.active_pokemon is None:
            print("Opponent has no active Pokemon.")
            return False

        return self.active_pokemon.perform_attack(
            attack,
            opponent.active_pokemon
        )

    # ==============================
    # PLAYER STATUS
    # ==============================

    def is_defeated(self):

        if self.active_pokemon is not None:
            return False

        if self.bench:
            return False

        return True

    def show_board(self):

        print("\n=========================")
        print(f"{self.name}'s BOARD")
        print("=========================")

        if self.active_pokemon:
            print(
                f"Active Pokemon: "
                f"{self.active_pokemon.name}"
            )
        else:
            print("Active Pokemon: None")

        print("\nBench:")

        if not self.bench:
            print("Empty")

        else:
            for index, pokemon in enumerate(
                self.bench,
                start=1
            ):
                print(
                    f"{index}. "
                    f"{pokemon.name} "
                    f"({pokemon.current_hp}/"
                    f"{pokemon.max_hp} HP)"
                )

        print(f"\nHand: {len(self.hand)} cards")
        print(
            f"Prize Cards: "
            f"{len(self.prize_cards)}"
        )
        print(
            f"Discard Pile: "
            f"{len(self.discard_pile)} cards"
        )

    # ==============================
    # STRING REPRESENTATION
    # ==============================

    def __str__(self):

        return (
            f"{self.name} "
            f"(Hand: {len(self.hand)}, "
            f"Bench: {len(self.bench)}, "
            f"Prizes: {len(self.prize_cards)})"
        )

    def __repr__(self):

        return (
            f"Player("
            f"name={self.name!r}, "
            f"hand={len(self.hand)}, "
            f"bench={len(self.bench)})"
        )