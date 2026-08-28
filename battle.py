from ex0 import CreatureFactory
from ex0 import FlameFactory
from ex0 import AquaFactory


def testing_factories(factory: CreatureFactory) -> None:
    warior_base = factory.create_base()
    wariore_evolve = factory.create_evolved()

    print("Testing factory")

    print(warior_base.describe())
    print(warior_base.attack())

    print(wariore_evolve.describe())
    print(wariore_evolve.attack())


def fight(first_fac: CreatureFactory, second_fac: CreatureFactory) -> None:
    warior_one = first_fac.create_base()
    warior_two = second_fac.create_base()

    print("Testing battle")

    print(warior_one.describe())
    print("vs.")
    print(warior_two.describe())

    print("fight!")

    print(warior_one.attack())
    print(warior_two.attack())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()

    testing_factories(flame)
    print()
    testing_factories(aqua)
    print()

    fight(flame, aqua)

if __name__ == "__main__":
    main()
