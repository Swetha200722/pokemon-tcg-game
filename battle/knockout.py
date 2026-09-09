from .prizes import PrizeManager


class KnockoutManager:

    @staticmethod
    def check(pokemon):

        if pokemon is None:
            return False

        return pokemon.is_knocked_out()

    @staticmethod
    def process(defending_player, attacking_player):

        pokemon = defending_player.active

        if pokemon is None:
            return False

        if not pokemon.is_knocked_out():
            return False

        defending_player.discard.append(pokemon)

        defending_player.active = None

        PrizeManager.take_prize(attacking_player)

        if defending_player.bench:
            defending_player.choose_new_active()

        return True