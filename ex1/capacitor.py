import abc


class HealCapability(abc.ABC):
    @abc.abstractmethod
    def heal(self) -> str:
        pass
