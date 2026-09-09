class AIOpponent:
    def __init__(self, name="AI_Trainer"):
        self.name = name

    def execute_turn(self, game_state):
        """
        Main decision loop for Person 4's module.
        Analyzes game_state and returns a sequence of actions taken during the turn.
        """
        actions_taken = []

        # 1. Action: Place Basic Pokémon on Bench if hand contains any
        bench_actions = self._play_pokemon_to_bench(game_state)
        actions_taken.extend(bench_actions)

        # 2. Action: Attach 1 Energy card (Rule: Max 1 per turn)
        energy_action = self._attach_energy(game_state)
        if energy_action:
            actions_taken.append(energy_action)

        # 3. Action: Attack active target if energy cost is satisfied
        attack_action = self._choose_best_attack(game_state)
        if attack_action:
            actions_taken.append(attack_action)
        else:
            actions_taken.append({"action": "PASS_TURN", "reason": "Not enough energy to attack"})

        return actions_taken

    def _play_pokemon_to_bench(self, game_state):
        actions = []
        ai_hand = game_state["ai_player"]["hand"]
        ai_bench = game_state["ai_player"]["bench"]

        # Limit bench size to max 5 Pokémon
        for card in list(ai_hand):
            if card.get("card_type") == "Pokémon" and card.get("subType") == "Basic":
                if len(ai_bench) < 5:
                    ai_bench.append(card)
                    ai_hand.remove(card)
                    actions.append({"action": "BENCH_POKEMON", "card": card["name"]})
        return actions

    def _attach_energy(self, game_state):
        ai_hand = game_state["ai_player"]["hand"]
        active_pkmn = game_state["ai_player"]["active"]

        if not active_pkmn:
            return None

        # Find an energy card in hand
        energy_card = next((c for c in ai_hand if c.get("card_type") == "Energy"), None)

        if energy_card:
            active_pkmn["attached_energy"] += 1
            ai_hand.remove(energy_card)
            return {
                "action": "ATTACH_ENERGY",
                "target": active_pkmn["name"],
                "total_energy": active_pkmn["attached_energy"]
            }
        return None

    def _choose_best_attack(self, game_state):
        active_pkmn = game_state["ai_player"]["active"]
        opponent_active = game_state["opponent_player"]["active"]

        if not active_pkmn or not opponent_active:
            return None

        attached_energy = active_pkmn.get("attached_energy", 0)
        usable_attacks = []

        for attack in active_pkmn.get("attacks", []):
            if attached_energy >= attack["energy_cost"]:
                usable_attacks.append(attack)

        if not usable_attacks:
            return None

        # Pick the attack that deals the highest damage
        best_attack = max(usable_attacks, key=lambda a: a["damage"])

        # Calculate damage against opponent
        opponent_active["hp"] -= best_attack["damage"]

        return {
            "action": "ATTACK",
            "attack_name": best_attack["name"],
            "damage_dealt": best_attack["damage"],
            "target": opponent_active["name"],
            "opponent_remaining_hp": max(0, opponent_active["hp"])
        }