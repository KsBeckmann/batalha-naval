import os
import random

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def posiciona_navio(tabuleiro, navio):
    print(f"Posicione o {navio.nome}:")
    posicionou = False  
    while not posicionou:
        direcao = input("Direcao(V/H): ")
        direcao = direcao.upper()
        if direcao != 'H' and direcao.upper() != 'V':
            continue    
        try: coluna = input("Coluna: ")
        except: print("linha precisa ser uma letra..."); continue
        coluna = coluna.upper()
        if coluna > 'J' or coluna < 'A': continue

        try: linha = int(input("Linha: "))
        except: print("linha precisa ser um numero..."); continue
        if linha > 10: continue
        posicionou = navio.posicionar(tabuleiro, linha, coluna, direcao)

def posiciona_navio_inimigo(tabuleiro, navio):
    print(f"Posicione o {navio.nome}:")
    posicionou = False
    while not posicionou:
        direcao = random.randint(1,2)
        if direcao == 1: direcao = 'V'
        else: direcao = 'H'
        coluna = chr(random.randint(65, 74))
        linha = random.randint(1, 10)
        posicionou = navio.posicionar(tabuleiro, linha, coluna, direcao)

def print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo, 
                    PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
                    PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
                    SU_inimigo_afundado, DE_inimigo_afundado):
    print("Tabuleiro Jogador: ")
    print("Navios afundados: ", end="")
    if PA_afundado: print("Porta-Avioes ", end="")
    if EN_afundado: print("Encouracado ", end="")
    if CR_afundado: print("Cruzador ", end="")
    if SU_afundado: print("Submarino ", end="")
    if DE_afundado: print("Destroyer ", end="")
    print("")
    print(tabuleiro_jogador)
    print("Tabuleiro Inimgo: ")
    print("Navios afundados: ", end="")
    if PA_inimigo_afundado: print("Porta-Avioes ", end="")
    if EN_inimigo_afundado: print("Encouracado ", end="")
    if CR_inimigo_afundado: print("Cruzador ", end="")
    if SU_inimigo_afundado: print("Submarino ", end="")
    if DE_inimigo_afundado: print("Destroyer ", end="")
    print("")
    print(tabuleiro_inimigo)