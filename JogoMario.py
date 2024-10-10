import pygame
import sys
import random
import time
import os
from final import exibir_final

def exibir_jogo_mario(screen):
    pygame.display.set_caption("Jogo da Memória do Mario")

    # Caminho para a pasta das cartas relativo ao diretório do script
    pasta_cartas = os.path.join(os.path.dirname(__file__), 'CartasMario')

    # Carregar todas as imagens da pasta das cartas
    imagens_cartas = []
    for filename in os.listdir(pasta_cartas):
        if filename.endswith('.png'):  # Verificar se o arquivo é uma imagem PNG
            imagem = pygame.image.load(os.path.join(pasta_cartas, filename))
            imagens_cartas.append(imagem)

    
    # Verificar se temos pelo menos 8 imagens
    if len(imagens_cartas) < 8:
        print("Erro: Deve haver pelo menos 8 imagens na pasta 'CartasMario'.")
        pygame.quit()
        sys.exit()

# Selecionar aleatoriamente 8 imagens se houver mais do que 8 disponíveis
    if len(imagens_cartas) > 8:
        imagens_cartas = random.sample(imagens_cartas, 8)


    # Carregar a imagem das costas das cartas
    costas_carta = pygame.image.load('CartasMario/costacartas.png')

    # Carregar a imagem de fundo
    imagem_fundo = pygame.image.load('Imagens/JogoMPZ.png')
    imagem_fundo = pygame.transform.smoothscale(imagem_fundo, screen.get_size())

    # Associar cada imagem a um identificador
    cartas_com_ids = list(enumerate(imagens_cartas))  # [(0, carta0), (1, carta1), ..., (7, carta7)]

    # Escolher aleatoriamente 4 cartas das 8 disponíveis
    cartas_escolhidas = random.sample(cartas_com_ids, 4)

    # Duplicar e embaralhar as cartas escolhidas
    cartas = cartas_escolhidas * 2
    random.shuffle(cartas)

    # Configurar o tamanho das cartas e do tabuleiro
    linhas, colunas = 2, 4  # Ajustado para um total de 8 cartas (2 linhas x 4 colunas)
    largura_tela, altura_tela = screen.get_size()

    # Definir largura fixa das cartas
    largura_carta_fixa = 250  # Ajuste esse valor conforme necessário
    altura_carta_fixa = int(largura_carta_fixa * costas_carta.get_height() / costas_carta.get_width())

    # Redimensionar as imagens das cartas e das costas das cartas
    cartas = [(id_carta, pygame.transform.smoothscale(carta, (largura_carta_fixa, altura_carta_fixa))) for id_carta, carta in cartas]
    costas_carta = pygame.transform.smoothscale(costas_carta, (largura_carta_fixa, altura_carta_fixa))

    # Espaçamento entre as cartas
    espaco_x = (largura_tela - (colunas * largura_carta_fixa)) // (colunas + 1)
    espaco_y = (altura_tela - (linhas * altura_carta_fixa)) // (linhas + 1)

    # Inicializar variáveis do jogo
    cartas_viradas = []
    cartas_acertadas = []
    start_time = time.time()

    # Função para desenhar o tabuleiro
    def desenhar_tabuleiro():
        screen.blit(imagem_fundo, (0, 0))
        for i in range(linhas):
            for j in range(colunas):
                index = i * colunas + j
                x = espaco_x + j * (largura_carta_fixa + espaco_x)
                y = espaco_y + i * (altura_carta_fixa + espaco_y)
                if index in cartas_acertadas or index in cartas_viradas:
                    screen.blit(cartas[index][1], (x, y))  # Exibe a carta
                else:
                    screen.blit(costas_carta, (x, y))  # Exibe o verso da carta

    # Loop principal do jogo
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
                        if cx <= x <= cx + largura_carta_fixa and cy <= y <= cy + altura_carta_fixa:
                            if index not in cartas_viradas and index not in cartas_acertadas:
                                cartas_viradas.append(index)
                                if len(cartas_viradas) == 2:
                                    desenhar_tabuleiro()
                                    pygame.display.flip()
                                    pygame.time.wait(1000)  # Aguarda um segundo para o jogador ver as cartas
                                    # Comparar os IDs das cartas para verificar se formam um par
                                    if cartas[cartas_viradas[0]][0] == cartas[cartas_viradas[1]][0]:
                                        cartas_acertadas.extend(cartas_viradas)  # Mantém as cartas viradas
                                    cartas_viradas = []

        desenhar_tabuleiro()
        pygame.display.flip()

        # Espera para mostrar as cartas
        esperar = True
                                
        if esperar:
        # Aguarda um segundo se as cartas não formarem um par
            pygame.time.wait(00)  # Altere o tempo conforme necessário

        # Verificar se o jogador ganhou
        if len(cartas_acertadas) == len(cartas):
            elapsed_time = time.time() - start_time
            print(f"Você ganhou! Tempo total: {elapsed_time:.2f} segundos")
            pygame.quit()
            sys.exit()

# Inicializar o jogo
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    exibir_jogo_mario(screen)