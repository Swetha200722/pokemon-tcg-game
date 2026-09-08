from .card import Card, CardType, Rarity


class EnergyCard(Card):

    def __init__(
        self,
        card_id,
        name,
        energy_type,
        energy_amount=1,
        is_special=False,
        effect=None,
        rarity=Rarity.COMMON,
        description="",
        image=""
    ):

        super().__init__(
            card_id,
            name,
            CardType.ENERGY,
            rarity,
            description,
            image
        )

        self.energy_type = energy_type
        self.energy_amount = energy_amount
        self.is_special = is_special
        self.effect = effect

    # ==============================
    # VALIDATION
    # ==============================

    def validate(self):

        if not super().validate():
            return False

        if not isinstance(self.energy_type, str):
            return False

        if not self.energy_type.strip():
            return False

        if not isinstance(self.energy_amount, int):
            return False

        if self.energy_amount <= 0:
            return False

        if not isinstance(self.is_special, bool):
            return False

        return True

    # ==============================
    # ENERGY INFORMATION
    # ==============================

    def get_energy_value(self):

        return self.energy_amount

    def get_energy_type(self):

        return self.energy_type

    def is_basic_energy(self):

        return not self.is_special

    def is_special_energy(self):

        return self.is_special

    # ==============================
    # EFFECT
    # ==============================

    def has_effect(self):

        return self.effect is not None

    def apply_effect(self, pokemon=None):

        if not self.effect:
            return None

        if callable(self.effect):
            return self.effect(pokemon)

        return self.effect

    # ==============================
    # DETAILS
    # ==============================

    def get_details(self):

        details = super().get_details()

        details.update({
            "energy_type": self.energy_type,
            "energy_amount": self.energy_amount,
            "is_special": self.is_special,
            "effect": self.effect
        })

        return details

    # ==============================
    # DISPLAY
    # ==============================

    def display_energy(self):

        print("-------------------------")
        print("ENERGY CARD")
        print("-------------------------")

        print(f"ID: {self.card_id}")
        print(f"Name: {self.name}")
        print(f"Energy Type: {self.energy_type}")
        print(f"Energy Amount: {self.energy_amount}")

        if self.is_special:
            print("Energy Category: Special Energy")
        else:
            print("Energy Category: Basic Energy")

        if self.effect:
            print(f"Effect: {self.effect}")

        if self.description:
            print(f"Description: {self.description}")

    # ==============================
    # STRING REPRESENTATION
    # ==============================

    def __str__(self):

        category = "Special" if self.is_special else "Basic"

        return (
            f"{self.name} "
            f"({self.energy_type}, "
            f"{category}, "
            f"{self.energy_amount} energy)"
        )

    def __repr__(self):

        return (
            f"EnergyCard("
            f"card_id={self.card_id!r}, "
            f"name={self.name!r}, "
            f"energy_type={self.energy_type!r}, "
            f"energy_amount={self.energy_amount!r})"
        )