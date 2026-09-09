from ai_agent import AIOpponent

# Mock game state sent from Person 3/Person 5
mock_game_state = {
    "ai_player": {
        "active": {
            "name": "Charmander",
            "hp": 70,
            "attached_energy": 0,
            "attacks": [
                {"name": "Scratch", "energy_cost": 1, "damage": 10},
                {"name": "Ember", "energy_cost": 2, "damage": 30}
            ]
        },
        "bench": [],
        "hand": [
            {"name": "Fire Energy", "card_type": "Energy"},
            {"name": "Charmander", "card_type": "Pokémon", "subType": "Basic"},
            {"name": "Fire Energy", "card_type": "Energy"}
        ]
    },
    "opponent_player": {
        "active": {
            "name": "Pikachu",
            "hp": 60
        }
    }
}

# Run the AI script
if __name__ == "__main__":
    bot = AIOpponent(name="CharmanderBot")
    
    print("--- TURN 1 ---")
    turn_1_log = bot.execute_turn(mock_game_state)
    for step in turn_1_log:
        print(step)

    print("\n--- TURN 2 ---")
    turn_2_log = bot.execute_turn(mock_game_state)
    for step in turn_2_log:
        print(step)