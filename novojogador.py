import pygame
import sys
from tema import exibir_tema

# Função para exibir a tela de novo jogador
def exibir_novojogador(screen):
    pygame.display.set_caption("Novo Jogador")

    # Carregar a imagem de fundo da tela "novojogador"
    background = pygame.image.load('Imagens/NovoJogador.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

    # Ajustar tamanho da fonte proporcionalmente à altura da tela
    tamanho_fonte = int(screen.get_height() * 0.04)
    caminho_fonte = 'Fontes/arcade_gamer.ttf'
    fonte = pygame.font.Font(caminho_fonte, tamanho_fonte)

    # Definir as cores das fontes
    cor_fonte_superior = "#DF4B40"

    # Texto centralizado na parte superior
    texto_superior = ("DIGITE O SEU NOME",
                      "E ESCOLHA SEU PERSONAGEM")

    # Função para renderizar o texto com quebras de linha
    def render_multiline(text, font, color):
        lines = text.split('\n')
        surfaces = [font.render(line, True, color) for line in lines]
        return surfaces

    texto_renderizado_superior = render_multiline('\n'.join(texto_superior), fonte, cor_fonte_superior)

    # Ajustar a posição vertical do texto com base na altura do texto renderizado
    altura_texto = sum(line.get_height() for line in texto_renderizado_superior)
    y_inicial = (screen.get_height() // 3 - 100) - (altura_texto // 3)  # Ajuste para subir o texto

    # Carregar imagens dos personagens com tamanho maior
    imagem_personagem1 = pygame.image.load('Imagens/personagem1.png')
    imagem_personagem1 = pygame.transform.smoothscale(imagem_personagem1, (350, 350))  # Ajuste o tamanho conforme necessário
    pos_personagem1 = (screen.get_width() // 2 - imagem_personagem1.get_width() // 2, screen.get_height() // 2 + 40 - imagem_personagem1.get_height() // 2)

    imagem_personagem2 = pygame.image.load('Imagens/personagem2.png')
    imagem_personagem2 = pygame.transform.smoothscale(imagem_personagem2, (350, 350))  # Ajuste o tamanho conforme necessário
    pos_personagem2 = (screen.get_width() // 2 - imagem_personagem2.get_width() // 2, screen.get_height() // 2 + 40 - imagem_personagem1.get_height() // 2)

    # Botão para ir para a tela "Tema"
    imagem_ins = pygame.image.load('Imagens/botaoIns.png')
    largura_botao = int(screen.get_width() * 0.15)
    altura_botao = int(screen.get_height() * 0.2)
    imagem_ins = pygame.transform.scale(imagem_ins, (largura_botao, altura_botao))
    imagem_ins_rect = imagem_ins.get_rect(center=(int(screen.get_width() * 0.85), int(screen.get_height() * 0.15)))

    # Caixa de entrada de texto
    caixa_input = pygame.Rect(screen.get_width() // 2 - 135, screen.get_height() // 3 + 418, 300, 50)  # Ajuste para descer a caixa de texto
    cor_caixa = "#feffd5"
    cor_caixa_foco = "#feffd5"
    texto_input = 'Insira seu nome aqui'
    input_ativo = False

    mostrar_personagem1 = True  # Flag para controlar qual personagem está sendo mostrado

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

                # Clicar no botão para ir para a tela "Tema"
                if imagem_ins_rect.collidepoint(event.pos):
                    nome_jogador = texto_input.strip()  # Obter o nome digitado (removendo espaços em branco extras)
                    exibir_tema(screen, nome_jogador)  # Chama a função exibir_tema para mostrar a tela "Tema" com o nome do jogador

                # Avançar para o próximo personagem ao clicar na tela
                mostrar_personagem1 = not mostrar_personagem1

            if event.type == pygame.KEYDOWN:
                if input_ativo:
                    if event.key == pygame.K_RETURN:
                        # Ao pressionar Enter, o texto digitado é armazenado
                        print(texto_input)  # Aqui você pode processar o nome digitado
                    elif event.key == pygame.K_BACKSPACE:
                        # Backspace para apagar caracteres
                        texto_input = texto_input[:-1]
                    else:
                        # Adiciona caracteres digitados ao texto
                        texto_input += event.unicode

        # Desenhar a imagem de fundo na tela
        screen.blit(background, (0, 0))
        screen.blit(imagem_ins, imagem_ins_rect.topleft)

        # Desenhar o texto centralizado na parte superior
        y_offset = y_inicial
        for line in texto_renderizado_superior:
            screen.blit(line, ((screen.get_width() - line.get_width()) // 2, y_offset))
            y_offset += line.get_height()

        # Desenhar o personagem atual na tela
        if mostrar_personagem1:
            screen.blit(imagem_personagem1, pos_personagem1)
        else:
            screen.blit(imagem_personagem2, pos_personagem2)

        # Desenhar a caixa de entrada de texto
        pygame.draw.rect(screen, cor_caixa if not input_ativo else cor_caixa_foco, caixa_input, 2)

        # Renderizar o texto digitado na caixa de texto com tamanho ajustado
        tamanho_fonte_caixa = int(tamanho_fonte * 0.4)  # Reduzir tamanho da fonte para a caixa de texto
        fonte_caixa = pygame.font.Font(caminho_fonte, tamanho_fonte_caixa)

        # Incluir "|" se o usuário estiver digitando
        texto_com_indicacao = texto_input
        if input_ativo:
            texto_com_indicacao += "|"

        texto_renderizado_input = fonte_caixa.render(texto_com_indicacao, True, "#41a8ad")
        screen.blit(texto_renderizado_input, (caixa_input.x + 10, caixa_input.y + 10))

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    exibir_novojogador(screen)
