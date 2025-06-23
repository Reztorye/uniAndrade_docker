# inimigos/chefe.py
from .inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self, nome: str, dano: int, forca_especial: int):
        super().__init__(nome, dano)
        self.forca_especial = forca_especial

    def ataque_especial(self, alvo) -> None:
        dano_total = self.dano + self.forca_especial
        print(f"👹 {self.nome} usa ATAQUE ESPECIAL! Causa {dano_total} de dano.")
        alvo.defender(dano_total)

    def atacar(self, alvo) -> None:
        # Ataque normal ou especial, sua escolha de lógica
        self.ataque_especial(alvo)
    def esta_vivo(self) -> bool:
        if self.saude <= 0:
            print(f"👹 {self.nome} foi derrotado!")
            return False
        return True