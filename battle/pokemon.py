class Pokemon:

    def __init__(
        self,
        name,
        hp,
        pokemon_type,
        weakness=None,
        resistance=None,
        retreat_cost=1
    ):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.pokemon_type = pokemon_type

        self.weakness = weakness
        self.resistance = resistance

        self.retreat_cost = retreat_cost

        self.attacks = []
        self.energy = []

        self.status = None

    def add_attack(self, attack):
        self.attacks.append(attack)

    def attach_energy(self, energy):
        self.energy.append(energy)

    def energy_count(self):
        return len(self.energy)

    def remove_energy(self, amount):

        if len(self.energy) < amount:
            return False

        for _ in range(amount):
            self.energy.pop()

        return True

    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def is_knocked_out(self):
        return self.hp <= 0

    def __str__(self):
        return f"{self.name} HP: {self.hp}/{self.max_hp}"