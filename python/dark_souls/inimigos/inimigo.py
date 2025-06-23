# inimigos/inimigo.py
from abc import ABC, abstractmethod

class Inimigo(ABC):
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100

    @property
    def saude(self) -> int:
        return self.__saude

    @saude.setter
    def saude(self, valor: int):
        self.__saude = max(0, min(valor, 100))

    @abstractmethod
    def atacar(self, alvo):
        """Inflige dano ao alvo."""
        pass

    def defender(self, dano_recebido: int) -> None:
        self.saude -= dano_recebido
        print(f"{self.nome} recebeu {dano_recebido} de dano (saúde: {self.saude}/100).")
    def esta_vivo(self) -> bool:
        return self.saude > 0