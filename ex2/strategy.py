import abc
from ex0.creature import Creature
from ex1.capacitor import HealCapability
from ex1.capacitor import TransformCapability


class BattleStrategy(abc.ABC):
    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class NormalStrategy(BattleStrategy):
    pass


class AggressiveStrategy(BattleStrategy):
    pass


class DefensiveStrategy(BattleStrategy):
    pass
