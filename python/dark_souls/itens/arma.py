from .item import Item

class Arma(Item):
    def __init__(self, nome: str, dano: int, resistencia: int):
        super().__init__(nome, tipo="Arma")
        self.dano = dano
        self.resistencia = resistencia

    def usar(self, alvo):
        # Aplica dano ao alvo considerando o atributo dano
        alvo.saude -= self.dano
        print(f"{self.nome} causa {self.dano} de dano em {alvo.nome}! Saúde de {alvo.nome}: {alvo.saude}")
