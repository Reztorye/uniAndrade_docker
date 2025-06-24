# itens/arma.py
from .item import Item

class Arma(Item):
    def __init__(self, nome: str, dano: int, resistencia: int):
        super().__init__(nome)
        self.dano = dano
        self.resistencia = resistencia

    def usar(self, usuario) -> None: 
        self.resistencia -= 1
        if self.resistencia <= 0:
            print(f"💥 {self.nome} quebrou!")
            self.resistencia = 0