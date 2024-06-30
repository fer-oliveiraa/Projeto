import pygame
import sys

def exibir_jogo_zelda(screen):
    pygame.display.set_caption("Jogo Zelda")

     # Carregar a imagem de fundo da tela "tema"
    background = pygame.image.load('Imagens/JogoMPZ.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    # Exemplo básico de loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background, (0, 0))
        # Lógica do jogo aqui
        # Desenhar na tela, atualizar estados, etc.

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    exibir_jogo_zelda(screen)