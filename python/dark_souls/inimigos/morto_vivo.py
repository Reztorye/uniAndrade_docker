# inimigos/morto_vivo.py
from .inimigo import Inimigo

class MortoVivo(Inimigo):
    def __init__(self, nome: str, dano: int, podridao: int, velocidade: int):
        super().__init__(nome, dano)
        self.podridao = podridao
        self.velocidade = velocidade

    def morder(self, alvo) -> None:
        dano_total = self.dano + self.podridao
        print(f"🦴 {self.nome} morde {alvo.nome} e causa {dano_total} de dano!")
        alvo.defender(dano_total)

    def atacar(self, alvo) -> None:
        self.morder(alvo)
