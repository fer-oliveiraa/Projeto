import pygame
import sys
from tema import exibir_tema

# Função para carregar e redimensionar uma imagem
def carregar_imagem(path, largura, altura):
    imagem = pygame.image.load(path)
    return pygame.transform.smoothscale(imagem, (largura, altura))

# Função para renderizar texto multilinha
def render_multiline(text, font, color):
    lines = text.split('\n')
    surfaces = [font.render(line, True, color) for line in lines]
    return surfaces

# Função para ajustar elementos na tela
def ajustar_elementos(screen):
    largura_tela, altura_tela = screen.get_size()

    background = carregar_imagem('Imagens/tema_novojogador.png', largura_tela, altura_tela)

    # Ajuste da fonte
    tamanho_fonte = int(altura_tela * 0.04)
    caminho_fonte = 'Fontes/arcade_gamer.ttf'
    fonte = pygame.font.Font(caminho_fonte, tamanho_fonte)
    fonte_caixa = pygame.font.Font(caminho_fonte, int(tamanho_fonte * 0.4))

    # Carregar e ajustar imagens
    #background = carregar_imagem('Imagens/NovoJogador.png', largura_tela, altura_tela)
    tamanho_personagem = int(largura_tela * 0.18)  # Tamanho relativo ao tamanho da tela
    imagem_personagem1 = carregar_imagem('Imagens/personagem1.png', tamanho_personagem, tamanho_personagem)
    imagem_personagem2 = carregar_imagem('Imagens/personagem2.png', tamanho_personagem, tamanho_personagem)
    imagem_ins = carregar_imagem('Imagens/BotaoSeta.png', int(largura_tela * 0.15), int(altura_tela * 0.2))

    # Posições dos elementos (Centralizados horizontalmente e ajustados verticalmente)
    pos_personagem1 = (int(largura_tela * 0.50) - imagem_personagem1.get_width() // 2, int(altura_tela * 0.5 + 40) - imagem_personagem1.get_height() // 2)
    pos_personagem2 = (int(largura_tela * 0.50) - imagem_personagem2.get_width() // 2, int(altura_tela * 0.5 + 40) - imagem_personagem2.get_height() // 2)
    imagem_ins_rect = imagem_ins.get_rect(center=(int(largura_tela * 0.85), int(altura_tela * 0.15)))
    caixa_input = pygame.Rect(largura_tela // 2 - int(largura_tela * 0.07), int(altura_tela * 0.80), int(largura_tela * 0.3), int(altura_tela * 0.05))

    # Definir áreas de clique ao lado das imagens dos personagens, afastadas por n pixels
    distancia_afastamento = 60

    area_clique_esquerda = pygame.Rect(
        pos_personagem1[0] - distancia_afastamento - 65,  #largura da área de clique
        pos_personagem1[1],
        50,
        tamanho_personagem
    )

    area_clique_direita = pygame.Rect(
        pos_personagem1[0] + tamanho_personagem + distancia_afastamento,
        pos_personagem1[1],
        50,
        tamanho_personagem
    )

    return {
        'largura_tela': largura_tela,
        'altura_tela': altura_tela,
        'background': background,
        'imagem_personagem1': imagem_personagem1,
        'imagem_personagem2': imagem_personagem2,
        'imagem_ins': imagem_ins,
        'pos_personagem1': pos_personagem1,
        'pos_personagem2': pos_personagem2,
        'imagem_ins_rect': imagem_ins_rect,
        'caixa_input': caixa_input,
        'fonte': fonte,
        'fonte_caixa': fonte_caixa,
        'area_clique_esquerda': area_clique_esquerda,
        'area_clique_direita': area_clique_direita
    }

# Função principal para exibir a tela de novo jogador
def exibir_novojogador(screen):
    pygame.display.set_caption("Novo Jogador")

    elementos = ajustar_elementos(screen)
    largura_tela = elementos['largura_tela']
    altura_tela = elementos['altura_tela']
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
    area_clique_esquerda = elementos['area_clique_esquerda']
    area_clique_direita = elementos['area_clique_direita']

    cor_fonte_superior = "#DF4B40"

    texto_superior = (
        "DIGITE O SEU NOME",
        "E ESCOLHA SEU PERSONAGEM"
    )

    texto_renderizado_superior = render_multiline('\n'.join(texto_superior), fonte, cor_fonte_superior)

    altura_texto = sum(line.get_height() for line in texto_renderizado_superior)
    y_inicial = int(altura_tela * 0.15)

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

                # Verifica se o clique foi em uma das áreas de clique ao lado das imagens dos personagens
                if area_clique_esquerda.collidepoint(event.pos) or area_clique_direita.collidepoint(event.pos):
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

        # Mostra o personagem apropriado com base no valor de mostrar_personagem1
        if mostrar_personagem1:
            screen.blit(imagem_personagem1, pos_personagem1)
        else:
            screen.blit(imagem_personagem2, pos_personagem2)

        # Desenha a caixa de input de texto
        pygame.draw.rect(screen, cor_caixa if not input_ativo else cor_caixa_foco, caixa_input, 2)

        # Adiciona um indicador de cursor se a caixa de input estiver ativa
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
