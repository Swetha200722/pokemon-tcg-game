from .damage import DamageCalculator
from .effects import StatusEffects
from .knockout import KnockoutManager
from .retreat import RetreatManager
from .turn import TurnManager
from .win_conditions import WinCondition


class Game:

    def __init__(self, player1, player2):

        self.players = [
            player1,
            player2
        ]

        self.turn = TurnManager()

        self.winner = None
        self.started = False

        self.history = []

    def current_player(self):
        return self.players[
            self.turn.current_player
        ]

    def opponent(self):
        return self.players[
            1 - self.turn.current_player
        ]

    def start(self):

        if (
            self.players[0].active is None
            or self.players[1].active is None
        ):
            return False

        self.started = True

        self.turn.start_turn()

        self.history.append(
            "Game started"
        )

        return True

    def start_turn(self):

        player = self.current_player()

        self.turn.start_turn()

        card = player.draw_card()

        self.history.append(
            f"Turn {self.turn.turn_number}: "
            f"{player.name}'s turn"
        )

        self.turn.main_phase()

        return card

    def attach_energy(self, energy):

        player = self.current_player()

        if self.turn.energy_attached:
            return False

        if player.active is None:
            return False

        player.active.attach_energy(energy)

        self.turn.energy_attached = True

        self.history.append(
            f"{player.name} attached "
            f"{energy.energy_type} energy "
            f"to {player.active.name}"
        )

        return True

    def attack(self, attack_index):

        player = self.current_player()
        opponent = self.opponent()

        attacker = player.active
        defender = opponent.active

        if attacker is None:
            return {
                "success": False,
                "message": "No active Pokemon"
            }

        if defender is None:
            return {
                "success": False,
                "message": "Opponent has no active Pokemon"
            }

        if self.turn.attacked:
            return {
                "success": False,
                "message": "Already attacked this turn"
            }

        if attack_index < 0 or attack_index >= len(attacker.attacks):
            return {
                "success": False,
                "message": "Invalid attack"
            }

        attack = attacker.attacks[
            attack_index
        ]

        if not attack.can_use(attacker):
            return {
                "success": False,
                "message": "Not enough energy"
            }

        if not StatusEffects.can_attack(attacker):
            return {
                "success": False,
                "message":
                f"{attacker.name} cannot attack because of status"
            }

        self.turn.attack_phase()

        damage = DamageCalculator.apply(
            attacker,
            defender,
            attack
        )

        self.turn.attacked = True

        self.history.append(
            f"{attacker.name} used "
            f"{attack.name} and dealt "
            f"{damage} damage"
        )

        if attack.effect:
            attack.effect(defender)

        knocked_out = KnockoutManager.process(
            opponent,
            player
        )

        if knocked_out:
            self.history.append(
                f"{defender.name} was knocked out"
            )

        self.winner = WinCondition.check(
            self.players[0],
            self.players[1]
        )

        return {
            "success": True,
            "attacker": attacker.name,
            "attack": attack.name,
            "damage": damage,
            "defender_hp": defender.hp,
            "knockout": knocked_out,
            "winner":
                self.winner.name
                if self.winner
                else None
        }

    def retreat(self, bench_index):

        player = self.current_player()

        if self.turn.retreated:
            return False

        success = RetreatManager.retreat(
            player,
            bench_index
        )

        if success:

            self.turn.retreated = True

            self.history.append(
                f"{player.name} retreated Pokemon"
            )

        return success

    def end_turn(self):

        player = self.current_player()

        StatusEffects.end_turn_effect(
            player.active
        )

        if (
            player.active is not None
            and player.active.is_knocked_out()
        ):

            KnockoutManager.process(
                player,
                self.opponent()
            )

        self.winner = WinCondition.check(
            self.players[0],
            self.players[1]
        )

        if self.winner:
            return self.winner

        self.turn.end_phase()
        self.turn.next_turn()

        return None

    def get_state(self):

        return {
            "turn": self.turn.turn_number,

            "current_player":
                self.current_player().name,

            "phase":
                self.turn.phase,

            "player1_hp":
                self.players[0].active.hp
                if self.players[0].active
                else 0,

            "player2_hp":
                self.players[1].active.hp
                if self.players[1].active
                else 0,

            "player1_prizes":
                self.players[0].prizes_remaining,

            "player2_prizes":
                self.players[1].prizes_remaining,

            "winner":
                self.winner.name
                if self.winner
                else None
        }