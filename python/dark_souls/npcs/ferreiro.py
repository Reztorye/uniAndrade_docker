from .npc import NPC

class Ferreiro(NPC):
    def __init__(self, dialogo: str, amizade: int, inventario: list, metal: str):
        super().__init__(dialogo, amizade)
        self.inventario = inventario  # lista de objetos Item
        self.metal = metal

    def falar(self):
        print(f"{self.dialogo} (Amizade: {self.amizade})")

    def vender_item(self, jogador, item):
        if item in self.inventario:
            self.inventario.remove(item)
            print(f"{self.dialogo} vendeu {item.nome} a {jogador.nome}.")
            # aqui você pode adicionar ao inventário do jogador, se existir
        else:
            print(f"Desculpe, não tenho {item.nome} no momento.")
