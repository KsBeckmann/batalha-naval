import os
import random
from typing import Any
from tabuleiro import Tabuleiro
from navios import Navio

def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def posiciona_navio(tabuleiro: Tabuleiro, navio: Navio) -> None:
    print(f"Posicione o {navio.nome}({navio.tamanho}):")
    posicionou = False  
    while not posicionou:
        direcao_valida = False
        while not direcao_valida:
            direcao_input = input("Direcao(V/H): ")
            direcao = direcao_input.upper()
            if direcao != 'H' and direcao != 'V':
                print("Por favor, digite apenas V (vertical) ou H (horizontal).")
                continue
            direcao_valida = True
        
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
        
        posicionou = navio.posicionar(tabuleiro, linha, coluna, direcao)
        if not posicionou:
            print("Não foi possível posicionar o navio nessa posição. Tente novamente.")

def posiciona_navio_inimigo(tabuleiro: Tabuleiro, navio: Navio) -> None:
    posicionou = False
    while not posicionou:
        direcao = random.randint(1,2)
        if direcao == 1: direcao = 'V'
        else: direcao = 'H'
        coluna = chr(random.randint(65, 74))
        linha = random.randint(1, 10)
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
    print("Tabuleiro Jogador: ")
    print("Navios afundados: ", end="")
    if PA_afundado: print("Porta-Avioes(5) ", end="")
    if EN_afundado: print("Encouracado(4) ", end="")
    if CR_afundado: print("Cruzador(3) ", end="")
    if SU_afundado: print("Submarino(2) ", end="")
    if DE_afundado: print("Destroyer(1) ", end="")
    print("")
    print(tabuleiro_jogador)
    print("Tabuleiro Inimgo: ")
    print("Navios afundados: ", end="")
    if PA_inimigo_afundado: print("Porta-Avioes(5) ", end="")
    if EN_inimigo_afundado: print("Encouracado(4) ", end="")
    if CR_inimigo_afundado: print("Cruzador(3) ", end="")
    if SU_inimigo_afundado: print("Submarino(2) ", end="")
    if DE_inimigo_afundado: print("Destroyer(1) ", end="")
    print("")
    print(tabuleiro_inimigo)