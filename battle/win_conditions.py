class WinCondition:

    @staticmethod
    def check(player1, player2):

        if player1.prizes_remaining == 0:
            return player1

        if player2.prizes_remaining == 0:
            return player2

        if not player1.has_available_pokemon():
            return player2

        if not player2.has_available_pokemon():
            return player1

        return None