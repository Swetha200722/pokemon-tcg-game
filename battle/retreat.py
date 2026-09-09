class RetreatManager:

    @staticmethod
    def can_retreat(player):

        active = player.active

        if active is None:
            return False

        if not player.bench:
            return False

        if active.energy_count() < active.retreat_cost:
            return False

        return True

    @staticmethod
    def retreat(player, bench_index):

        if not RetreatManager.can_retreat(player):
            return False

        if bench_index < 0 or bench_index >= len(player.bench):
            return False

        old_active = player.active
        new_active = player.bench[bench_index]

        old_active.remove_energy(
            old_active.retreat_cost
        )

        player.bench[bench_index] = old_active
        player.active = new_active

        return True