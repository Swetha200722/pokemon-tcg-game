from battle.player import Player
from battle.pokemon import Pokemon
from battle.knockout import KnockoutManager


p1 = Player("Player 1")
p2 = Player("Player 2")

pikachu = Pokemon(
    "Pikachu",
    30,
    "Lightning"
)

p2.active = pikachu

pikachu.take_damage(30)

result = KnockoutManager.process(
    p2,
    p1
)

print("Knockout:", result)
print(
    "Player 1 prizes:",
    p1.prizes_remaining
)