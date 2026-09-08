from cards.card import Rarity
from cards.attack import Attack
from cards.pokemon import PokemonCard, PokemonStage
from cards.energy import EnergyCard
from cards.trainer import TrainerCard, TrainerType
from cards.deck import Deck
from cards.player import Player
from cards.database import CardDatabase


# ==========================================
# CREATE ATTACKS
# ==========================================

thunder_shock = Attack(
    name="Thunder Shock",
    damage=30,
    energy_cost=1,
    energy_types=["Electric"]
)


quick_attack = Attack(
    name="Quick Attack",
    damage=20,
    energy_cost=1,
    energy_types=["Electric"]
)


# ==========================================
# CREATE POKEMON
# ==========================================

pikachu = PokemonCard(
    card_id=1,
    name="Pikachu",
    hp=60,
    pokemon_type="Electric",
    stage=PokemonStage.BASIC,
    attacks=[
        thunder_shock,
        quick_attack
    ],
    weakness="Fighting",
    resistance=None,
    retreat_cost=1,
    rarity=Rarity.COMMON,
    description="An Electric-type Pokemon.",
    image="images/pikachu.png"
)


charmander = PokemonCard(
    card_id=2,
    name="Charmander",
    hp=70,
    pokemon_type="Fire",
    stage=PokemonStage.BASIC,
    weakness="Water",
    retreat_cost=1,
    rarity=Rarity.COMMON,
    description="A Fire-type Pokemon."
)


# ==========================================
# CREATE ENERGY CARDS
# ==========================================

electric_energy = EnergyCard(
    card_id=101,
    name="Electric Energy",
    energy_type="Electric",
    energy_amount=1
)


fire_energy = EnergyCard(
    card_id=102,
    name="Fire Energy",
    energy_type="Fire",
    energy_amount=1
)


# ==========================================
# CREATE TRAINER CARD
# ==========================================

potion = TrainerCard(
    card_id=201,
    name="Potion",
    trainer_type=TrainerType.ITEM,
    effect_description="Heal 20 HP."
)


# ==========================================
# DATABASE
# ==========================================

database = CardDatabase()

database.add_card(pikachu)
database.add_card(charmander)
database.add_card(electric_energy)
database.add_card(fire_energy)
database.add_card(potion)


print("\n================================")
print("       CARD DATABASE")
print("================================")

database.show_all_cards()


# ==========================================
# POKEMON INFORMATION
# ==========================================

print("\n================================")
print("       POKEMON INFORMATION")
print("================================")

pikachu.display_pokemon()


# ==========================================
# ENERGY INFORMATION
# ==========================================

print("\n================================")
print("       ENERGY INFORMATION")
print("================================")

electric_energy.display_energy()


# ==========================================
# TRAINER INFORMATION
# ==========================================

print("\n================================")
print("       TRAINER INFORMATION")
print("================================")

potion.display_trainer()


# ==========================================
# CREATE DECK
# ==========================================

deck = Deck("Pikachu Deck")

deck.add_card(pikachu)
deck.add_card(charmander)
deck.add_card(electric_energy)
deck.add_card(fire_energy)
deck.add_card(potion)

print("\n================================")
print("          DECK")
print("================================")

deck.display()


# ==========================================
# CREATE PLAYER
# ==========================================

player = Player(
    name="Player 1",
    deck=deck
)


# ==========================================
# DRAW CARDS
# ==========================================

print("\n================================")
print("       DRAW CARDS")
print("================================")

player.draw_cards(3)

player.show_hand()


# ==========================================
# CARD VALIDATION
# ==========================================

print("\n================================")
print("      CARD VALIDATION")
print("================================")

print(
    "Pikachu:",
    pikachu.validate()
)

print(
    "Electric Energy:",
    electric_energy.validate()
)

print(
    "Potion:",
    potion.validate()
)


# ==========================================
# FINAL PLAYER BOARD
# ==========================================

print("\n================================")
print("       PLAYER BOARD")
print("================================")

player.show_board()


print("\n================================")
print("       SYSTEM TEST COMPLETE")
print("================================")