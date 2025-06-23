from .inimigo import Inimigo

class MortoVivo(Inimigo):
    def __init__(self, nome: str, dano: int, podridao: int, velocidade: int):
        super().__init__(nome, dano)
        self.podridao = podridao
        self.velocidade = velocidade

    def atacar(self, alvo):
        alvo.saude -= self.dano
        print(f"{self.nome} investe e causa {self.dano} de dano em {alvo.nome}!")

    def morder(self, alvo):
        dano_extra = self.dano + self.podridao
        alvo.saude -= dano_extra
        print(f"{self.nome} morde e causa {dano_extra} de dano (incluindo {self.podridao} de podridão) em {alvo.nome}!")
