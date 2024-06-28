import pygame
import sys
from tema import exibir_tema

def carregar_imagem(path, largura, altura):
    imagem = pygame.image.load(path)
    return pygame.transform.smoothscale(imagem, (largura, altura))

def render_multiline(text, font, color):
    lines = text.split('\n')
    surfaces = [font.render(line, True, color) for line in lines]
    return surfaces

def ajustar_elementos(screen):
    # Dimensões da tela
    largura_tela, altura_tela = screen.get_size()

    # Ajuste da fonte
    tamanho_fonte = int(altura_tela * 0.04)
    caminho_fonte = 'Fontes/arcade_gamer.ttf'
    fonte = pygame.font.Font(caminho_fonte, tamanho_fonte)
    fonte_caixa = pygame.font.Font(caminho_fonte, int(tamanho_fonte * 0.4))

    # Carregar e ajustar imagens
    background = carregar_imagem('Imagens/NovoJogador.png', largura_tela, altura_tela)
    imagem_personagem1 = carregar_imagem('Imagens/personagem1.png', 350, 350)
    imagem_personagem2 = carregar_imagem('Imagens/personagem2.png', 350, 350)
    imagem_ins = carregar_imagem('Imagens/botaoIns.png', int(largura_tela * 0.15), int(altura_tela * 0.2))

    # Posições dos elementos
    pos_personagem1 = (largura_tela // 2 - imagem_personagem1.get_width() // 2, altura_tela // 2 + 40 - imagem_personagem1.get_height() // 2)
    pos_personagem2 = (largura_tela // 2 - imagem_personagem2.get_width() // 2, altura_tela // 2 + 40 - imagem_personagem2.get_height() // 2)
    imagem_ins_rect = imagem_ins.get_rect(center=(int(largura_tela * 0.85), int(altura_tela * 0.15)))
    caixa_input = pygame.Rect(largura_tela // 2 - 135, altura_tela // 3 + 418, 300, 50)

    return {
        'background': background,
        'imagem_personagem1': imagem_personagem1,
        'imagem_personagem2': imagem_personagem2,
        'imagem_ins': imagem_ins,
        'pos_personagem1': pos_personagem1,
        'pos_personagem2': pos_personagem2,
        'imagem_ins_rect': imagem_ins_rect,
        'caixa_input': caixa_input,
        'fonte': fonte,
        'fonte_caixa': fonte_caixa
    }

def exibir_novojogador(screen):
    pygame.display.set_caption("Novo Jogador")

    elementos = ajustar_elementos(screen)
    background = elementos['background']
    imagem_personagem1 = elementos['imagem_personagem1']
    imagem_personagem2 = elementos['imagem_personagem2']
    imagem_ins = elementos['imagem_ins']
    pos_personagem1 = elementos['pos_personagem1']
    pos_personagem2 = elementos['pos_personagem2']
    imagem_ins_rect = elementos['imagem_ins_rect']
    caixa_input = elementos['caixa_input']
    fonte = elementos['fonte']
    fonte_caixa = elementos['fonte_caixa']

    # Definir as cores das fontes
    cor_fonte_superior = "#DF4B40"

    # Texto centralizado na parte superior
    texto_superior = ("DIGITE O SEU NOME",
                      "E ESCOLHA SEU PERSONAGEM")

    texto_renderizado_superior = render_multiline('\n'.join(texto_superior), fonte, cor_fonte_superior)

    altura_texto = sum(line.get_height() for line in texto_renderizado_superior)
    y_inicial = (screen.get_height() // 3 - 100) - (altura_texto // 3)

    cor_caixa = "#feffd5"
    cor_caixa_foco = "#feffd5"
    texto_input = 'Insira seu nome aqui'
    input_ativo = False
    mostrar_personagem1 = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if caixa_input.collidepoint(event.pos):
                    input_ativo = True
                else:
                    input_ativo = False

                if imagem_ins_rect.collidepoint(event.pos):
                    nome_jogador = texto_input.strip()
                    exibir_tema(screen, nome_jogador)

                mostrar_personagem1 = not mostrar_personagem1

            if event.type == pygame.KEYDOWN:
                if input_ativo:
                    if event.key == pygame.K_RETURN:
                        print(texto_input)
                    elif event.key == pygame.K_BACKSPACE:
                        texto_input = texto_input[:-1]
                    else:
                        texto_input += event.unicode

        screen.blit(background, (0, 0))
        screen.blit(imagem_ins, imagem_ins_rect.topleft)

        y_offset = y_inicial
        for line in texto_renderizado_superior:
            screen.blit(line, ((screen.get_width() - line.get_width()) // 2, y_offset))
            y_offset += line.get_height()

        if mostrar_personagem1:
            screen.blit(imagem_personagem1, pos_personagem1)
        else:
            screen.blit(imagem_personagem2, pos_personagem2)

        pygame.draw.rect(screen, cor_caixa if not input_ativo else cor_caixa_foco, caixa_input, 2)

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
