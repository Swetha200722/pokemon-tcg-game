from battle.turn import TurnManager


turn = TurnManager()

print(
    turn.turn_number,
    turn.current_player,
    turn.phase
)

turn.main_phase()

print("Phase:", turn.phase)

turn.next_turn()

print(
    turn.turn_number,
    turn.current_player,
    turn.phase
)