# jogadores/ferreiro.py
from .npc import NPC
from ..itens.arma import Arma

class Ferreiro(NPC):
    def __init__(self, nome: str, dialogo: str, amizade: int = 0, metal: int = 100):
        super().__init__(nome, dialogo, amizade)
        self.metal = metal
        self.inventario = []  # lista de itens (ex.: Arma, Pocao)

    def forjar_arma(self, nome_arma: str, dano: int, resistencia: int, custo_metal: int):
        if self.metal < custo_metal:
            print(f"❌ {self.nome}: metal insuficiente ({self.metal}/{custo_metal})")
            return None

        self.metal -= custo_metal
        nova_arma = Arma(nome_arma, dano, resistencia)
        self.inventario.append(nova_arma)
        print(f"🔨 {self.nome} forjou a arma {nome_arma}!")
        return nova_arma
    def reparar_arma(self, arma: Arma):
        if arma.resistencia >= arma.resistencia_maxima:
            print(f"❌ {self.nome}: {arma.nome} já está em perfeitas condições!")
            return

        custo_reparo = (arma.resistencia_maxima - arma.resistencia) * 10
        if self.metal < custo_reparo:
            print(f"❌ {self.nome}: metal insuficiente para reparar {arma.nome} ({self.metal}/{custo_reparo})")
            return

        self.metal -= custo_reparo
        arma.resistencia = arma.resistencia_maxima
        print(f"🔧 {self.nome} reparou a arma {arma.nome}!" )