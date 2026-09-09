from .card import Card, CardType, Rarity
from enum import Enum


class PokemonStage(Enum):
    BASIC = "Basic"
    STAGE_1 = "Stage 1"
    STAGE_2 = "Stage 2"


class StatusCondition(Enum):
    NORMAL = "Normal"
    BURNED = "Burned"
    CONFUSED = "Confused"
    PARALYZED = "Paralyzed"
    POISONED = "Poisoned"
    ASLEEP = "Asleep"


class PokemonCard(Card):

    def __init__(
        self,
        card_id,
        name,
        hp,
        pokemon_type,
        stage=PokemonStage.BASIC,
        evolves_from=None,
        evolves_to=None,
        attacks=None,
        abilities=None,
        weakness=None,
        resistance=None,
        retreat_cost=0,
        rarity=Rarity.COMMON,
        description="",
        image=""
    ):

        super().__init__(
            card_id,
            name,
            CardType.POKEMON,
            rarity,
            description,
            image
        )

        self.max_hp = hp
        self.current_hp = hp

        self.pokemon_type = pokemon_type
        self.stage = stage

        self.evolves_from = evolves_from
        self.evolves_to = evolves_to or []

        self.attacks = attacks or []
        self.abilities = abilities or []

        self.weakness = weakness
        self.resistance = resistance
        self.retreat_cost = retreat_cost

        self.attached_energy = []
        self.status_conditions = [StatusCondition.NORMAL]

    # -------------------------
    # VALIDATION
    # -------------------------

    def validate(self):

        if not super().validate():
            return False

        if not isinstance(self.hp if hasattr(self, "hp") else self.max_hp, (int, float)):
            return False

        if self.max_hp <= 0:
            return False

        if not isinstance(self.stage, PokemonStage):
            return False

        if self.retreat_cost < 0:
            return False

        return True

    # -------------------------
    # ENERGY
    # -------------------------

    def attach_energy(self, energy_card):

        if energy_card is None:
            return False

        self.attached_energy.append(energy_card)
        return True

    def remove_energy(self, energy_card):

        if energy_card in self.attached_energy:
            self.attached_energy.remove(energy_card)
            return True

        return False

    def total_energy(self):

        return sum(
            energy.energy_amount
            for energy in self.attached_energy
        )

    def get_energy_types(self):

        return [
            energy.energy_type
            for energy in self.attached_energy
        ]

    def can_attack(self, attack):

        return self.total_energy() >= attack.energy_cost

    # -------------------------
    # ATTACK
    # -------------------------

    def perform_attack(self, attack, defender):

        if attack not in self.attacks:
            print("This Pokemon does not have this attack.")
            return False

        if not self.can_attack(attack):
            print("Not enough energy!")
            return False

        damage = attack.calculate_damage(
            self,
            defender
        )

        defender.take_damage(damage)

        print(f"{self.name} used {attack.name}!")
        print(
            f"{damage} damage dealt to "
            f"{defender.name}!"
        )

        if attack.has_effect():
            attack.apply_effect(
                self,
                defender
            )

        if defender.is_knocked_out():
            print(
                f"{defender.name} is Knocked Out!"
            )

        return True

    # -------------------------
    # DAMAGE & HP
    # -------------------------

    def take_damage(self, damage):

        if damage < 0:
            damage = 0

        self.current_hp -= damage

        if self.current_hp < 0:
            self.current_hp = 0

    def heal(self, amount):

        if amount < 0:
            return False

        self.current_hp += amount

        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp

        return True

    def is_knocked_out(self):

        return self.current_hp <= 0

    def reset_hp(self):

        self.current_hp = self.max_hp

    # -------------------------
    # STATUS CONDITIONS
    # -------------------------

    def add_status_condition(self, condition):

        if not isinstance(condition, StatusCondition):
            return False

        if condition == StatusCondition.NORMAL:
            self.status_conditions = [
                StatusCondition.NORMAL
            ]
            return True

        if StatusCondition.NORMAL in self.status_conditions:
            self.status_conditions.remove(
                StatusCondition.NORMAL
            )

        if condition not in self.status_conditions:
            self.status_conditions.append(condition)

        return True

    def remove_status_condition(self, condition):

        if condition in self.status_conditions:
            self.status_conditions.remove(condition)

        if not self.status_conditions:
            self.status_conditions.append(
                StatusCondition.NORMAL
            )

        return True

    def clear_status_conditions(self):

        self.status_conditions = [
            StatusCondition.NORMAL
        ]

    def is_affected(self):

        return (
            StatusCondition.NORMAL
            not in self.status_conditions
        )

    # -------------------------
    # EVOLUTION
    # -------------------------

    def can_evolve_from(self, pokemon):

        if pokemon is None:
            return False

        if self.evolves_from is None:
            return False

        if isinstance(self.evolves_from, PokemonCard):
            return (
                pokemon.name
                == self.evolves_from.name
            )

        return pokemon.name == self.evolves_from

    def can_evolve_to(self, pokemon):

        if pokemon is None:
            return False

        for evolution in self.evolves_to:

            if isinstance(evolution, PokemonCard):

                if evolution.name == pokemon.name:
                    return True

            elif evolution == pokemon.name:
                return True

        return False

    def add_evolution(self, pokemon):

        if pokemon not in self.evolves_to:
            self.evolves_to.append(pokemon)

    # -------------------------
    # ATTACKS & ABILITIES
    # -------------------------

    def add_attack(self, attack):

        if attack not in self.attacks:
            self.attacks.append(attack)

    def remove_attack(self, attack):

        if attack in self.attacks:
            self.attacks.remove(attack)
            return True

        return False

    def add_ability(self, ability):

        if ability not in self.abilities:
            self.abilities.append(ability)

    def remove_ability(self, ability):

        if ability in self.abilities:
            self.abilities.remove(ability)
            return True

        return False

    # -------------------------
    # RETREAT
    # -------------------------

    def can_retreat(self):

        return self.total_energy() >= self.retreat_cost

    # -------------------------
    # DETAILS
    # -------------------------

    def get_details(self):

        details = super().get_details()

        details.update({
            "hp": self.max_hp,
            "current_hp": self.current_hp,
            "pokemon_type": self.pokemon_type,
            "stage": self.stage.value,
            "weakness": self.weakness,
            "resistance": self.resistance,
            "retreat_cost": self.retreat_cost,
            "attacks": [
                attack.get_details()
                for attack in self.attacks
            ],
            "abilities": self.abilities,
            "attached_energy": len(
                self.attached_energy
            ),
            "status_conditions": [
                condition.value
                for condition
                in self.status_conditions
            ]
        })

        return details

    # -------------------------
    # DISPLAY
    # -------------------------

    def display_pokemon(self):

        print("-------------------------")
        print("POKEMON CARD")
        print("-------------------------")

        print(f"ID: {self.card_id}")
        print(f"Name: {self.name}")
        print(
            f"HP: "
            f"{self.current_hp}/{self.max_hp}"
        )
        print(f"Type: {self.pokemon_type}")
        print(f"Stage: {self.stage.value}")

        if self.weakness:
            print(f"Weakness: {self.weakness}")

        if self.resistance:
            print(
                f"Resistance: "
                f"{self.resistance}"
            )

        print(
            f"Retreat Cost: "
            f"{self.retreat_cost}"
        )

        print("\nAttacks:")

        for attack in self.attacks:
            attack.display()

        if self.abilities:

            print("\nAbilities:")

            for ability in self.abilities:
                print(f"- {ability}")

        print("\nStatus:")

        for condition in self.status_conditions:
            print(f"- {condition.value}")