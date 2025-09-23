import random

class BotMemoria:
    def __init__(self, tamanho_memoria=4):
        # memória do bot: {id_carta: [posições]}
        self.memoria = {}
        self.tamanho_memoria = tamanho_memoria  

    def atualizar_memoria(self, carta, posicao):
        """Adiciona uma carta à memória do bot."""
        if carta not in self.memoria:
            self.memoria[carta] = []
        if posicao not in self.memoria[carta]:
            self.memoria[carta].append(posicao)

        # Se a memória estourar, remove cartas antigas
        if sum(len(v) for v in self.memoria.values()) > self.tamanho_memoria:
            chave_removida = list(self.memoria.keys())[0]
            self.memoria[chave_removida].pop(0)
            if not self.memoria[chave_removida]:
                del self.memoria[chave_removida]

    def escolher_jogada(self, posicoes_restantes):
        """Decide a jogada do bot baseado na memória."""

        # 1. Verifica se existe um par conhecido
        for carta, posicoes in self.memoria.items():
            if len(posicoes) == 2:
                return posicoes  

        # 2. Verifica se há uma carta única na memória
        for carta, posicoes in self.memoria.items():
            if len(posicoes) == 1:
                pos = posicoes[0]
                outra = random.choice([p for p in posicoes_restantes if p != pos])
                return [pos, outra]

        # 3. Se não sabe nada → joga duas aleatórias
        return random.sample(posicoes_restantes, 2)
