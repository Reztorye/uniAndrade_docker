from .jogador import Jogador

class Arqueiro(Jogador):
    def __init__(self, nome: str, dano: int, flechas: int, alcance: int):
        super().__init__(nome, dano)
        self.flechas = flechas
        self.alcance = alcance

    def atacar(self, alvo, dano):
        if self.flechas <= 0:
            print(f"{self.nome} não tem flechas! Sem munição.")
            return
        self.flechas -= 1
        print(f"{self.nome} dispara flecha a {self.alcance}m e causa {dano} de dano em {alvo.nome}!")
        alvo.saude -= dano
        print(f"Flechas restantes: {self.flechas}")

    def defender(self, dano_recebido: int):
        mitigacao = self.alcance // 10
        dano_final = max(0, dano_recebido - mitigacao)
        self.saude -= dano_final
        print(f"{self.nome} tenta desviar e mitiga {mitigacao}. Sofre {dano_final}. Saúde: {self.saude}")
