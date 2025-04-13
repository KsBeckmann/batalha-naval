# Batalha Naval

Este é um jogo de Batalha Naval implementado em Python utilizando interface de linha de comando (CLI). O jogo segue as regras clássicas de Batalha Naval com algumas funcionalidades adicionais, como sistema de escudos para os navios.

## Índice

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como jogar](#como-jogar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Implementação](#implementação)
  - [Classes principais](#classes-principais)
  - [Mecânicas do jogo](#mecânicas-do-jogo)
  - [Sistema de Escudos](#sistema-de-escudos)
  - [Efeitos Sonoros](#efeitos-sonoros)
- [Estrutura de Arquivos](#estrutura-de-arquivos)

## Requisitos

- Python 3.6 ou superior
- Pygame (para efeitos sonoros)

## Instalação

1. Instale as dependências:
   ```bash
   pip install pygame
   ```

## Como jogar

1. Execute o jogo:
   ```bash
   python3 run.py
   ```

2. Siga as instruções na tela:
   - Confirme se deseja iniciar o jogo com "Y"
   - Posicione seus navios informando a direção (V para vertical, H para horizontal), a coluna (A-J) e a linha (1-10)
   - Durante o jogo, escolha posições para atacar informando a coluna e a linha

3. Objetivo:
   - Afundar todos os navios do inimigo antes que ele afunde os seus

4. Navios disponíveis:
   - Porta-Aviões (5 espaços, representado por 'P')
   - Encouraçado (4 espaços, representado por 'E')
   - Cruzador (3 espaços, representado por 'C')
   - Submarino (2 espaços, representado por 'S')
   - Destroyer (1 espaço, representado por 'D')

5. Legenda do tabuleiro:
   - Espaço vazio: representa água
   - '~': representa um tiro na água
   - 'X': representa um tiro que acertou um navio
   - 'P', 'E', 'C', 'S', 'D': representam os navios no tabuleiro do jogador

## Estrutura do Projeto

O projeto está organizado nos seguintes módulos:

- `run.py`: Ponto de entrada do programa
- `main.py`: Controla o fluxo principal do jogo
- `tabuleiro.py`: Define as classes do tabuleiro e sua visualização
- `navios.py`: Define as classes dos diferentes tipos de navios
- `posicao.py`: Gerencia a conversão de coordenadas
- `utils.py`: Funções auxiliares para o jogo
- `audio.py`: Gerencia os efeitos sonoros

## Implementação

### Classes principais

#### Tabuleiro
O jogo utiliza duas classes de tabuleiro que herdam da classe base `Tabuleiro`:

1. `TabuleiroJogador`: Mostra todos os detalhes, incluindo as posições dos navios do jogador.
2. `TabuleiroInimigo`: Mostra apenas os tiros acertados ('X') e errados ('~'), ocultando as posições dos navios do inimigo.

Ambas as classes utilizam uma matriz de caracteres para representar o estado do jogo.

#### Navios
O jogo implementa cinco tipos de navios que herdam da classe base `Navio`:

1. `PortaAvioes`: Ocupa 5 espaços e tem 10% de chance de escudo
2. `Encouracado`: Ocupa 4 espaços e tem 20% de chance de escudo
3. `Cruzador`: Ocupa 3 espaços e tem 30% de chance de escudo
4. `Submarino`: Ocupa 2 espaços e tem 40% de chance de escudo
5. `Destroyer`: Ocupa 1 espaço e tem 50% de chance de escudo

#### Posição
A classe `PosicaoBarco` gerencia a conversão entre a notação do jogo (ex: A1, B2) e os índices da matriz (0,0), (1,1).

### Mecânicas do jogo

1. **Fase de posicionamento**:
   - O jogador posiciona seus navios informando direção, coluna e linha
   - O computador posiciona seus navios aleatoriamente

2. **Fase de jogo**:
   - Os jogadores alternam turnos para atirar em posições do tabuleiro adversário
   - A cada tiro é verificado se acertou água ou um navio
   - Se acertar um navio, é verificado se o escudo do navio está ativo

3. **Condições de vitória/derrota**:
   - O jogador vence se afundar todos os navios do inimigo
   - O jogador perde se todos os seus navios forem afundados

### Sistema de Escudos

Cada tipo de navio tem uma chance diferente de ativar seu escudo quando atingido:
- Porta-Aviões: 10% de chance
- Encouraçado: 20% de chance
- Cruzador: 30% de chance
- Submarino: 40% de chance
- Destroyer: 50% de chance

Quando o escudo é ativado, o navio não recebe dano naquela posição naquele turno.

### Efeitos Sonoros

O jogo utiliza a biblioteca Pygame para reproduzir efeitos sonoros durante o jogo:
- Som de tiro ao disparar
- Som de acerto quando um navio é atingido
- Som de erro quando o tiro cai na água
- Som de escudo quando um escudo é ativado

## Estrutura de Arquivos

```
batalha-naval/
├── run.py             # Ponto de entrada do programa
├── main.py            # Controle principal do jogo
├── tabuleiro.py       # Classes de tabuleiro
├── navios.py          # Classes dos navios
├── posicao.py         # Classe para gerenciar posições
├── utils.py           # Funções auxiliares
├── audio.py           # Gerenciamento de áudio
├── README.md          # Este arquivo
└── sons/              # Pasta com os arquivos de áudio
    ├── acerto.mp3
    ├── erro.mp3
    ├── escudo.mp3
    └── tiro.mp3
```

Este projeto demonstra conceitos importantes de programação orientada a objetos em Python, como herança, encapsulamento e abstração, além de implementar um jogo clássico com uma interface de linha de comando intuitiva.

# EU E MEUS MANOS NÃO FECHAMOS COM INTERFACE GRÁFICA