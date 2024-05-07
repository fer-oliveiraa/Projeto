import pygame
import sys



def exibir_instrucoes():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Instruções")

    # Carregue a imagem de fundo da tela de instruções
    background = pygame.image.load('Inicial/Primeira.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    # Titulo
    arcade_gamer_font = pygame.font.Font('arcade_gamer.ttf', 51)
    cor_texto = "#DF4B40"
    titulo_renderizado = arcade_gamer_font.render("Instruções", True, cor_texto)
    texto_renderizado = arcade_gamer_font.render("",True, cor_texto)
    
    # Obtendo o retângulo envolvente do texto do título
    texto_rect = texto_renderizado.get_rect()
    # Ajustando a posição do retângulo para o centro da tela
    texto_rect.centerx = screen.get_rect().centerx
    texto_rect.y = 40  # Definindo a posição vertical

    # Texto
    nine_font = pygame.font.Font('nine.ttf', 50)
    cor_texto = "#41A8AD"
    
    # Texto em parágrafos
    paragrafos = [
        "Uno é um jogo de cartas simples e divertido jogado por 2 ou mais jogadores.","O objetivo é se livrar de todas as suas cartas primeiro.",
        "Cada jogador recebe 7 cartas e, em cada turno, eles jogam uma carta que", "combine com a carta no topo do monte por cor, número ou ação.",
        "As cartas de ação têm efeitos especiais, como inverter a direção do jogo, pular o", "próximo jogador ou fazer com que o próximo jogador compre cartas extras.",
        "O jogo continua até que alguém fique sem cartas, e esse jogador vence a rodada."
    ]
    
    # Renderizando cada parágrafo separadamente
    paragrafo_renderizado = []
    for i, paragrafo in enumerate(paragrafos):
        texto = nine_font.render(paragrafo, True, cor_texto)
        texto_rect = texto.get_rect()
        texto_rect.centerx = screen.get_rect().centerx
        texto_rect.y = 300 + i * 50 # Definindo a posição vertical para cada parágrafo
        paragrafo_renderizado.append((texto, texto_rect))


    imagem = pygame.image.load('Inicial/botaoIns.png')
    imagem_rect = imagem.get_rect()
    imagem_rect.topleft = (1500,800)

    
        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Blit da imagem de fundo e do texto na tela
        screen.blit(background, (0, 0))
        screen.blit(texto_renderizado, texto_rect)
        screen.blit(titulo_renderizado, (718,150))
        screen.blit(imagem, imagem_rect.topleft)
        
        # Renderizando e desenhando cada parágrafo na tela
        for texto, texto_rect in paragrafo_renderizado:
            screen.blit(texto, texto_rect)
            
        pygame.display.flip()

if __name__ == '__main__':
    exibir_instrucoes()
