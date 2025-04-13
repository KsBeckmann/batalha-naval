import os
import random
from typing import Any
from tabuleiro import Tabuleiro
from navios import Navio

def limpar_tela() -> None:
    """
    Limpa o terminal/console.
    Usa 'cls' no Windows e 'clear' em sistemas Unix/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def posiciona_navio(tabuleiro: Tabuleiro, navio: Navio) -> None:
    """
    Função para posicionar um navio no tabuleiro com entrada do usuário.
    
    Args:
        tabuleiro: O tabuleiro onde o navio será posicionado
        navio: O navio a ser posicionado
    """
    print(f"Posicione o {navio.nome}({navio.tamanho}):")
    posicionou = False  
    while not posicionou:
        # Solicita a direção do navio (vertical ou horizontal)
        direcao_valida = False
        while not direcao_valida:
            direcao_input = input("Direcao(V/H): ")
            direcao = direcao_input.upper()
            if direcao != 'H' and direcao != 'V':
                print("Por favor, digite apenas V (vertical) ou H (horizontal).")
                continue
            direcao_valida = True
        
        # Solicita a coluna (A-J)
        coluna_valida = False
        while not coluna_valida:
            coluna_input = input("Coluna (A-J): ")
            if len(coluna_input) != 1:
                print("Por favor, digite apenas uma letra.")
                continue
            coluna = coluna_input.upper()
            if coluna < 'A' or coluna > 'J':
                print("Por favor, digite uma letra entre A e J.")
                continue
            coluna_valida = True
        
        # Solicita a linha (1-10)
        linha_valida = False
        while not linha_valida:
            try:
                linha = int(input("Linha (1-10): "))
                if linha < 1 or linha > 10:
                    print("Por favor, digite um número entre 1 e 10.")
                    continue
                linha_valida = True
            except ValueError:
                print("Por favor, digite um número válido.")
                continue
        
        # Tenta posicionar o navio
        posicionou = navio.posicionar(tabuleiro, linha, coluna, direcao)
        if not posicionou:
            print("Não foi possível posicionar o navio nessa posição. Tente novamente.")

def posiciona_navio_inimigo(tabuleiro: Tabuleiro, navio: Navio) -> None:
    """
    Função para posicionar automaticamente um navio no tabuleiro inimigo.
    
    Args:
        tabuleiro: O tabuleiro onde o navio será posicionado
        navio: O navio a ser posicionado
    """
    posicionou = False
    while not posicionou:
        # Gera direção aleatória
        direcao = random.randint(1,2)
        if direcao == 1: direcao = 'V'
        else: direcao = 'H'
        
        # Gera posição aleatória (A-J, 1-10)
        coluna = chr(random.randint(65, 74))  # ASCII: A=65, J=74
        linha = random.randint(1, 10)
        
        # Tenta posicionar o navio
        posicionou = navio.posicionar(tabuleiro, linha, coluna, direcao)

def print_tabuleiros(tabuleiro_jogador, 
                    tabuleiro_inimigo,
                    PA_afundado: bool, 
                    EN_afundado: bool, 
                    CR_afundado: bool, 
                    SU_afundado: bool, 
                    DE_afundado: bool,
                    PA_inimigo_afundado: bool, 
                    EN_inimigo_afundado: bool, 
                    CR_inimigo_afundado: bool, 
                    SU_inimigo_afundado: bool, 
                    DE_inimigo_afundado: bool) -> None:
    """
    Exibe os tabuleiros do jogador e do inimigo, junto com o status de navios afundados.
    
    Args:
        tabuleiro_jogador: Tabuleiro do jogador
        tabuleiro_inimigo: Tabuleiro do inimigo
        PA_afundado, EN_afundado, etc.: Status de afundamento dos navios do jogador
        PA_inimigo_afundado, EN_inimigo_afundado, etc.: Status de afundamento dos navios do inimigo
    """
    # Exibe o tabuleiro do jogador e navios afundados
    print("Tabuleiro Jogador: ")
    print("Navios afundados: ", end="")
    if PA_afundado: print("Porta-Avioes(5) ", end="")
    if EN_afundado: print("Encouracado(4) ", end="")
    if CR_afundado: print("Cruzador(3) ", end="")
    if SU_afundado: print("Submarino(2) ", end="")
    if DE_afundado: print("Destroyer(1) ", end="")
    print("")
    print(tabuleiro_jogador)
    
    # Exibe o tabuleiro do inimigo e navios afundados
    print("Tabuleiro Inimgo: ")
    print("Navios afundados: ", end="")
    if PA_inimigo_afundado: print("Porta-Avioes(5) ", end="")
    if EN_inimigo_afundado: print("Encouracado(4) ", end="")
    if CR_inimigo_afundado: print("Cruzador(3) ", end="")
    if SU_inimigo_afundado: print("Submarino(2) ", end="")
    if DE_inimigo_afundado: print("Destroyer(1) ", end="")
    print("")
    print(tabuleiro_inimigo)