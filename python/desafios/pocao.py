class Pocao:
    def __init__(self, tipo: str, potencia: int):
        self.tipo = tipo.title()
        self.potencia = potencia


class Personagem:
    def __init__(self, nome: str):
        self.nome = nome
        self.saude = 5
        self.vivo = True

    def usar_pocao(self, pocao: Pocao) -> None:
        # Reviver
        if pocao.tipo.lower() == "reviver":
            if self.vivo:
                print(f"{self.nome} já está vivo. Poção de {pocao.tipo} não foi usada.")
            else:
                self.vivo = True
                self.saude = min(pocao.potencia, 100)
                print(f"{self.nome} foi revivido com {self.saude} de vida! 👏")
                print(r"""
         
     __/)     (\__
  ,-'~~(   _   )~~`-.
 /      \/'_`\/      \
|       /_(_)_\       |
|     _(/(\_/)\)_     |
|    / // \ / \\ \    |
 \  | ``  / \ ''  |  /
  \  )   /   \   (  /
   )/   /     \   \(
   '    `-`-'-'    `
                      """)
            return

        # Bloquei outras poções se estiver morto
        if not self.vivo:
            print(f"{self.nome} está morto e não pode usar poções.")
            return

        # Poção de cura
        if pocao.tipo.lower() == "cura":
            cura_possivel = min(pocao.potencia, 100 - self.saude)
            if cura_possivel <= 0:
                print(f"{self.nome} não precisa se curar. Saúde já está em {self.saude}.")
            else:
                self.saude += cura_possivel
                print(f"{self.nome} usou poção de {pocao.tipo} e recuperou {cura_possivel} de vida (saúde: {self.saude}).")
                print(r"""
      .-.
     ( + )   Poção de Cura!
      `-'
      |_|_
     /_|_\\
    /_____\\
""")
        # Poção de veneno
        elif pocao.tipo.lower() == "veneno":
            dano = pocao.potencia
            if self.saude - dano <= 0:
                self.saude = 0
                self.vivo = False
                print(f"{self.nome} usou poção de {pocao.tipo} e recebeu {dano} de dano (saúde: {self.saude}).")
                print(f"{self.nome} morreu.")
                print(r"""
         _____
        /     \
       | () () |
        \  ^  /
         |||||
         |||||
""")
            else:
                self.saude -= dano
                print(f"{self.nome} usou poção de {pocao.tipo} e recebeu {dano} de dano (saúde: {self.saude}).")


def menu() -> None:
    print(r"""
+===========================================+
|               MENU DO JOGO                |
+===========================================+
| 1 - Usar Poção de Cura                    |
| 2 - Usar Poção de Veneno                  |
| 3 - Usar Poção de Reviver                 |
| 4 - Mostrar Status                        |
| 5 - Sair                                  |
+===========================================+
""")


def mostrar_status(personagem: Personagem) -> None:
    """Mostra o status atual do personagem."""
    estado = "vivo" if personagem.vivo else "morto"
    print(f"\n{personagem.nome} - Saúde: {personagem.saude} - Estado: {estado}\n")


def processar_escolha(
    escolha: str,
    personagem: Personagem,
    pocao_cura: Pocao,
    pocao_veneno: Pocao,
    pocao_reviver: Pocao
) -> bool:
    """
    Processa a opção escolhida pelo player no menu.
    """
    if escolha == "1":
        personagem.usar_pocao(pocao_cura)
    elif escolha == "2":
        personagem.usar_pocao(pocao_veneno)
    elif escolha == "3":
        personagem.usar_pocao(pocao_reviver)
    elif escolha == "4":
        mostrar_status(personagem)
    elif escolha == "5":
        print("Saindo do jogo. Até mais!")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True


if __name__ == "__main__":
    p1 = Personagem("Chaves")
    pocao_cura = Pocao("Cura", 15)
    pocao_veneno = Pocao("Veneno", 20)
    pocao_reviver = Pocao("Reviver", 30)

    rodando = True
    while rodando:
        menu()
        escolha = input("Escolha uma opção (1-5): ")
        rodando = processar_escolha(escolha, p1, pocao_cura, pocao_veneno, pocao_reviver)
