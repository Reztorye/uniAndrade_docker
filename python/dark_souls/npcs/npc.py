from abc import ABC, abstractmethod

class NPC(ABC):
    def __init__(self, dialogo: str, amizade: int):
        self.dialogo = dialogo
        self.amizade = amizade

    @abstractmethod
    def falar(self):
        """Implementar fala e possivelmente alterar `amizade`."""
        pass
