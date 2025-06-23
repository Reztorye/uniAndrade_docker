from abc import ABC, abstractmethod

class Jogador(ABC):
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
        self.__saude = 100
        self.saude_maxima = 100
        self.efeitos_ativos = []

    @property
    def saude(self):
        return self.__saude

    @saude.setter
    def saude(self, valor):
        self.__saude = max(0, min(valor, self.saude_maxima))

    @abstractmethod
    def atacar(self, alvo, dano):
        pass

    @abstractmethod
    def defender(self, dano_recebido: int):
        pass

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
