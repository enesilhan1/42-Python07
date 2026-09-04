from ex0 import CreatureFactory
from ex0.creature import Creature
from ex1.creatures import Sproutling
from ex1.creatures import Bloomelle
from ex1.creatures import Morphagon
from ex1.creatures import Shiftling


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()