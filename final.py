import pygame
import sys

def exibir_final(screen, nome_vencedor, avatar_vencedor_path):
    pygame.display.set_caption("Fim de Jogo!")

    largura_tela, altura_tela = screen.get_size()

  
    if nome_vencedor == "O melhor bot":
        caminho_background = 'Imagens/tela_derrota.png'
    elif nome_vencedor == "Empate!":
        caminho_background = 'Imagens/tela_empate.png'
    else:
        caminho_background = 'Imagens/parabens_final.png'

    
    try:
        background = pygame.image.load(caminho_background)
        background = pygame.transform.smoothscale(background, (largura_tela, altura_tela))
    except pygame.error:
        print(f"Erro ao carregar a imagem de fundo: {caminho_background}")
        background = pygame.Surface((largura_tela, altura_tela))
        background.fill((253, 246, 227))

    screen.blit(background, (0, 0))

   
    if nome_vencedor != "O melhor bot" and nome_vencedor != "Empate!":
        
        if avatar_vencedor_path:
            try:
                avatar_img = pygame.image.load(avatar_vencedor_path)
                tamanho_avatar = int(largura_tela * 0.18)
                avatar_img = pygame.transform.scale(avatar_img, (tamanho_avatar, tamanho_avatar))
                pos_avatar = (
                    int(largura_tela * 0.50) - avatar_img.get_width() // 2,
                    int(altura_tela * 0.5 + 40) - avatar_img.get_height() // 2
                )
                screen.blit(avatar_img, pos_avatar)
            except pygame.error:
                print(f"Erro ao carregar a imagem do avatar: {avatar_vencedor_path}")

        
        nome_fonte = pygame.font.Font('Fontes/arcade_gamer.ttf', int(altura_tela * 0.04))
        cor_texto = "#DF4B40"
        texto_nome = nome_fonte.render(nome_vencedor.upper(), True, cor_texto)
        texto_rect = texto_nome.get_rect(center=(largura_tela // 2, int(altura_tela * 0.825)))
        screen.blit(texto_nome, texto_rect)
    
    pygame.display.flip()


    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                esperando = False

    pygame.quit()
    sys.exit()