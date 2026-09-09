from battle.player import Player
from battle.pokemon import Pokemon
from battle.attacks import Attack
from battle.energy import Energy
from battle.game import Game


player1 = Player(
    "Ash"
)

player2 = Player(
    "Gary"
)


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


thunder_shock = Attack(
    "Thunder Shock",
    30,
    1
)

water_gun = Attack(
    "Water Gun",
    20,
    1
)


pikachu.add_attack(
    thunder_shock
)

squirtle.add_attack(
    water_gun
)


player1.set_active(
    pikachu
)

player2.set_active(
    squirtle
)


game = Game(
    player1,
    player2
)


game.start()

game.start_turn()


game.attach_energy(
    Energy("Lightning")
)


result = game.attack(0)

print("\nATTACK RESULT")
print(result)


print("\nGAME STATE")
print(game.get_state())


game.end_turn()


print("\nNEXT TURN")
print(game.get_state())