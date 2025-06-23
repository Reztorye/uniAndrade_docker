# itens/item.py
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    @abstractmethod
    def usar(self, alvo):
        """Define o efeito do item sobre o alvo."""
        pass