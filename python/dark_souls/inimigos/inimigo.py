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
        # ⚠️ Aqui corrigido: atribui diretamente, não soma
        self.__saude = max(0, valor)

    @abstractmethod
    def atacar(self, alvo):
        pass

