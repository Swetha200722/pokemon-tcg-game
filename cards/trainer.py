from .card import Card, CardType, Rarity
from enum import Enum


class TrainerType(Enum):

    ITEM = "Item"
    SUPPORTER = "Supporter"
    STADIUM = "Stadium"
    TOOL = "Tool"


class TrainerCard(Card):

    def __init__(
        self,
        card_id,
        name,
        trainer_type,
        effect_description,
        effect=None,
        rarity=Rarity.COMMON,
        description="",
        image=""
    ):

        super().__init__(
            card_id,
            name,
            CardType.TRAINER,
            rarity,
            description,
            image
        )

        self.trainer_type = trainer_type
        self.effect_description = effect_description
        self.effect = effect

    # ==============================
    # VALIDATION
    # ==============================

    def validate(self):

        if not super().validate():
            return False

        if not isinstance(self.trainer_type, TrainerType):
            return False

        if (
            not isinstance(
                self.effect_description,
                str
            )
            or not self.effect_description.strip()
        ):
            return False

        return True

    # ==============================
    # TYPE CHECKING
    # ==============================

    def is_item(self):

        return self.trainer_type == TrainerType.ITEM

    def is_supporter(self):

        return self.trainer_type == TrainerType.SUPPORTER

    def is_stadium(self):

        return self.trainer_type == TrainerType.STADIUM

    def is_tool(self):

        return self.trainer_type == TrainerType.TOOL

    # ==============================
    # EFFECT
    # ==============================

    def has_effect(self):

        return self.effect is not None

    def use(self, player=None, target=None):

        if self.effect:

            if callable(self.effect):
                return self.effect(player, target)

            return self.effect

        print(self.effect_description)

        return True

    # ==============================
    # DETAILS
    # ==============================

    def get_details(self):

        details = super().get_details()

        details.update({
            "trainer_type": self.trainer_type.value,
            "effect_description": self.effect_description,
            "effect": self.effect
        })

        return details

    # ==============================
    # DISPLAY
    # ==============================

    def display_trainer(self):

        print("-------------------------")
        print("TRAINER CARD")
        print("-------------------------")

        print(f"ID: {self.card_id}")
        print(f"Name: {self.name}")
        print(f"Trainer Type: {self.trainer_type.value}")
        print(f"Rarity: {self.rarity.value}")

        print(
            f"Effect: "
            f"{self.effect_description}"
        )

        if self.description:
            print(
                f"Description: "
                f"{self.description}"
            )

    # ==============================
    # STRING REPRESENTATION
    # ==============================

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.trainer_type.value}, "
            f"{self.rarity.value})"
        )

    def __repr__(self):

        return (
            f"TrainerCard("
            f"card_id={self.card_id!r}, "
            f"name={self.name!r}, "
            f"trainer_type={self.trainer_type!r})"
        )