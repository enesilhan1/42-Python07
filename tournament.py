from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy
from ex2 import DefensiveStrategy, AggressiveStrategy
from ex2 import InvalidStrategyError


def battle(fight: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(fight)} opponents involved")
    for i in range(len(fight)):
        for j in range(i + 1, len(fight)):
            fac1, strategy1 = fight[i]
            fac2, strategy2 = fight[j]

            creature1 = fac1.create_base()
            creature2 = fac2.create_base()

            print("\n* Battle *")

            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())

            print("now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return




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
