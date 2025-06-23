# jogadores/npc.py
from abc import ABC, abstractmethod

class NPC(ABC):
    def __init__(self, nome: str, dialogo: str, amizade: int = 0):
        self.nome = nome
        self.dialogo = dialogo
        self.amizade = amizade

    def conversar(self) -> None:
        print(f"{self.nome} diz: “{self.dialogo}”")

    def melhorar_amizade(self, pontos: int) -> None:
        self.amizade += pontos
        print(f"🔔 Amizade com {self.nome} agora é {self.amizade}!")
    def piorar_amizade(self, pontos: int) -> None:
        self.amizade -= pontos
        if self.amizade < 0:
            self.amizade = 0
        print(f"🔔 Amizade com {self.nome} agora é {self.amizade}!" )