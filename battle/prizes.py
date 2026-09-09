class PrizeManager:

    @staticmethod
    def take_prize(player):

        if player.prizes_remaining > 0:
            player.prizes_remaining -= 1

        return player.prizes_remaining

    @staticmethod
    def all_prizes_taken(player):
        return player.prizes_remaining == 0