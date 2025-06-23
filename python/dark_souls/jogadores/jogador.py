from abc import ABC, abstractmethod

class Jogador(ABC):
    def __init__(self, nome: str, dano: int):
        self.nome = nome
        self.dano = dano
        self.__saude = 100  # saúde encapsulada

    @property
    def saude(self) -> int:
        return self.__saude

    @saude.setter
    def saude(self, valor: int):
        # Só altera saúde dentro de limites
        self.__saude = max(0, min(100, valor))

    @abstractmethod
    def atacar(self, alvo, dano):
        """Ataca um alvo, recebendo o valor de dano a aplicar."""
        pass


    @abstractmethod
    def defender(self, dano_recebido: int):
        """Implementar defesa/mitigação específica."""
        pass
