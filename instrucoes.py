import pygame
import sys



def exibir_instrucoes():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Instruções")

    # Carregue a imagem de fundo da tela de instruções
    background = pygame.image.load('Imagens/Ins.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    # Titulo
    arcade_gamer_font = pygame.font.Font('Fontes/arcade_gamer.ttf', 40)
    cor_texto = "#DF4B40"
    titulo_renderizado = arcade_gamer_font.render("Instruções", True, cor_texto)
    texto_renderizado = arcade_gamer_font.render("",True, cor_texto)
    
    # Obtendo o retângulo envolvente do texto do título
    texto_rect = texto_renderizado.get_rect()
    # Ajustando a posição do retângulo para o centro da tela
    texto_rect.centerx = screen.get_rect().centerx
    texto_rect.y = 40  # Definindo a posição vertical

    # Texto
    nine_font = pygame.font.Font('Fontes/nine.ttf', 50)
    cor_texto = "#41A8AD"
    
    # Texto em parágrafos
    paragrafos = [
        "Bem-vindo ao jogo da memória!",
        "O objetivo é encontrar pares de cartas","idênticas no tabuleiro","virando duas cartas por vez.",
        "Quem encontrar mais pares vence.","Prepare sua memória e divirta-se!"
    ]
    
    # Renderizando cada parágrafo separadamente
    paragrafo_renderizado = []
    for i, paragrafo in enumerate(paragrafos):
        texto = nine_font.render(paragrafo, True, cor_texto)
        texto_rect = texto.get_rect()
        texto_rect.centerx = screen.get_rect().centerx
        texto_rect.y = 250 + i * 70 # Definindo a posição vertical para cada parágrafo
        paragrafo_renderizado.append((texto, texto_rect))


    imagem = pygame.image.load('Imagens/botaoIns.png')
    imagem_rect = imagem.get_rect()
    imagem_rect.topleft = (1100,100)

    
        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Blit da imagem de fundo e do texto na tela
        screen.blit(background, (0, 0))
        screen.blit(texto_renderizado, texto_rect)
        screen.blit(titulo_renderizado, (455,150))
        screen.blit(imagem, imagem_rect.topleft)
        
        # Renderizando e desenhando cada parágrafo na tela
        for texto, texto_rect in paragrafo_renderizado:
            screen.blit(texto, texto_rect)
            
        pygame.display.flip()

if __name__ == '__main__':
    exibir_instrucoes()
