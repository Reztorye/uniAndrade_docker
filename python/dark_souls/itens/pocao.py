from .item import Item

class Pocao(Item):
    def __init__(self, nome: str, cura: int):
        super().__init__(nome, tipo="Poção")
        self.cura = cura

    def usar(self, jogador):
        # Cura o jogador e imprime status
        jogador.saude += self.cura
        print(f"{jogador.nome} bebeu {self.nome} e recuperou {self.cura} de saúde! Saúde atual: {jogador.saude}")
