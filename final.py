import pygame

def exibir_final(screen, nome_jogador, tempo_jogo):
    pygame.display.set_caption("Ranking")

    # Aqui você pode adicionar o código para exibir o ranking,
    # incluindo o nome do jogador e o tempo que ele levou para completar o jogo.
    # Exemplo:
    fonte = pygame.font.Font(None, 74)
    texto = f"Parabéns {nome_jogador}, seu tempo foi de {tempo_jogo:.2f} segundos!"
    texto_surface = fonte.render(texto, True, (255, 255, 255))
    screen.blit(texto_surface, (50, 50))
    pygame.display.flip()

    # Espera até que o jogador feche a janela
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperando = False

    pygame.quit()
