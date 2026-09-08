from battle.pokemon import Pokemon


pokemon = Pokemon(
    "Pikachu",
    100,
    "Lightning"
)

pokemon.take_damage(30)

print("HP:", pokemon.hp)

pokemon.heal(10)

print("After Heal:", pokemon.hp)

print(
    "Knocked Out:",
    pokemon.is_knocked_out()
)