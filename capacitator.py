from ex1 import creatures
from ex1 import capacitor
from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory


def healing(fac: HealingCreatureFactory) -> None:
    base = fac.create_base()
    print("Testing Creature with healing capability")
    print(" base:")

    print(base.describe())
    print(base.attack())
    print(base.heal())




def main() -> None:
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()

    healing(heal)


if __name__ == "__main__":
    main()