from enum import Enum


class CardType(Enum):
    POKEMON = "Pokemon"
    ENERGY = "Energy"
    TRAINER = "Trainer"


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    ULTRA_RARE = "Ultra Rare"
    SECRET_RARE = "Secret Rare"


class Card:

    def __init__(
        self,
        card_id,
        name,
        card_type,
        rarity=Rarity.COMMON,
        description="",
        image=""
    ):

        self.card_id = card_id
        self.name = name
        self.card_type = card_type
        self.rarity = rarity
        self.description = description
        self.image = image

    # ==============================
    # VALIDATION
    # ==============================

    def validate(self):

        if self.card_id is None:
            return False

        if not isinstance(self.name, str):
            return False

        if not self.name.strip():
            return False

        if not isinstance(self.card_type, CardType):
            return False

        if not isinstance(self.rarity, Rarity):
            return False

        if not isinstance(self.description, str):
            return False

        if not isinstance(self.image, str):
            return False

        return True

    # ==============================
    # CARD TYPE CHECKING
    # ==============================

    def is_pokemon(self):

        return self.card_type == CardType.POKEMON

    def is_energy(self):

        return self.card_type == CardType.ENERGY

    def is_trainer(self):

        return self.card_type == CardType.TRAINER

    # ==============================
    # GETTERS
    # ==============================

    def get_id(self):

        return self.card_id

    def get_name(self):

        return self.name

    def get_card_type(self):

        return self.card_type

    def get_rarity(self):

        return self.rarity

    def get_description(self):

        return self.description

    def get_image(self):

        return self.image

    # ==============================
    # DETAILS
    # ==============================

    def get_details(self):

        return {
            "card_id": self.card_id,
            "name": self.name,
            "card_type": self.card_type.value,
            "rarity": self.rarity.value,
            "description": self.description,
            "image": self.image
        }

    def to_dict(self):

        return self.get_details()

    # ==============================
    # DISPLAY
    # ==============================

    def display(self):

        print("-------------------------")
        print("CARD INFORMATION")
        print("-------------------------")

        print(f"ID: {self.card_id}")
        print(f"Name: {self.name}")
        print(f"Type: {self.card_type.value}")
        print(f"Rarity: {self.rarity.value}")

        if self.description:
            print(f"Description: {self.description}")

        if self.image:
            print(f"Image: {self.image}")

    # ==============================
    # STRING REPRESENTATION
    # ==============================

    def __str__(self):

        return (
            f"{self.name} "
            f"({self.card_type.value}, "
            f"{self.rarity.value})"
        )

    def __repr__(self):

        return (
            f"Card("
            f"card_id={self.card_id!r}, "
            f"name={self.name!r}, "
            f"card_type={self.card_type!r}, "
            f"rarity={self.rarity!r})"
        )

    # ==============================
    # COMPARISON
    # ==============================

    def __eq__(self, other):

        if not isinstance(other, Card):
            return False

        return self.card_id == other.card_id

    def __hash__(self):

        return hash(self.card_id)