import abc
from . import creature


class CreatureFactory(abc.ABC):

    @abc.abstractmethod
    def create_base(self) -> creature.Creatures:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> creature.Creatures:
        pass