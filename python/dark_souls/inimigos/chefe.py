from .inimigo import Inimigo

class Chefe(Inimigo):
    def __init__(self, nome: str, dano: int, forca_especial: int):
        super().__init__(nome, dano)
        self.forca_especial = forca_especial

    def atacar(self, alvo):
        # ex.: alvo deve possuir propriedade saude
        alvo.saude -= self.dano
        print(f"{self.nome} ataca ferozmente e causa {self.dano} de dano em {alvo.nome}!")

    def ataque_especial(self, alvo):
        dano_total = self.dano + self.forca_especial
        alvo.saude -= dano_total
        print(f"{self.nome} usa ataque especial e causa {dano_total} de dano em {alvo.nome}!")
