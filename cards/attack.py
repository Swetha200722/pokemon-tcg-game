class Attack:

    def __init__(
        self,
        name,
        damage,
        energy_cost,
        effect=None,
        energy_types=None
    ):

        self.name = name
        self.damage = damage
        self.energy_cost = energy_cost
        self.effect = effect
        self.energy_types = energy_types or []

    # ==============================
    # VALIDATION
    # ==============================

    def validate(self):

        if not self.name or not self.name.strip():
            return False

        if not isinstance(self.damage, (int, float)):
            return False

        if self.damage < 0:
            return False

        if not isinstance(self.energy_cost, int):
            return False

        if self.energy_cost < 0:
            return False

        if not isinstance(self.energy_types, list):
            return False

        return True

    # ==============================
    # ENERGY REQUIREMENT
    # ==============================

    def get_energy_cost(self):

        return self.energy_cost

    def get_energy_types(self):

        return self.energy_types

    def can_use(self, pokemon):

        return pokemon.total_energy() >= self.energy_cost

    # ==============================
    # DAMAGE CALCULATION
    # ==============================

    def calculate_damage(self, attacker, defender):

        damage = self.damage

        # Weakness
        if (
            defender.weakness is not None
            and defender.weakness == attacker.pokemon_type
        ):
            damage *= 2

        # Resistance
        if (
            defender.resistance is not None
            and defender.resistance == attacker.pokemon_type
        ):
            damage -= 30

        if damage < 0:
            damage = 0

        return damage

    # ==============================
    # EFFECT
    # ==============================

    def has_effect(self):

        return self.effect is not None

    def apply_effect(self, attacker=None, defender=None):

        if not self.effect:
            return None

        if callable(self.effect):
            return self.effect(attacker, defender)

        return self.effect

    # ==============================
    # DETAILS
    # ==============================

    def get_details(self):

        return {
            "name": self.name,
            "damage": self.damage,
            "energy_cost": self.energy_cost,
            "energy_types": self.energy_types,
            "effect": self.effect
        }

    # ==============================
    # DISPLAY
    # ==============================

    def display(self):

        print("-------------------------")
        print(f"Attack: {self.name}")
        print(f"Damage: {self.damage}")
        print(f"Energy Cost: {self.energy_cost}")

        if self.energy_types:
            print(
                "Energy Types: "
                + ", ".join(self.energy_types)
            )

        if self.effect:
            print(f"Effect: {self.effect}")

    # ==============================
    # STRING REPRESENTATION
    # ==============================

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.damage} damage, "
            f"{self.energy_cost} energy)"
        )

    def __repr__(self):

        return (
            f"Attack("
            f"name={self.name!r}, "
            f"damage={self.damage!r}, "
            f"energy_cost={self.energy_cost!r})"
        )