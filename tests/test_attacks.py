from battle.pokemon import Pokemon
from battle.attacks import Attack
from battle.energy import Energy


pikachu = Pokemon(
    "Pikachu",
    100,
    "Lightning"
)

attack = Attack(
    "Thunder Shock",
    30,
    1
)

pikachu.add_attack(attack)

pikachu.attach_energy(
    Energy("Lightning")
)

print(
    "Can Attack:",
    attack.can_use(pikachu)
)