from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidStrategyError


def battle(fight: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    pass


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([(flame, normal), (heal, defensive)])

    print("\nTournament 1 (error)")
    battle([(flame, aggressive), (heal, defensive)])

    print("\nTournament 2 (multiple)")
    battle([(aqua, normal), (heal, defensive), (transform, aggressive)])

    print()



if __name__ == "__main__":
    main()
