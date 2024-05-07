'''''''''
screen = pygame.display.set_mode((800, 600))
background_rect = background.get_rect()   Tela menor para ajustes 
background_rect.center = screen.get_rect().center
screen.blit(background, background_rect.topleft)
''''''''' #Isso e para ajustes da tela 



"Uno é um jogo de cartas simples e divertido jogado por 2 ou mais jogadores. O objetivo é se livrar de todas as suas cartas primeiro.\n\n"
                                         
        "Cada jogador recebe 7 cartas e, em cada turno, eles jogam uma carta que combine com a carta no topo do monte por cor, número ou ação.\n\n" 

        "\nAs cartas de ação têm efeitos especiais, como inverter a direção do jogo, pular o próximo jogador ou fazer com que o próximo jogador compre cartas extras.\n\n"

        "\n O jogo continua até que alguém fique sem cartas, e esse jogador vence a rodada."