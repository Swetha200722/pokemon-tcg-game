import random


class StatusEffects:

    @staticmethod
    def poison(pokemon):
        pokemon.status = "POISONED"

    @staticmethod
    def burn(pokemon):
        pokemon.status = "BURNED"

    @staticmethod
    def sleep(pokemon):
        pokemon.status = "ASLEEP"

    @staticmethod
    def paralysis(pokemon):
        pokemon.status = "PARALYZED"

    @staticmethod
    def confusion(pokemon):
        pokemon.status = "CONFUSED"

    @staticmethod
    def clear(pokemon):
        pokemon.status = None

    @staticmethod
    def can_attack(pokemon):

        if pokemon.status == "ASLEEP":
            return False

        if pokemon.status == "PARALYZED":
            return False

        if pokemon.status == "CONFUSED":

            result = random.choice([True, False])

            if not result:
                pokemon.take_damage(30)

            return result

        return True

    @staticmethod
    def end_turn_effect(pokemon):

        if pokemon is None:
            return

        if pokemon.status == "POISONED":
            pokemon.take_damage(10)

        elif pokemon.status == "BURNED":
            pokemon.take_damage(20)

            if random.choice([True, False]):
                pokemon.status = None

        elif pokemon.status == "ASLEEP":

            if random.choice([True, False]):
                pokemon.status = None

        elif pokemon.status == "PARALYZED":
            pokemon.status = None