import abc

class Creature(abc.ABC):

    def __init__(self, name: str, kind: str):
        self.name = name
        self.kind = kind
        

    @abc.abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.kind} type Creature")


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return ("Flameling uses Ember!")
