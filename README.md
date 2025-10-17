# Jogo da Memória com Bot (Temas: Mario, Pokémon e Zelda)

## Descrição

Este projeto é uma implementação completa de um Jogo da Memória, desenvolvido em **Python** com a biblioteca **Pygame**. O grande diferencial é a inclusão de um adversário controlado por IA (um **Bot**) com memória configurável, tornando a jogabilidade mais desafiadora e dinâmica.

O jogador pode escolher entre três temas clássicos dos videogames — Mario, Pokémon e Zelda — e competir contra o Bot para ver quem encontra mais pares de cartas.

## Funcionalidades

-   **Interface Gráfica Completa:** O jogo possui um fluxo de telas bem definido, incluindo menu principal, instruções, seleção de jogador, escolha de tema e telas de resultado.
-   **Adversário com IA:** Jogue contra um Bot com memória de curto prazo que "aprende" com as jogadas (suas e dele) para tentar encontrar os pares.
-   **Três Temas Clássicos:**
    -   🍄 Super Mario Bros
    -   🔥 Pokémon
    -   🛡️ The Legend of Zelda
-   **Telas de Resultado Personalizadas:** Imagens únicas para vitória do jogador, vitória do bot e empate, exibindo o avatar escolhido.
-   **Personalização do Jogador:** Permite que o usuário digite seu nome e escolha entre dois avatares na tela de novo jogador.
-   **Design Responsivo:** Os elementos da interface se ajustam para preencher a tela, independentemente da resolução.
-   **Música e Depuração:** O jogo conta com música de fundo e exibe informações de depuração (como a memória do Bot) no terminal para análise.

## Tecnologias Utilizadas

-   **Python 3**
-   **Pygame**

## Como Executar

### Pré-requisitos

Antes de começar, certifique-se de que você tem o Python 3 e o Pygame instalados.

```bash
# Para instalar o Pygame, execute no seu terminal:
pip install pygame
```

## Iniciando o Jogo
1. Clone ou faça o download deste repositório.

2. Navegue até a pasta raiz do projeto (/Projeto/) pelo terminal.

3. Execute o arquivo menu.py, que é o ponto de entrada principal do jogo.

## Como Jogar
1. Na tela inicial, clique em START para ir para as instruções.

2. Na tela de instruções, clique na seta para avançar para a tela de seleção de jogador.

3. Digite seu nome, escolha seu avatar usando as setas na tela e clique na seta vermelha para continuar.

4. Escolha um dos três temas: Mario, Pokémon ou Zelda.

5. O jogo começará! Clique nas cartas para virá-las e encontrar os pares. Você e o Bot jogarão em turnos alternados.

6. O jogo termina quando todos os pares forem encontrados, exibindo o resultado da partida (vitória, derrota ou empate).


## Créditos
Desenvolvido por Fernanda Oliveira como parte do projeto de TCC.

Imagens, fontes e personagens são propriedade de seus respectivos criadores (Nintendo, Game Freak, etc.) e foram utilizadas apenas para fins educacionais e de demonstração.
