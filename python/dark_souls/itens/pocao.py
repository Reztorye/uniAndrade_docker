# itens/pocao.py

from .item import Item

# dark_souls/itens/pocao.py

from .item import Item

class Pocao(Item):
    def __init__(self, nome, cura):
        super().__init__(nome, tipo="pocao")
        self.cura = cura

    def usar(self, alvo):
        alvo.saude = min(alvo.saude + self.cura, alvo.saude_maxima)
        print(f"❤️ {alvo.nome} recuperou {self.cura} de HP!")

class PocaoBuff(Pocao):
    def __init__(self, nome, effect_type, value, duration):
        super().__init__(nome, cura=0)
        self.tipo = "buff"
        self.effect_type = effect_type
        self.value = value
        self.duration = duration

    def usar(self, alvo):
        efeito = {
            'type': self.effect_type,
            'value': self.value,
            'remaining_turns': self.duration
        }
        alvo.adicionar_efeito(efeito)
        print(f"✨ {alvo.nome} ganhou +{self.value} de {self.effect_type} por {self.duration} turnos!")
