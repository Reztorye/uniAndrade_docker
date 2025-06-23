from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nome: str, tipo: str):
        self.nome = nome
        self.tipo = tipo

    @abstractmethod
    def usar(self, alvo):
        """Define o comportamento ao usar este item."""
        pass
