import random
import time

# --- Importações das Classes do Jogo ---
# Jogadores
from .jogadores.cavaleiro import Cavaleiro
from .jogadores.arqueiro import Arqueiro

# NPCs
from .npcs.npc import NPC
from .npcs.ferreiro import Ferreiro

# Inimigos
from .inimigos.chefe import Chefe
from .inimigos.morto_vivo import MortoVivo

# Itens
from .itens.arma import Arma
from .itens.pocao import Pocao, PocaoBuff

# --- Funções Iniciais do Jogo ---

def escolher_heroi():
    """
    Permite ao jogador escolher entre as classes de herói disponíveis.
    Retorna uma instância da classe do herói escolhido.
    """
    print("🔰 Escolha seu herói:")
    print("1️⃣  Cavaleiro (mais defesa)")
    print("2️⃣  Arqueiro (mais flechas)")
    while True:
        escolha = input("Opção (1/2): ").strip()
        if escolha == "2":
            return Arqueiro(nome="Legolas", dano=15, flechas=10, alcance=15)
        elif escolha == "1":
            return Cavaleiro(nome="Artorias", dano=20, armadura=10, resistencia=5)
        else:
            print("❌ Opção inválida. Tente novamente.")

def montar_inventario_inicial(heroi):
    """
    Cria e retorna o inventário inicial com base na classe do herói.
    """
    print("🎒 Montando seu inventário inicial...")
    if isinstance(heroi, Cavaleiro):
        inventario = [
            Arma("Espada Longa", dano=25, resistencia=20),
            Pocao("Poção de Vida Pequena", cura=30)
        ]
    elif isinstance(heroi, Arqueiro):
        inventario = [
            Arma("Arco Curto", dano=20, resistencia=15),
            Pocao("Poção de Vida Pequena", cura=30)
        ]
    
    # Adiciona itens comuns a todas as classes
    inventario.extend([
        PocaoBuff("Poção de Força", effect_type="dano", value=10, duration=3),
        PocaoBuff("Poção de Defesa", effect_type="defesa", value=5, duration=2)
    ])
    
    for item in inventario:
        print(f"  - {item.nome} adicionado.")
    time.sleep(1)
    return inventario

# --- Funções de Interação e Menus ---

def imprimir_status_heroi(heroi):
    """Exibe o status atual do herói (Saúde, Efeitos)."""
    print(f"\n--- STATUS DE {heroi.nome.upper()} ---")
    print(f"❤️  Saúde: {heroi.saude}/{heroi.saude_maxima}")
    if heroi.efeitos_ativos:
        print("✨ Efeitos Ativos:")
        for efeito in heroi.efeitos_ativos:
            print(f"  - {efeito['type'].capitalize()}: +{efeito['value']} ({efeito['remaining_turns']} turnos restantes)")
    print("--------------------")


def imprimir_menu_principal():
    """Exibe o menu de ações principais do jogo."""
    print("\nO que você deseja fazer?")
    print("1️⃣  Ir para a Floresta (Enfrentar inimigos)")
    print("2️⃣  Visitar o Ferreiro")
    print("3️⃣  Enfrentar o Chefe Final")
    print("4️⃣  Ver Inventário e Status")
    print("0️⃣  Sair do Jogo")

def imprimir_menu_batalha():
    """Exibe as opções de ação durante uma batalha."""
    print("\n=== AÇÕES DE BATALHA ===")
    print("1️⃣  Atacar com a arma")
    print("2️⃣  Defender")
    print("3️⃣  Usar Poção")
    print("4️⃣  Fugir")

def escolher_item(heroi, inventario, tipo_item):
    """
    Função genérica para escolher um item do inventário (Poção ou Arma).
    """
    itens_disponiveis = [item for item in inventario if isinstance(item, tipo_item)]
    
    if not itens_disponiveis:
        print(f"❌ Você não possui itens do tipo '{tipo_item.__name__}'!")
        return None

    print(f"Escolha um(a) {tipo_item.__name__}:")
    for i, item in enumerate(itens_disponiveis, 1):
        if isinstance(item, Arma):
            print(f"{i}. {item.nome} (Dano: {item.dano}, Resistência: {item.resistencia})")
        elif isinstance(item, Pocao):
            if isinstance(item, PocaoBuff):
                print(f"{i}. {item.nome} (Efeito: +{item.value} de {item.effect_type})")
            else:
                print(f"{i}. {item.nome} (Cura: +{item.cura} HP)")

    while True:
        try:
            escolha = int(input("Opção: "))
            if 1 <= escolha <= len(itens_disponiveis):
                return itens_disponiveis[escolha - 1]
            else:
                print("❌ Opção inválida.")
        except ValueError:
            print("❌ Por favor, digite um número.")

# --- Lógica do Ferreiro ---

def visitar_ferreiro(heroi, ferreiro):
    """
    Gerencia a interação do jogador com o Ferreiro, permitindo forjar e reparar armas.
    """
    print(f"\nVocê encontra {ferreiro.nome}, o ferreiro da vila.")
    ferreiro.conversar()
    
    while True:
        print("\n--- FERRARIA ---")
        print(f"Você possui {ferreiro.metal} de metal.")
        print("1️⃣  Forjar Nova Arma")
        print("2️⃣  Reparar Arma")
        print("3️⃣  Melhorar Amizade (+10 metal)")
        print("0️⃣  Voltar ao menu principal")
        
        opcao = input("O que deseja fazer? ").strip()
        
        if opcao == "1":
            # Para simplificar, definimos uma arma padrão que ele pode forjar
            ferreiro.forjar_arma(
                nome_arma="Espada de Aço",
                dano=40,
                resistencia=30,
                custo_metal=50
            )
            # Adiciona a última arma forjada ao inventário do herói
            if ferreiro.inventario:
                 heroi.inventario.append(ferreiro.inventario[-1])

        elif opcao == "2":
            arma_para_reparar = escolher_item(heroi, heroi.inventario, Arma)
            if arma_para_reparar:
                # Adicionamos um atributo 'resistencia_maxima' dinamicamente para o reparo
                if not hasattr(arma_para_reparar, 'resistencia_maxima'):
                    arma_para_reparar.resistencia_maxima = arma_para_reparar.resistencia
                
                custo_reparo = (arma_para_reparar.resistencia_maxima - arma_para_reparar.resistencia) * 2 # 2 de metal por ponto
                
                if ferreiro.metal < custo_reparo:
                    print(f"❌ {ferreiro.nome}: Metal insuficiente para reparar. ({ferreiro.metal}/{custo_reparo})")
                else:
                    ferreiro.metal -= custo_reparo
                    arma_para_reparar.resistencia = arma_para_reparar.resistencia_maxima
                    print(f"🔧 {ferreiro.nome} reparou a arma {arma_para_reparar.nome}!")

        elif opcao == "3":
            if ferreiro.metal >= 10:
                ferreiro.metal -= 10
                ferreiro.melhorar_amizade(5)
            else:
                print("❌ Metal insuficiente para melhorar a amizade.")

        elif opcao == "0":
            print(f"{ferreiro.nome}: \"Até a próxima, guerreiro!\"")
            break
        else:
            print("❌ Opção inválida.")

# --- Lógica de Batalha ---

def batalha(heroi, inimigo):
    """
    Executa o loop de uma batalha entre o herói e um inimigo.
    Retorna True se o herói vencer, False caso contrário.
    """
    print(f"\n⚔️  Você encontrou um {inimigo.nome} (Saúde: {inimigo.saude})! ⚔️")
    time.sleep(1)

    while heroi.saude > 0 and inimigo.saude > 0:  # ✅ Aqui foi trocado
        imprimir_status_heroi(heroi)
        imprimir_menu_batalha()

        # -- Turno do Herói --
        acao_valida = False
        while not acao_valida:
            opc = input("Ação: ").strip()

            if opc == "1":  # Atacar
                arma_equipada = escolher_item(heroi, heroi.inventario, Arma)
                if arma_equipada:
                    dano_base = heroi.dano + arma_equipada.dano + heroi.get_buff("dano")
                    dano_final = int(dano_base * random.uniform(0.9, 1.1))

                    if random.random() < 0.1:
                        dano_final *= 2
                        print("✨ ATAQUE CRÍTICO! ✨")

                    arma_equipada.usar(heroi)
                    heroi.atacar(inimigo, dano_final)

                    if arma_equipada.resistencia <= 0:
                        heroi.inventario.remove(arma_equipada)

                    acao_valida = True

            elif opc == "2":  # Defender
                print(f"{heroi.nome} se prepara para defender!")
                heroi.defendendo = True
                acao_valida = True

            elif opc == "3":  # Usar Poção
                pocao = escolher_item(heroi, heroi.inventario, Pocao)
                if pocao:
                    pocao.usar(heroi)
                    heroi.inventario.remove(pocao)
                    acao_valida = True

            elif opc == "4":  # Fugir
                if random.random() < 0.5:
                    print("💨 Você conseguiu fugir da batalha!")
                    return True
                else:
                    print("❌ A fuga falhou! O inimigo ataca!")
                    acao_valida = True
            else:
                print("❌ Opção inválida.")

        heroi.atualizar_efeitos()
        if inimigo.saude <= 0:
            break

        # -- Turno do Inimigo --
        print(f"\n--- Turno do {inimigo.nome} ---")
        time.sleep(1)

        if isinstance(inimigo, Chefe) and random.random() < 0.3:
            inimigo.ataque_especial(heroi)
        else:
            inimigo.atacar(heroi)

        if hasattr(heroi, 'defendendo'):
            heroi.defendendo = False

    # -- Fim da Batalha --
    if heroi.saude <= 0:  # ✅ Aqui foi trocado
        print(f"💀 {heroi.nome} foi derrotado...")
        return False
    else:
        print(f"🏆 Você derrotou o {inimigo.nome}!")
        metal_ganho = random.randint(5, 20)
        print(f"💰 Você coletou {metal_ganho} de metal.")
        ferreiro.metal += metal_ganho
        return True

# --- Função Principal do Jogo (main) ---

def main():
    """
    Função principal que executa o loop do jogo.
    """
    print("=========================================")
    print("  BEM-VINDO À JORNADA DO GUERREIRO!  ")
    print("=========================================")
    
    heroi = escolher_heroi()
    heroi.inventario = montar_inventario_inicial(heroi)
    
    # Criamos a instância do Ferreiro que será usada em todo o jogo
    global ferreiro
    ferreiro = Ferreiro(
        nome="Bjorn",
        dialogo="Precisa de uma lâmina mais afiada ou um reparo? Fale comigo.",
        metal=20 # Metal inicial do jogador, gerenciado pelo ferreiro
    )

    while True:
        imprimir_menu_principal()
        escolha_menu = input("Sua escolha: ").strip()

        if escolha_menu == "1": # Floresta
            # Linha corrigida com os argumentos faltando
            inimigo = MortoVivo(nome="Morto-Vivo Errante", dano=10, podridao=5, velocidade=2)
            vitoria = batalha(heroi, inimigo)
            if not vitoria:
                print("\nGAME OVER...")
                break

        elif escolha_menu == "2": # Ferreiro
            visitar_ferreiro(heroi, ferreiro)

        elif escolha_menu == "3": # Chefe
            chefe = Chefe(nome="Gwyn, Senhor das Cinzas", dano=25, forca_especial=15)
            vitoria = batalha(heroi, chefe)
            if vitoria:
                print("\n🎉 PARABÉNS! Você concluiu a jornada! 🎉")
            else:
                print("\nGAME OVER...")
            break # Encerra o jogo após a luta contra o chefe

        elif escolha_menu == "4": # Inventário e Status
            imprimir_status_heroi(heroi)
            print("\n🎒 Inventário:")
            for item in heroi.inventario:
                detalhe = ""
                if isinstance(item, Arma):
                    detalhe = f"(Dano: {item.dano}, Resistência: {item.resistencia})"
                elif isinstance(item, Pocao) and not isinstance(item, PocaoBuff):
                    detalhe = f"(Cura: +{item.cura} HP)"
                print(f"  - {item.nome} {detalhe}")
        
        elif escolha_menu == "0": # Sair
            print("👋 Até a próxima, aventureiro!")
            break
        
        else:
            print("❌ Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()