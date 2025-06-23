from .jogador import Jogador

class Cavaleiro(Jogador):
    def __init__(self, nome: str, dano: int, armadura: int, resistencia: int):
        super().__init__(nome, dano)
        self.armadura = armadura
        self.resistencia = resistencia

    def atacar(self, alvo, dano):
        print(f"{self.nome} golpeia {alvo.nome} causando {dano} de dano!")
        if hasattr(alvo, "saude"):
            alvo.saude -= dano


    def defender(self, dano_recebido: int):
        mitigado = min(self.armadura, self.resistencia)
        dano_final = max(0, dano_recebido - mitigado)
        self.saude -= dano_final
        print(f"{self.nome} bloqueia {mitigado} de dano. Sofreu {dano_final}. Saúde: {self.saude}")
