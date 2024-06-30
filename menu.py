import pygame
import sys
from instrucoes import exibir_instrucoes

# Inicialização do Pygame
pygame.init()

# Definir a cor do texto
cor_texto = "#DF4B40"

# Função para centralizar texto
def centralizar_texto(texto, fonte, cor, superficie, y):
    # Renderizar o texto com a fonte e cor fornecidas
    texto_renderizado = fonte.render(texto, True, cor)
    # Centralizar o texto na superfície fornecida na posição y
    texto_rect = texto_renderizado.get_rect(center=(superficie.get_width() / 2, y))
    return texto_renderizado, texto_rect

# Função para ajustar elementos na tela
def ajustar_elementos(screen):
    global arcade_gamer_font

    # Carregar e redimensionar a imagem de fundo para ajustar ao tamanho da tela
    background = pygame.image.load('Imagens/Menu.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    # Ajustar tamanho da fonte proporcionalmente à altura da tela
    tamanho_fonte = int(screen.get_height() * 0.1)
    arcade_gamer_font = pygame.font.Font('Fontes/arcade_gamer.ttf', tamanho_fonte)

    # Centralizar os textos "JOGO DA" e "MEMÓRIA"
    texto_renderizado, texto_rect = centralizar_texto("JOGO DA", arcade_gamer_font, cor_texto, screen, int(screen.get_height() * 0.4))
    texto_renderizado1, texto_rect1 = centralizar_texto("MEMÓRIA", arcade_gamer_font, cor_texto, screen, int(screen.get_height() * 0.5))

    # Carregar e redimensionar a imagem do botão
    imagem = pygame.image.load('Imagens/BotaoStart.png')
    imagem = pygame.transform.scale(imagem, (int(screen.get_width() * 0.1), int(screen.get_height() * 0.1)))
    imagem_rect = imagem.get_rect(center=(screen.get_width() / 2, int(screen.get_height() * 0.8)))

    return background, texto_renderizado, texto_renderizado1, imagem, imagem_rect, texto_rect, texto_rect1

# Configuração inicial da tela
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background, texto_renderizado, texto_renderizado1, imagem, imagem_rect, texto_rect, texto_rect1 = ajustar_elementos(screen)

# Carregar e reproduzir música de fundo
pygame.mixer.music.load('Audio/Audio1.mp3')
pygame.mixer.music.play(-1)

# Função para exibir instruções
def abrir_instrucoes():
    exibir_instrucoes()

# Loop principal do jogo
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Sair do loop principal
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if imagem_rect.collidepoint(mouse_pos):
                abrir_instrucoes()  # Abrir instruções se o botão for clicado
        if event.type == pygame.VIDEORESIZE:
            # Ajustar a tela e elementos ao redimensionar a janela
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background, texto_renderizado, texto_renderizado1, imagem, imagem_rect, texto_rect, texto_rect1 = ajustar_elementos(screen)

    # Desenhar a imagem de fundo na tela
    screen.blit(background, (0, 0))
    # Desenhar a imagem do botão na tela
    screen.blit(imagem, imagem_rect.topleft)
    # Desenhar os textos "JOGO DA" e "MEMÓRIA" na tela
    screen.blit(texto_renderizado, texto_rect.topleft)
    screen.blit(texto_renderizado1, texto_rect1.topleft)

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
sys.exit()
