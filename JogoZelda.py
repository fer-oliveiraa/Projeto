import pygame
import sys
import random
import time
import os

def exibir_jogo_zelda(screen):
    pygame.display.set_caption("Jogo da Memória de Zelda")

    pasta_cartas = os.path.join(os.path.dirname(__file__), 'CartasZelda')

    imagens_cartas = []
    for filename in os.listdir(pasta_cartas):
        if filename.endswith('.png') and filename != 'costacartas.png':
            imagem = pygame.image.load(os.path.join(pasta_cartas, filename))
            imagens_cartas.append(imagem)

    if len(imagens_cartas) < 6:
        print("Erro: Deve haver pelo menos 6 imagens na pasta 'CartasZelda'.")
        pygame.quit()
        sys.exit()

    imagens_cartas = random.sample(imagens_cartas, 6)
    costas_carta = pygame.image.load(os.path.join(pasta_cartas, 'costacartas.png'))
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
    start_time = time.time()

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                                    cartas_viradas = []

        desenhar_tabuleiro()
        pygame.display.flip()

        if len(cartas_acertadas) == len(cartas):
            elapsed_time = time.time() - start_time
            print(f"Você venceu! Tempo total: {elapsed_time:.2f} segundos")
            pygame.quit()
            sys.exit()
