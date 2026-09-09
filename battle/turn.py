class TurnManager:

    def __init__(self):

        self.current_player = 0
        self.turn_number = 1
        self.phase = "DRAW"

        self.energy_attached = False
        self.retreated = False
        self.attacked = False

    def start_turn(self):

        self.phase = "DRAW"

        self.energy_attached = False
        self.retreated = False
        self.attacked = False

    def main_phase(self):
        self.phase = "MAIN"

    def attack_phase(self):
        self.phase = "ATTACK"

    def end_phase(self):
        self.phase = "END"

    def next_turn(self):

        self.current_player = 1 - self.current_player

        self.turn_number += 1

        self.start_turn()