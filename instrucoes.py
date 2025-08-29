import pygame
import sys
from novojogador import exibir_novojogador 

def exibir_instrucoes():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Instruções")

    # Carregar a imagem de fundo da tela de instruções
    background = pygame.image.load('Imagens/Instrucoes.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    # Ajustar tamanho da fonte proporcionalmente à altura da tela
    tamanho_titulo_fonte = int(screen.get_height() * 0.08)  # Ajuste o valor conforme necessário
    tamanho_texto_fonte = int(screen.get_height() * 0.05)   # Ajuste o valor conforme necessário

    # Fonte e cor do título
    arcade_gamer_font = pygame.font.Font('Fontes/arcade_gamer.ttf', tamanho_titulo_fonte)
    cor_texto_titulo = "#DF4B40"
    titulo_renderizado = arcade_gamer_font.render("Instruções", True, cor_texto_titulo)

    # Fonte e cor do texto
    nine_font = pygame.font.Font('Fontes/nine.ttf', tamanho_texto_fonte)
    cor_texto = "#41A8AD"

    # Texto de instruções com quebras de linha
    texto_instrucoes = (
        "Bem-vindo ao Jogo da Memória! Neste jogo o seu objetivo é encontrar pares\n"
        "de cartas idênticas escondidas em um tabuleiro, virando duas cartas por\n"
        "vez. Mas aqui há um diferencial: você jogará contra um bot!\n"
        "Ambos irão alternar turnos tentando lembrar e descobrir as posições das\n"
        "cartas. Ao final, quem encontrar mais pares será o grande vencedor.\n"
        "Prepare sua memória, concentre-se bem e divirta-se nessa disputa\n"
        "inteligente!\n"
    )

    # Renderizar o título centralizado
    titulo_rect = titulo_renderizado.get_rect(center=(screen.get_width() // 2, int(screen.get_height() * 0.1)))

    # Função para renderizar o texto com quebras de linha alinhado à esquerda e centralizado horizontalmente
    def renderizar_texto_multilinha(texto, fonte, cor, superficie, pos_inicial_y):
        linhas = texto.split('\n')
        y_offset = pos_inicial_y
        renderizacoes = []
        for linha in linhas:
            renderizado = fonte.render(linha, True, cor)
            rect = renderizado.get_rect(left=50, top=y_offset)  # Alinhar à esquerda com margem de 50 pixels
            renderizacoes.append((renderizado, rect))
            y_offset += rect.height + 10  # Adiciona um pequeno espaçamento entre linhas
        return renderizacoes

    # Renderizar o texto de instruções com quebras de linha alinhado à esquerda
    texto_renderizado = renderizar_texto_multilinha(texto_instrucoes, nine_font, cor_texto, screen, int(screen.get_height() * 0.4))

    # Carregar e redimensionar a imagem do botão
    imagem = pygame.image.load('Imagens/BotaoSeta.png')
    largura_botao = int(screen.get_width() * 0.15)
    altura_botao = int(screen.get_height() * 0.2)
    imagem = pygame.transform.scale(imagem, (largura_botao, altura_botao))
    imagem_rect = imagem.get_rect(center=(int(screen.get_width() * 0.85), int(screen.get_height() * 0.15)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi no botão
                if imagem_rect.collidepoint(event.pos):
                    exibir_novojogador(screen)  # Passar a tela screen como argumento

        # Blit da imagem de fundo e do texto na tela
        screen.blit(background, (0, 0))
        screen.blit(titulo_renderizado, titulo_rect)
        screen.blit(imagem, imagem_rect.topleft)

        # Renderizando e desenhando cada linha do texto na tela
        for linha, rect in texto_renderizado:
            screen.blit(linha, rect)
            
        pygame.display.flip()

if __name__ == '__main__':
    exibir_instrucoes()
