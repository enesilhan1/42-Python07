import abc
from . import creature


class CreatureFactory(abc.ABC):

    @abc.abstractmethod
    def create_base(self) -> creature.Creature:
        pass

    @abc.abstractmethod
    def create_evolved(self) -> creature.Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        return creature.Flameling()

    def create_evolved(self) -> creature.Creature:
        return creature.Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> creature.Creature:
        return creature.Aquabub()

    def create_evolved(self) -> creature.Creature:
        return creature.Torragon()