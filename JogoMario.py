import pygame
import sys
import random
import time
import os

def exibir_jogo_mario(screen):
    pygame.display.set_caption("Jogo da Memória Mario")

    # Caminho para a pasta das cartas relativo ao diretório do script
    pasta_cartas = os.path.join(os.path.dirname(__file__), 'CartasMario')

    # Carregar todas as imagens da pasta das cartas
    imagens_cartas = []
    for filename in os.listdir(pasta_cartas):
        if filename.endswith('.png'):  # Verificar se o arquivo é uma imagem PNG
            imagem = pygame.image.load(os.path.join(pasta_cartas, filename))
            imagens_cartas.append(imagem)

    if len(imagens_cartas) < 6:
        print("Erro: Deve haver pelo menos 6 imagens na pasta 'CartasMario'.")
        pygame.quit()
        sys.exit()

    imagens_cartas = random.sample(imagens_cartas, 6)
    costas_carta = pygame.image.load('CartasMario/costacartas.png')
    imagem_fundo = pygame.image.load('Imagens/JogoMPZ.png')
    imagem_fundo = pygame.transform.smoothscale(imagem_fundo, screen.get_size())

    cartas_com_ids = list(enumerate(imagens_cartas))
    cartas = cartas_com_ids * 2
    random.shuffle(cartas)

    linhas, colunas = 3, 4
    largura_tela, altura_tela = screen.get_size()
    largura_carta_fixa = 200
    altura_carta_fixa = int(largura_carta_fixa * costas_carta.get_height() / costas_carta.get_width())

    cartas = [(id_carta, pygame.transform.smoothscale(carta, (largura_carta_fixa, altura_carta_fixa))) for id_carta, carta in cartas]
    costas_carta = pygame.transform.smoothscale(costas_carta, (largura_carta_fixa, altura_carta_fixa))

    espaco_x = (largura_tela - (colunas * largura_carta_fixa)) // (colunas + 1)
    espaco_y = (altura_tela - (linhas * altura_carta_fixa)) // (linhas + 1)

    cartas_viradas = []
    cartas_acertadas = []
    pares_jogador = 0
    pares_bot = 0
    turno_jogador = True
    start_time = time.time()

    # Memória do bot
    memoria_bot = {}

    def desenhar_tabuleiro():
        screen.blit(imagem_fundo, (0, 0))
        for i in range(linhas):
            for j in range(colunas):
                index = i * colunas + j
                x = espaco_x + j * (largura_carta_fixa + espaco_x)
                y = espaco_y + i * (altura_carta_fixa + espaco_y)
                if index in cartas_acertadas or index in cartas_viradas:
                    screen.blit(cartas[index][1], (x, y))
                else:
                    screen.blit(costas_carta, (x, y))

    def jogada_bot():
        # Primeiro, verifique se a memória do bot tem um par conhecido
        for id_carta, indices in memoria_bot.items():
            if len(indices) == 2 and indices[0] not in cartas_acertadas and indices[1] not in cartas_acertadas:
                return indices[0], indices[1]

        # Se não tiver um par conhecido, vire uma carta da memória
        cartas_nao_viradas = [i for i in range(len(cartas)) if i not in cartas_viradas and i not in cartas_acertadas]
        carta1 = random.choice(cartas_nao_viradas)

        # Verifique se o bot lembra de uma carta correspondente
        id_carta1 = cartas[carta1][0]
        if id_carta1 in memoria_bot and len(memoria_bot[id_carta1]) == 1:
            return carta1, memoria_bot[id_carta1][0]

        # Se não lembrar, vire outra carta aleatória
        cartas_nao_viradas.remove(carta1)
        carta2 = random.choice(cartas_nao_viradas)

        return carta1, carta2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and turno_jogador:
                x, y = event.pos
                for i in range(linhas):
                    for j in range(colunas):
                        index = i * colunas + j
                        cx = espaco_x + j * (largura_carta_fixa + espaco_x)
                        cy = espaco_y + i * (altura_carta_fixa + espaco_y)
                        if cx <= x < cx + largura_carta_fixa and cy <= y < cy + altura_carta_fixa:
                            if index not in cartas_viradas and index not in cartas_acertadas:
                                cartas_viradas.append(index)
                                if len(cartas_viradas) == 2:
                                    desenhar_tabuleiro()
                                    pygame.display.flip()
                                    pygame.time.wait(1000)
                                    if cartas[cartas_viradas[0]][0] == cartas[cartas_viradas[1]][0]:
                                        cartas_acertadas.extend(cartas_viradas)
                                        pares_jogador += 1
                                    cartas_viradas = []
                                    turno_jogador = False

        if not turno_jogador and len(cartas_acertadas) < len(cartas):
            carta1, carta2 = jogada_bot()
            cartas_viradas.extend([carta1, carta2])
            desenhar_tabuleiro()
            pygame.display.flip()
            pygame.time.wait(800)
            if cartas[carta1][0] == cartas[carta2][0]:
                cartas_acertadas.extend([carta1, carta2])
                pares_bot += 1
            else:
                # Adicionar as cartas à memória do bot
                for carta in [carta1, carta2]:
                    id_carta = cartas[carta][0]
                    if id_carta not in memoria_bot:
                        memoria_bot[id_carta] = []
                    memoria_bot[id_carta].append(carta)

            cartas_viradas = []
            turno_jogador = True

        desenhar_tabuleiro()
        pygame.display.flip()

        if len(cartas_acertadas) == len(cartas):
            elapsed_time = time.time() - start_time
            vencedor = "Jogador" if pares_jogador > pares_bot else "Bot" if pares_bot > pares_jogador else "Empate"
            print(f"Fim do jogo! Tempo total: {elapsed_time:.2f} segundos")
            print(f"Jogador: {pares_jogador} pares | Bot: {pares_bot} pares")
            print(f"Vencedor: {vencedor}")
            pygame.quit()
            sys.exit()

# Inicializar o jogo
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    exibir_jogo_mario(screen)