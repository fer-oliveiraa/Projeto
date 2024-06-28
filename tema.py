import pygame
import sys

def exibir_tema(screen, nome_jogador):
    pygame.display.set_caption("Tema")

    # Carregar a imagem de fundo da tela "tema"
    background = pygame.image.load('Imagens/tema.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    # Ajustar tamanho da fonte proporcionalmente à altura da tela
    tamanho_fonte = int(screen.get_height() * 0.04)  # Ajuste para 4% da altura da tela
    caminho_fonte = 'Fontes/arcade_gamer.ttf'
    fonte = pygame.font.Font(caminho_fonte, tamanho_fonte)

    # Definir as cores das fontes
    cor_fonte_superior = "#DF4B40"

    # Texto centralizado na parte superior
    texto_superior = (f"JOGADOR(A) {nome_jogador.upper()} ESCOLHA QUAL ",
                      "TEMA MAIS CHAMA SUA ATENÇÃO",
                      "E SE PREPARE PARA INICIAR O JOGO")

    # Função para renderizar o texto com quebras de linha
    def render_multiline(text, font, color):
        lines = text.split('\n')
        surfaces = [font.render(line, True, color) for line in lines]
        return surfaces

    texto_renderizado_superior = render_multiline('\n'.join(texto_superior), fonte, cor_fonte_superior)

    # Ajustar a posição vertical do texto com base na altura do texto renderizado
    altura_texto = sum(line.get_height() for line in texto_renderizado_superior)
    y_inicial = (screen.get_height() // 3 - 100) - (altura_texto // 3)  # Ajuste para subir o texto

    # Botão para iniciar o jogo
    imagem_iniciar = pygame.image.load('Imagens/botaoIns.png')
    largura_botao = int(screen.get_width() * 0.15)
    altura_botao = int(screen.get_height() * 0.2)
    imagem_iniciar = pygame.transform.scale(imagem_iniciar, (largura_botao, altura_botao))
    imagem_iniciar_rect = imagem_iniciar.get_rect(center=(int(screen.get_width() * 0.85), int(screen.get_height() * 0.85)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi dentro do botão para iniciar o jogo
                if imagem_iniciar_rect.collidepoint(event.pos):
                    print("Iniciar jogo com o tema selecionado")  # Aqui você pode adicionar a lógica para iniciar o jogo

        # Desenhar a imagem de fundo na tela
        screen.blit(background, (0, 0))
        screen.blit(imagem_iniciar, imagem_iniciar_rect.topleft)

        # Desenhar o texto centralizado na parte superior
        y_offset = y_inicial
        for line in texto_renderizado_superior:
            screen.blit(line, ((screen.get_width() - line.get_width()) // 2, y_offset))
            y_offset += line.get_height()

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    exibir_tema(screen, "Nome Jogador")
