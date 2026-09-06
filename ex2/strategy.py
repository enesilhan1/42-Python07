import abc
from ex0.creature import Creature
from ex1.capacitor import HealCapability
from ex1.capacitor import TransformCapability
from ex2.error import InvalidStrategyError


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "normal")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "aggressive")
        if isinstance(creature, TransformCapability):
            print(creature.transform())

        print(creature.attack())

        if isinstance(creature, TransformCapability):
            print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    pass
