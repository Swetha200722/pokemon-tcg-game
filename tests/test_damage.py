from battle.pokemon import Pokemon
from battle.attacks import Attack
from battle.damage import DamageCalculator


pikachu = Pokemon(
    "Pikachu",
    100,
    "Lightning"
)

squirtle = Pokemon(
    "Squirtle",
    100,
    "Water",
    weakness="Lightning"
)

attack = Attack(
    "Thunder Shock",
    30,
    1
)

damage = DamageCalculator.apply(
    pikachu,
    squirtle,
    attack
)

print("Damage:", damage)
print("Squirtle HP:", squirtle.hp)