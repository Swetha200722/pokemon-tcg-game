class DamageCalculator:

    @staticmethod
    def calculate(attacker, defender, attack):

        damage = attack.damage

        if defender.weakness == attacker.pokemon_type:
            damage *= 2

        if defender.resistance == attacker.pokemon_type:
            damage -= 20

        if damage < 0:
            damage = 0

        return damage

    @staticmethod
    def apply(attacker, defender, attack):

        damage = DamageCalculator.calculate(
            attacker,
            defender,
            attack
        )

        defender.take_damage(damage)

        return damage