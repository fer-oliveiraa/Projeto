import pygame
import sys
import random
import time
import os
from bot_memoria import BotMemoria

def exibir_jogo_pokemon(screen):
    pygame.display.set_caption("Jogo Pokémon")

    pasta_cartas = os.path.join(os.path.dirname(__file__), 'CartasPokemon')

    # Altera a forma de carregar as imagens para manter o nome do arquivo
    imagens_cartas_com_nomes = []
    for filename in os.listdir(pasta_cartas):
        if filename.endswith('.png') and 'costacartas' not in filename:
            imagem = pygame.image.load(os.path.join(pasta_cartas, filename))
            imagens_cartas_com_nomes.append((filename, imagem))

    if len(imagens_cartas_com_nomes) < 6:
        print("Erro: Deve haver pelo menos 6 imagens na pasta 'CartasPokemon' (sem contar 'costacartas.png').")
        pygame.quit()
        sys.exit()

    # Seleciona 6 pares (nome do arquivo, imagem) aleatórios
    imagens_selecionadas = random.sample(imagens_cartas_com_nomes, 6)
    
    background = pygame.image.load('Imagens/fundoT.png')
    background = pygame.transform.smoothscale(background, screen.get_size())
    costas_carta = pygame.image.load(os.path.join(pasta_cartas, 'costacartas.png'))

    # Associa um ID a cada par (nome do arquivo, imagem)
    cartas_com_ids = list(enumerate(imagens_selecionadas))
    
    # Imprime o mapeamento de ID para nome da carta no terminal
    print("--- Mapeamento de Cartas da Partida ---")
    for id_carta, (nome_arquivo, _) in cartas_com_ids:
        print(f"ID {id_carta} -> {nome_arquivo}")
    print("------------------------------------")

    # Extrai apenas as imagens para a lista de cartas do jogo
    imagens_para_jogo = [img for _, (_, img) in cartas_com_ids]
    cartas_para_duplicar = list(enumerate(imagens_para_jogo))

    cartas = cartas_para_duplicar * 2
    random.shuffle(cartas)

    linhas, colunas = 3, 4
    largura_tela, altura_tela = screen.get_size()
    largura_carta_fixa = 200
    altura_carta_fixa = int(largura_carta_fixa * costas_carta.get_height() / costas_carta.get_width())

    cartas = [(id_carta, pygame.transform.smoothscale(carta, (largura_carta_fixa, altura_carta_fixa))) for id_carta, carta in cartas]
    costas_carta = pygame.transform.smoothscale(costas_carta, (largura_carta_fixa, altura_carta_fixa))

    espaco_x = (largura_tela - (colunas * largura_carta_fixa)) // (colunas + 1)
    espaco_y = (altura_tela - (linhas * altura_carta_fixa)) // (linhas + 1)

    # --- Variáveis de estado do jogo ---
    cartas_viradas = []
    cartas_acertadas = []
    pares_jogador = 0
    pares_bot = 0
    turno_jogador = True
    bot = BotMemoria(tamanho_memoria=4)
    start_time = time.time()

    def desenhar_tabuleiro():
        screen.blit(background, (0, 0))
        for i in range(linhas):
            for j in range(colunas):
                index = i * colunas + j
                x = espaco_x + j * (largura_carta_fixa + espaco_x)
                y = espaco_y + i * (altura_carta_fixa + espaco_y)
                if index in cartas_acertadas or index in cartas_viradas:
                    screen.blit(cartas[index][1], (x, y))
                else:
                    screen.blit(costas_carta, (x, y))
        fonte_placar = pygame.font.Font('Fontes/arcade_gamer.ttf', 30)
        placar_jogador = fonte_placar.render(f"Jogador: {pares_jogador}", True, (255,255,255))
        placar_bot = fonte_placar.render(f"Bot: {pares_bot}", True, (255,255,255))
        screen.blit(placar_jogador, (20, 20))
        screen.blit(placar_bot, (largura_tela - placar_bot.get_width() - 20, 20))


    # Loop principal do jogo
    while True:
        if turno_jogador:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if len(cartas_viradas) < 2:
                        x, y = event.pos
                        for i in range(linhas):
                            for j in range(colunas):
                                index = i * colunas + j
                                cx = espaco_x + j * (largura_carta_fixa + espaco_x)
                                cy = espaco_y + i * (altura_carta_fixa + espaco_y)
                                if cx <= x <= cx + largura_carta_fixa and cy <= y <= cy + altura_carta_fixa:
                                    if index not in cartas_viradas and index not in cartas_acertadas:
                                        cartas_viradas.append(index)
        else: # Vez do bot
            pygame.time.wait(1000)
            posicoes_restantes = [i for i in range(len(cartas)) if i not in cartas_acertadas]
            jogada_bot = bot.escolher_jogada(posicoes_restantes)
            if jogada_bot:
                cartas_viradas.extend(jogada_bot)

        if len(cartas_viradas) == 2:
            desenhar_tabuleiro()
            pygame.display.flip()
            
            id_carta1 = cartas[cartas_viradas[0]][0]
            pos_carta1 = cartas_viradas[0]
            id_carta2 = cartas[cartas_viradas[1]][0]
            pos_carta2 = cartas_viradas[1]
            
            bot.atualizar_memoria(id_carta1, pos_carta1)
            bot.atualizar_memoria(id_carta2, pos_carta2)

            print(f"Memória do Bot: {bot.memoria}")

            pygame.time.wait(1000)
            
            if id_carta1 == id_carta2:
                cartas_acertadas.extend(cartas_viradas)
                if turno_jogador:
                    pares_jogador += 1
                else:
                    pares_bot += 1
                
                bot.remover_par_da_memoria(id_carta1)

            turno_jogador = not turno_jogador
            cartas_viradas = []

        desenhar_tabuleiro()
        pygame.display.flip()

        if len(cartas_acertadas) == len(cartas):
            elapsed_time = time.time() - start_time
            print(f"Você venceu! Tempo total: {elapsed_time:.2f} segundos")
            print(f"Jogador: {pares_jogador} pares")
            print(f"Bot: {pares_bot} pares")
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    exibir_jogo_pokemon(screen)