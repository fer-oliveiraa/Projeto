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

    def remover_par_da_memoria(self, carta_id):
        """NOVO: Remove um par encontrado da memória do bot."""
        if carta_id in self.memoria:
            del self.memoria[carta_id]

    def escolher_jogada(self, posicoes_restantes):
        """Decide a jogada do bot baseado na memória."""

        # Verifica se existe um par conhecido na memória
        for carta, posicoes in self.memoria.items():
            if len(posicoes) == 2:
                # Garante que as posições conhecidas ainda estão em jogo
                if all(p in posicoes_restantes for p in posicoes):
                    return posicoes

        # Verifica se há uma carta única na memória
        for carta, posicoes in self.memoria.items():
            if len(posicoes) == 1:
                pos = posicoes[0]
                if pos in posicoes_restantes:
                    # Tenta encontrar uma carta aleatória que não seja a própria carta conhecida
                    outras_posicoes = [p for p in posicoes_restantes if p != pos]
                    if outras_posicoes:
                        outra = random.choice(outras_posicoes)
                        return [pos, outra]

        # Se não sabe nada → joga duas aleatórias
        if len(posicoes_restantes) >= 2:
            return random.sample(posicoes_restantes, 2)
        else:
            return [] # Não há jogadas possíveis