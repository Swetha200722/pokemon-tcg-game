class Attack:

    def __init__(
        self,
        name,
        damage,
        energy_cost,
        effect=None
    ):
        self.name = name
        self.damage = damage
        self.energy_cost = energy_cost
        self.effect = effect

    def can_use(self, pokemon):
        return pokemon.energy_count() >= self.energy_cost

    def execute(self, attacker):

        if not self.can_use(attacker):
            return False

        return True

    def __str__(self):
        return f"{self.name} - {self.damage} damage"