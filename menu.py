import pygame
import sys
from instrucoes import exibir_instrucoes

pygame.init()

cor_texto = "#DF4B40"

def centralizar_texto(texto, fonte, cor, superficie, y):
    texto_renderizado = fonte.render(texto, True, cor)
    texto_rect = texto_renderizado.get_rect(center=(superficie.get_width() / 2, y))
    return texto_renderizado, texto_rect

def ajustar_elementos(screen):
    global arcade_gamer_font

    background = pygame.image.load('Imagens/Menu.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    tamanho_fonte = int(screen.get_height() * 0.1)
    arcade_gamer_font = pygame.font.Font('Fontes/arcade_gamer.ttf', tamanho_fonte)

    texto_renderizado, texto_rect = centralizar_texto("JOGO DA", arcade_gamer_font, cor_texto, screen, int(screen.get_height() * 0.4))
    texto_renderizado1, texto_rect1 = centralizar_texto("MEMÓRIA", arcade_gamer_font, cor_texto, screen, int(screen.get_height() * 0.5))

    imagem = pygame.image.load('Imagens/BotaoStart.png')
    imagem = pygame.transform.scale(imagem, (int(screen.get_width() * 0.1), int(screen.get_height() * 0.1)))
    imagem_rect = imagem.get_rect(center=(screen.get_width() / 2, int(screen.get_height() * 0.8)))

    return background, texto_renderizado, texto_renderizado1, imagem, imagem_rect, texto_rect, texto_rect1

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background, texto_renderizado, texto_renderizado1, imagem, imagem_rect, texto_rect, texto_rect1 = ajustar_elementos(screen)

pygame.mixer.music.load('Audio/Audio1.mp3')
pygame.mixer.music.play(-1)

def abrir_instrucoes():
    exibir_instrucoes()

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if imagem_rect.collidepoint(mouse_pos):
                abrir_instrucoes()
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background, texto_renderizado, texto_renderizado1, imagem, imagem_rect, texto_rect, texto_rect1 = ajustar_elementos(screen)

    screen.blit(background, (0, 0))
    screen.blit(imagem, imagem_rect.topleft)
    screen.blit(texto_renderizado, texto_rect.topleft)
    screen.blit(texto_renderizado1, texto_rect1.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
