import pygame
import sys
from instrucoes import exibir_instrucoes
pygame.init()



# Configuração da tela (tamanho da janela)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
background = pygame.image.load('Imagens/Jogo1.png')
background = pygame.transform.smoothscale(background, screen.get_size())

pygame.mixer.music.load('Audio/audio.mp3')
pygame.mixer.music.play(-1)
arcade_gamer_font = pygame.font.Font('Fontes/arcade_gamer.ttf', 85)
cor_texto = "#DF4B40"
texto_renderizado = arcade_gamer_font.render("JOGO DA", True, cor_texto)
texto_renderizado1 = arcade_gamer_font.render("MEMÓRIA", True, cor_texto)


imagem = pygame.image.load('Imagens/botao.png')
imagem_rect = imagem.get_rect()
imagem_rect.topleft = (600,550)

def abrir_instrucoes():
    exibir_instrucoes() 


# Loop principal do jogo
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
            



    # Blit da imagem de fundo na tela
    screen.blit(background, (0, 0))
    screen.blit(imagem, imagem_rect.topleft)
    screen.blit(texto_renderizado, (390,280))
    screen.blit(texto_renderizado1, (390,400))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()