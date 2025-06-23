# jogadores/jogador.py

class Jogador:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
        self.saude = 100
        self.saude_maxima = 100
        # → Novo:
        self.efeitos_ativos = []

    def adicionar_efeito(self, efeito):
        self.efeitos_ativos.append(efeito)

    def get_buff(self, effect_type):
        return sum(e['value'] for e in self.efeitos_ativos if e['type'] == effect_type)

    def atualizar_efeitos(self):
        for e in self.efeitos_ativos[:]:
            e['remaining_turns'] -= 1
            if e['remaining_turns'] <= 0:
                self.efeitos_ativos.remove(e)
                print(f"🔔 Efeito de {e['type']} expirou em {self.nome}!")
