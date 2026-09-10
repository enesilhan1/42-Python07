from ex1.capacitor import HealCapability
from ex1.capacitor import TransformCapability
from ex1 import HealingCreatureFactory
from ex1 import TransformCreatureFactory


def healing(fac: HealingCreatureFactory) -> None:
    base = fac.create_base()
    print("Testing Creature with healing capability")
    print(" base:")

    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())

    evo = fac.create_evolved()
    print(" evolved:")
    print(evo.describe())
    print(evo.attack())
    if isinstance(evo, HealCapability):
        print(evo.heal())


def transform(fac: TransformCreatureFactory) -> None:
    base = fac.create_base()
    print("Testing Creature with transform capability")
    print(" base:")
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.revert())

    evo = fac.create_evolved()
    print(" evolved:")
    print(evo.describe())
    print(evo.attack())
    if isinstance(evo, TransformCapability):
        print(evo.transform())
    print(evo.attack())
    if isinstance(evo, TransformCapability):
        print(evo.revert())


def main() -> None:
    heal = HealingCreatureFactory()
    trans = TransformCreatureFactory()

    healing(heal)
    print()
    transform(trans)


if __name__ == "__main__":
    main()
