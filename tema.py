import pygame
import sys
from JogoMario import exibir_jogo_mario
from JogoPokemon import exibir_jogo_pokemon
from JogoZelda import exibir_jogo_zelda


def exibir_tema(screen, nome_jogador, avatar_path):
    pygame.display.set_caption("Tema")

    
    background = pygame.image.load('Imagens/tema_tema.png')
    background = pygame.transform.smoothscale(background, screen.get_size())

   
    tamanho_fonte = int(screen.get_height() * 0.04)
    caminho_fonte = 'Fontes/arcade_gamer.ttf'
    fonte = pygame.font.Font(caminho_fonte, tamanho_fonte)

    
    cor_fonte_superior = "#DF4B40"

    texto_superior = (
        f"{nome_jogador.upper()} ESCOLHA QUAL ",
        "TEMA CHAMA MAIS A SUA ATENÇÃO, ",
        "E SE PREPARE PARA INICIAR O JOGO"
    )

    def render_multiline(text, font, color):
        lines = text.split('\n')
        surfaces = [font.render(line, True, color) for line in lines]
        return surfaces

    texto_renderizado_superior = render_multiline('\n'.join(texto_superior), fonte, cor_fonte_superior)

  
    altura_tela = screen.get_height()
    tamanho_imagem = int(altura_tela * 0.10)

    imagem1 = pygame.image.load('Imagens/BotaoMario.png')
    imagem2 = pygame.image.load('Imagens/BotaoPokemon.png')
    imagem3 = pygame.image.load('Imagens/BotaoZelda.png')


    largura_original1, altura_original1 = imagem1.get_size()
    proporcao1 = tamanho_imagem / altura_original1
    largura_nova1 = int(largura_original1 * proporcao1)
    imagem1 = pygame.transform.scale(imagem1, (largura_nova1, tamanho_imagem))

    largura_original2, altura_original2 = imagem2.get_size()
    proporcao2 = tamanho_imagem / altura_original2
    largura_nova2 = int(largura_original2 * proporcao2)
    imagem2 = pygame.transform.scale(imagem2, (largura_nova2, tamanho_imagem))

    largura_original3, altura_original3 = imagem3.get_size()
    proporcao3 = tamanho_imagem / altura_original3
    largura_nova3 = int(largura_original3 * proporcao3)
    imagem3 = pygame.transform.scale(imagem3, (largura_nova3, tamanho_imagem))

    
    espacamento_vertical = int(altura_tela * 0.17)
    y_inicial = (screen.get_height() // 3 - 100) - (sum(line.get_height() for line in texto_renderizado_superior) // 3)

    largura_botao = largura_nova1
    altura_botao = tamanho_imagem

    pos_imagem1 = pygame.Rect((screen.get_width() - largura_botao) // 2 - largura_botao - int(screen.get_width() * 0.05), y_inicial + sum(line.get_height() for line in texto_renderizado_superior) + espacamento_vertical, largura_botao, altura_botao)
    pos_imagem2 = pygame.Rect((screen.get_width() - largura_botao) // 2, y_inicial + sum(line.get_height() for line in texto_renderizado_superior) + espacamento_vertical, largura_botao, altura_botao)
    pos_imagem3 = pygame.Rect((screen.get_width() - largura_botao) // 2 + largura_botao + int(screen.get_width() * 0.05), y_inicial + sum(line.get_height() for line in texto_renderizado_superior) + espacamento_vertical, largura_botao, altura_botao)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                if pos_imagem1.collidepoint(event.pos):
                    exibir_jogo_mario(screen, nome_jogador, avatar_path)
                if pos_imagem2.collidepoint(event.pos):
                    exibir_jogo_pokemon(screen, nome_jogador, avatar_path)
                if pos_imagem3.collidepoint(event.pos):
                    exibir_jogo_zelda(screen, nome_jogador, avatar_path)

        screen.blit(background, (0, 0))
        screen.blit(imagem1, pos_imagem1.topleft)
        screen.blit(imagem2, pos_imagem2.topleft)
        screen.blit(imagem3, pos_imagem3.topleft)

        y_offset = y_inicial
        for line in texto_renderizado_superior:
            screen.blit(line, ((screen.get_width() - line.get_width()) // 2, y_offset))
            y_offset += line.get_height()

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    exibir_tema(screen, "Jogador Teste", "Imagens/personagem1.png")