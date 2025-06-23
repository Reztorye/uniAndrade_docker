import random
from .jogadores.cavaleiro import Cavaleiro
from .jogadores.arqueiro import Arqueiro
from .inimigos.chefe import Chefe
from .inimigos.morto_vivo import MortoVivo
from .itens.arma import Arma
from .itens.pocao import Pocao

def escolher_heroi():
    print("🔰 Escolha seu herói:")
    print("1️⃣  Cavaleiro (mais defesa)")
    print("2️⃣  Arqueiro (mais flechas)")
    escolha = input("Opção (1/2): ").strip()
    if escolha == "2":
        return Arqueiro(nome="Legolas", dano=20, flechas=10, alcance=15)
    else:
        return Cavaleiro(nome="Artorias", dano=25, armadura=10, resistencia=5)

def montar_inventario():
    return [
        Arma(nome="Espada Longa", dano=25, resistencia=100),
        Pocao(nome="Poção de Vida", cura=50),
        Pocao(nome="Poção Menor", cura=30),
    ]

def imprimir_menu():
    print("\n=== AÇÕES ===")
    print("1️⃣  Atacar")
    print("2️⃣  Defender")
    print("3️⃣  Usar Poção")
    print("4️⃣  Ver Status")
    print("5️⃣  Ver Inventário")
    print("0️⃣  Sair")

def usar_pocao(heroi, inventario):
    poções = [i for i in inventario if isinstance(i, Pocao)]
    if not poções:
        print("❌ Você não tem poções!")
        return
    for idx, p in enumerate(poções, 1):
        print(f"{idx}. {p.nome} (+{p.cura} HP)")
    escolha = input("Qual usar? ").strip()
    try:
        pocao = poções[int(escolha)-1]
        pocao.usar(heroi)
        inventario.remove(pocao)
    except:
        print("❌ Escolha inválida.")

def turno_heroi(heroi, inimigo, inventario):
    opc = input("Ação: ").strip()
    if opc == "1":
        base = heroi.dano
        var = random.uniform(0.9, 1.1)
        dano = int(base * var)
        if random.random() < 0.1:
            dano *= 2
            print("✨ CRÍTICO! ✨")
        heroi.atacar(inimigo, dano)
    elif opc == "2":
        heroi.defender(inimigo.dano)
    elif opc == "3":
        usar_pocao(heroi, inventario)
    elif opc == "4":
        print(f"🛡️ {heroi.nome} - Vida: {heroi.saude}")
    elif opc == "5":
        print("🎒 Inventário:")
        for it in inventario:
            print(f"- {it.nome}")
    elif opc == "0":
        return False
    else:
        print("❌ Opção inválida.")
    return True

def main():
    heroi     = escolher_heroi()
    inventario= montar_inventario()
    inimigo   = Chefe(nome="Gwyn", dano=20, forca_especial=15)

    print(f"\nVocê é {heroi.nome} (Vida: {heroi.saude})")
    print(f"Enfrenta: {inimigo.nome} (HP: {inimigo.saude})\n")

    turno = 1
    ativo = True
    while ativo and heroi.saude > 0 and inimigo.saude > 0:
        imprimir_menu()
        ativo = turno_heroi(heroi, inimigo, inventario)
        if not ativo or inimigo.saude <= 0:
            break

        print(f"\n--- Turno do {inimigo.nome} (#{turno}) ---")
        if turno % 3 == 0:
            inimigo.ataque_especial(heroi)
        else:
            inimigo.atacar(heroi)
        turno += 1

    print()
    if inimigo.saude <= 0:
        print("🏆 Parabéns, você derrotou o chefe!")
    elif heroi.saude <= 0:
        print("💀 Você foi derrotado... Tente de novo!")
    else:
        print("👋 Saindo do jogo!")

if __name__ == "__main__":
    main()
