# inimigos/inimigo.py
from abc import ABC, abstractmethod

class Inimigo(ABC):
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100  # encapsulada igual ao Jogador

    @property
    def saude(self) -> int:
        return self.__saude

    @saude.setter
    def saude(self, valor: int):
        self.__saude = max(0, self.__saude + valor)

    @abstractmethod
    def atacar(self, alvo):
        """Implementar ataque específico que afeta `alvo.saude`."""
        pass
