import random
from .jogadores.cavaleiro import Cavaleiro
from .jogadores.arqueiro import Arqueiro
from .inimigos.chefe import Chefe
from .inimigos.morto_vivo import MortoVivo
from .itens.arma import Arma
from .itens.pocao import Pocao, PocaoBuff

def escolher_heroi():
    print("🔰 Escolha seu herói:")
    print("1️⃣  Cavaleiro (mais defesa)")
    print("2️⃣  Arqueiro (mais flechas)")
    escolha = input("Opção (1/2): ").strip()
    if escolha == "2":
        return Arqueiro(nome="Legolas", dano=20, flechas=10, alcance=15)
    else:
        return Cavaleiro(nome="Artorias", dano=25, armadura=10, resistencia=5)

def montar_inventario(heroi):
    if isinstance(heroi, Cavaleiro):
        return [
            Arma("Espada Longa", dano=25, resistencia=100),
            Pocao("Poção de Vida", cura=50),
            PocaoBuff("Poção de Defesa", effect_type="defesa", value=0.5, duration=2),
            PocaoBuff("Poção de Força",    effect_type="dano",   value=10,  duration=3),
        ]
    elif isinstance(heroi, Arqueiro):
        return [
            Arma("Arco Curto",    dano=20, resistencia=80),
            Pocao("Poção de Vida", cura=50),
            PocaoBuff("Poção de Defesa", effect_type="defesa", value=0.5, duration=2),
            PocaoBuff("Poção de Força",    effect_type="dano",   value=10,  duration=3),
        ]
    else:
        return [
            Arma("Arma Genérica", dano=15, resistencia=50),
            Pocao("Poção Genérica", cura=40)
        ]

def imprimir_menu():
    print("\n=== AÇÕES ===")
    print("1️⃣  Atacar")
    print("2️⃣  Defender")
    print("3️⃣  Usar Poção")
    print("4️⃣  Ver Inventário")
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
    # If the user presses Enter or provides invalid input, the loop continues.
    opc = input("Ação (pressione 0 para sair, Enter para continuar): ").strip()
    if opc == "1":
        base = heroi.dano + heroi.get_buff("dano")
        var  = random.uniform(0.9, 1.1)
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
        print("🎒 Inventário:")
        for it in inventario:
            print(f"- {it.nome}")
    elif opc == "0":
        return False
    else:
        print("❌ Opção inválida. Pressione Enter para tentar novamente ou 0 para sair.")
    heroi.atualizar_efeitos()
    print(f"💥 {inimigo.nome} agora tem {inimigo.saude} de HP!\n")
    return True

def main():
    heroi      = escolher_heroi()
    inventario = montar_inventario(heroi)
    inimigo    = Chefe(nome="Gwyn", dano=20, forca_especial=15)

    print(f"\nVocê é {heroi.nome} (Vida: {heroi.saude})")
    print(f"Enfrenta: {inimigo.nome} (HP: {inimigo.saude})\n")

    turno = 1
    ativo = True
    while ativo and heroi.saude > 0:
        imprimir_menu()
        ativo = turno_heroi(heroi, inimigo, inventario)
        # se o usuário escolheu sair ou matou o inimigo, pula o turno inimigo
        if not ativo:
            break
        if inimigo.saude <= 0:
            print("🏆 Parabéns, você derrotou o chefe!")
            return

        print(f"\n--- Turno do {inimigo.nome} (#{turno}) ---")
        if turno % 3 == 0:
            inimigo.ataque_especial(heroi)
        else:
            inimigo.atacar(heroi)
        turno += 1

    # após sair do loop, checa resultado final
    if heroi.saude <= 0:
        print("💀 Você foi derrotado... Tente de novo!")
    elif inimigo.saude <= 0:
        print("🏆 Parabéns, você derrotou o chefe!")
    else:
        print("👋 Saindo do jogo!")
    

if __name__ == "__main__":
    main()
