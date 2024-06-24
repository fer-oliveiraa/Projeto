import pygame
import sys

def exibir_novojogador():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Novo Jogador")

    # Carregar a imagem de fundo da tela "novojogador"
    background = pygame.image.load('Imagens/NovoJogador.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    # Ajustar tamanho da fonte proporcionalmente à altura da tela
    tamanho_fonte = int(screen.get_height() * 0.1)
    fonte = pygame.font.Font(None, tamanho_fonte)

    # Texto de boas-vindas
    #texto = "Bem-vindo, Novo Jogador!"
    #texto_renderizado = fonte.render(texto, True, (255, 255, 255))  # Cor branca

    # Posicionamento do texto no centro da tela
    #texto_rect = texto_renderizado.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # Caixa de entrada de texto
    caixa_input = pygame.Rect(screen.get_width() // 2 - 150, screen.get_height() // 2 + 50, 300, 50)
    cor_caixa = (255, 255, 255)
    cor_caixa_foco = (200, 200, 200)
    texto_input = ''
    input_ativo = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro da caixa de texto
                if caixa_input.collidepoint(event.pos):
                    input_ativo = True
                else:
                    input_ativo = False
            elif event.type == pygame.KEYDOWN:
                if input_ativo:
                    if event.key == pygame.K_RETURN:
                        # Ao pressionar Enter, o texto digitado é armazenado
                        print(texto_input)  # Aqui você pode processar o nome digitado
                        texto_input = ''  # Limpa o texto após pressionar Enter
                    elif event.key == pygame.K_BACKSPACE:
                        # Backspace para apagar caracteres
                        texto_input = texto_input[:-1]
                    else:
                        # Adiciona caracteres digitados ao texto
                        texto_input += event.unicode

        # Desenhar a imagem de fundo na tela
        screen.blit(background, (0, 0))

        # Desenhar o texto no centro da tela
        #screen.blit(texto_renderizado, texto_rect)

        # Desenhar a caixa de entrada de texto
        pygame.draw.rect(screen, cor_caixa if not input_ativo else cor_caixa_foco, caixa_input, 2)

        # Renderizar o texto digitado na caixa de texto
        texto_renderizado_input = fonte.render(texto_input, True, (255, 255, 255))
        screen.blit(texto_renderizado_input, (caixa_input.x + 10, caixa_input.y + 10))

        pygame.display.flip()

if __name__ == '__main__':
    exibir_novojogador()
