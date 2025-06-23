from abc import ABC, abstractmethod

class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    @abstractmethod
    def usar(self, alvo):
        """Define o comportamento ao usar este item."""
        pass
