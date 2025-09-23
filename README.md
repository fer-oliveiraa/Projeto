# Jogo da Memória - Temas Mario, Pokémon e Zelda

Este projeto é um jogo da memória desenvolvido em Python usando a biblioteca Pygame. O jogador pode escolher entre três temas clássicos dos videogames: Mario, Pokémon e Zelda. O objetivo é encontrar todos os pares de cartas no menor tempo possível.

## Funcionalidades

- Tela inicial para digitar o nome do jogador e escolher o personagem
- Seleção de tema: Mario, Pokémon ou Zelda
- Jogo da memória com cartas personalizadas para cada tema
- Interface responsiva, ajustando elementos conforme o tamanho da tela
- Contagem de tempo para desafiar o jogador

## Como jogar

1. Execute o arquivo principal do projeto.
2. Digite seu nome e escolha seu personagem.
3. Selecione o tema desejado.
4. Encontre todos os pares de cartas clicando nas cartas para virá-las.
5. Tente terminar o jogo no menor tempo possível!

## Requisitos

- Python 3.x
- Pygame (`pip install pygame`)
- As pastas `Imagens`, `Fontes`, e as pastas de cartas de cada tema devem estar presentes no diretório do projeto.

## Estrutura de Pastas

```
Projeto/
├── Imagens/
│   ├── BotaoMario.png
│   ├── BotaoPokemon.png
│   ├── BotaoZelda.png
│   ├── tema_novoJ.png
│   ├── fundoT.png
│   └── ... (outras imagens)
├── Fontes/
│   └── arcade_gamer.ttf
├── CartasMario/
├── CartasPokemon/
├── CartasZelda/
├── JogoMario.py
├── JogoPokemon.py
├── JogoZelda.py
├── tema.py
├── novojogador.py
└── README.md
```

## Como executar

No terminal, navegue até a pasta do projeto e execute:

```
python novojogador.py
```

ou

```
python tema.py
```

## Créditos

Desenvolvido por Fernanda para o TCC.

Imagens e personagens são de propriedade de seus respectivos criadores (Nintendo, Game Freak, etc.) e são usadas apenas para fins educacionais.