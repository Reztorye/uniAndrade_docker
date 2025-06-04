from typing import Dict
from collections import Counter
import random
import time

class Inventario:
    def __init__(self, capacidade_maxima: int = 10):
        # organiza os itens
        self.itens: Counter[str] = Counter()
        self.equipamentos: Dict[str, Dict] = {}
        self.capacidade_maxima = capacidade_maxima
        self.slots = dict(cabeca=None, corpo=None, maos=None, pes=None, acessorio=None)

    def adicionar_item(self, item: str, quantidade: int = 1) -> bool:
        total = sum(self.itens.values())
        if total + quantidade > self.capacidade_maxima:
            print(f"Inventário cheio ({total}/{self.capacidade_maxima})")
            return False
        self.itens[item] += quantidade
        print(f"Adicionado {quantidade}x {item}")
        return True

    def remover_item(self, item: str, quantidade: int = 1) -> bool:
        if self.itens[item] < quantidade:
            print(f"Sem {quantidade}x {item}")
            return False
        self.itens[item] -= quantidade
        if self.itens[item] == 0:
            del self.itens[item]
        print(f"Removido {quantidade}x {item}")
        return True

    def mostrar_inventario(self) -> None:
        total = sum(self.itens.values())
        print(f"\n=== INVENTÁRIO ({total}/{self.capacidade_maxima}) ===")
        if self.itens:
            for nome, qt in self.itens.items():
                print(f"- {nome} x{qt}")
        else:
            print("- Vazio")
        print("\n--- Equipamentos ---")
        for slot, itm in self.slots.items():
            print(f"{slot.capitalize()}: {itm or 'Vazio'}")

class PersonagemGame:
    def __init__(self, nome: str, vida: int, forca: int, nivel: int, classe: str):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.nivel = nivel
        self.classe = classe
        self.inventario = Inventario()

    def atacar(self, alvo: 'PersonagemGame') -> None:
        dano = self.forca * self.nivel
        alvo.vida = max(alvo.vida - dano, 0)
        print(f"{self.nome} -> {alvo.nome}: causou {dano} pontos (vida {alvo.vida})")

    def usar_item(self, item: str) -> bool:
        if self.inventario.remover_item(item):
            cura = 20  # cura fixa
            self.vida = min(self.vida + cura, 100)
            print(f"{self.nome} usou {item}, +{cura} vida (vida {self.vida})")
            return True
        print(f"{item} não disponível")
        return False

    def provocar(self, alvo: 'PersonagemGame') -> None:
        frases = [
            "Você não me assusta!",
            "Tenho certeza que pode fazer melhor.",
            "Venha lutar até o fim!"
        ]
        print(f"{self.nome} provoca: '{random.choice(frases)}'")

    def mostrar_status(self) -> None:
        print(f"[{self.nome}] {self.classe} N{self.nivel} Vida:{self.vida} Força:{self.forca}")
        self.inventario.mostrar_inventario()

if __name__ == "__main__":
    random.seed()
    hero = PersonagemGame("Herói", 100, 10, 1, "Guerreiro")
    goblin = PersonagemGame("Goblin", 80, 8, 1, "Inimigo")
    hero.inventario.adicionar_item("Poção", 2)

    turno = 1
    while hero.vida > 0 and goblin.vida > 0:
        print("\n" + "="*30)
        print(f" Turno {turno} ".center(30, "="))
        print("="*30)
        # ação do herói
        if hero.vida <= 30 and hero.inventario.itens.get("Poção", 0):
            hero.usar_item("Poção")
        else:
            hero.atacar(goblin)

        time.sleep(0.5)
        if goblin.vida <= 0:
            print(f"{goblin.nome} foi derrotado!")
            break

        # ação do goblin
        acao = random.choice(["atacar", "provocar", "esperar"])
        if acao == "atacar":
            goblin.atacar(hero)
        elif acao == "provocar":
            goblin.provocar(hero)
        else:
            print(f"{goblin.nome} hesita...")

        time.sleep(0.5)
        if hero.vida <= 0:
            print(f"{hero.nome} caiu em combate!")
            break

        turno += 1
