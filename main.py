import os
import random

class PosicaoBarco():
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna.upper()
    
    def __str__(self):
        return f"{self.linha}{self.coluna}"
    
    def converte_indices(self):
        coluna = ord(self.coluna) - 65
        self.linha -= 1
        return [self.linha, coluna]
    
    def pos_eh_valida(self, tamanho_tabuleiro):
        if self.linha > tamanho_tabuleiro or self.linha <= 0:
            return False

        if ord(self.coluna) - 64 > tamanho_tabuleiro or ord(self.coluna) - 64 <= 0:
            return False
        
        return True

class Navio():
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.posicoes = []
        self.posicoes_atingidas = []

    def posicionar(self, tabuleiro, linha: int, coluna: str, direcao: str) -> bool:
        direcao = direcao.upper()
        if not tabuleiro.adicionar_navio(self, linha, coluna, direcao):
            return False
        self.posicoes = (linha, coluna)
        return True
    
    def barco_acertado(self, linha, coluna):
        self.posicoes_atingidas.append([linha, coluna])
    
    def esta_afundando(self):
        if len(self.posicoes_atingidas) == self.tamanho:
            return True

    def __str__(self):
        resultado = f"Nome: {self.nome}\nTamanho: {self.tamanho}\n"
        resultado += "Posições do navio:\n"
        for pos in self.posicoes:
            resultado += f"  {pos}\n"
        resultado += f"Posições atingidas: {self.posicoes_atingidas}\n"
        return resultado

class PortaAvioes(Navio):
    def __init__(self):
        super().__init__("PortaAvioes", 5)

class Encouracado(Navio):
    def __init__(self):
        super().__init__("Encouracado", 4)

class Cruzador(Navio):
    def __init__(self):
        super().__init__("Cruzador", 3)

class Submarino(Navio):
    def __init__(self):
        super().__init__("Submarino", 2)

class Destroyer(Navio):
    def __init__(self):
        super().__init__("Destroyer", 1)

class Tabuleiro:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabuleiro_matriz = [[0 for _ in range(self.tamanho)] for _ in range(self.tamanho)]
    
    def adicionar_navio(self, navio: Navio, linha: int, coluna: str, direcao: str) -> bool:
        if not self.posicao_valida(navio, linha, coluna, direcao):
            return False
        direcao = direcao.upper()
        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()
        if navio.nome == 'PortaAvioes': caractere = 'P'
        elif navio.nome == 'Encouracado': caractere = 'E'
        elif navio.nome == 'Cruzador': caractere = 'C'
        elif navio.nome == 'Submarino': caractere = 'S'
        elif navio.nome == 'Destroyer': caractere = 'D'

        if direcao == 'V':
            for i in range(navio.tamanho):
                self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] = caractere
                posicao_numeros[0] = posicao_numeros[0]+1

        if direcao == 'H':
            for i in range(navio.tamanho):
                self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] = caractere
                posicao_numeros[1] = posicao_numeros[1]+1
        return True

    def posicao_valida(self, navio, linha, coluna, direcao) -> bool:
        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()

        if posicao_numeros[0] < 0 or posicao_numeros[1] < 0:
            return False

        if direcao == 'V':
            for i in range(navio.tamanho):
                posicao_numeros[0] = posicao_numeros[0]+1
                if posicao_numeros[0] > self.tamanho or self.tabuleiro_matriz[posicao_numeros[0]-1][posicao_numeros[1]] != 0:
                    return False
            
        if direcao == 'H':
            for i in range(navio.tamanho):
                posicao_numeros[1] = posicao_numeros[1]+1
                if posicao_numeros[1] > self.tamanho or self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]-1] != 0:
                    return False
        return True

    def registrar_tiro(self, linha, coluna):
        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()

        if self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] == '~':
            return "posicao_ja_jogada"
        if self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] == 'X':
            return "posicao_ja_jogada"

        if self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] != 0:
            barco = self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]]
            self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] = 'X'
            return barco
        
        self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] = '~'
        return 0

class TabuleiroJogador(Tabuleiro):
    def __init__(self, tamanho=10):
        super().__init__(tamanho)
    
    def __str__(self):
        coord_num = 1
        tabuleiro_desenho = "    A   B   C   D   E   F   G   H   I   J\n"
        tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
        for linha in self.tabuleiro_matriz:
            tabuleiro_desenho += f"{coord_num}"
            if coord_num != 10: tabuleiro_desenho += " "
            for caractere in linha:
                if caractere == 0:
                    tabuleiro_desenho += "|   "
                    continue
                tabuleiro_desenho += f"| {caractere} "
            tabuleiro_desenho += "|"
            tabuleiro_desenho += "\n"
            tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
            coord_num += 1
        return tabuleiro_desenho
    
class TabuleiroInimigo(Tabuleiro):
    def __init__(self, tamanho=10):
        super().__init__(tamanho)

    def __str__(self):
        coord_num = 1
        tabuleiro_desenho = "    A   B   C   D   E   F   G   H   I   J\n"
        tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
        for linha in self.tabuleiro_matriz:
            tabuleiro_desenho += f"{coord_num}"
            if coord_num != 10: tabuleiro_desenho += " "
            for caractere in linha:
                if caractere == '~' or caractere == 'X':
                    tabuleiro_desenho += f"| {caractere} "
                    continue
                tabuleiro_desenho += "|   "

            tabuleiro_desenho += "|"
            tabuleiro_desenho += "\n"
            tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
            coord_num += 1
        return tabuleiro_desenho
    # def __str__(self):
    #     coord_num = 1
    #     tabuleiro_desenho = "    A   B   C   D   E   F   G   H   I   J\n"
    #     tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
    #     for linha in self.tabuleiro_matriz:
    #         tabuleiro_desenho += f"{coord_num}"
    #         if coord_num != 10: tabuleiro_desenho += " "
    #         for caractere in linha:
    #             if caractere == 0:
    #                 tabuleiro_desenho += "|   "
    #                 continue
    #             tabuleiro_desenho += f"| {caractere} "
    #         tabuleiro_desenho += "|"
    #         tabuleiro_desenho += "\n"
    #         tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
    #         coord_num += 1
    #     return tabuleiro_desenho

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

def print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo):
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

#MAIN ------------------------------------------------------------------
tabuleiro_jogador = TabuleiroJogador()
tabuleiro_inimigo = TabuleiroInimigo()

porta_avioes = PortaAvioes()
global PA_afundado; PA_afundado = False

encouracado = Encouracado()
global EN_afundado; EN_afundado = False

cruzador = Cruzador()
global CR_afundado; CR_afundado = False

submarino = Submarino()
global SU_afundado; SU_afundado = False

destroyer = Destroyer()
global DE_afundado; DE_afundado = False


porta_avioes_inimigo = PortaAvioes()
global PA_inimigo_afundado; PA_inimigo_afundado = False

encouracado_inimigo  = Encouracado()
global EN_inimigo_afundado; EN_inimigo_afundado = False

cruzador_inimigo = Cruzador()
global CR_inimigo_afundado; CR_inimigo_afundado = False

submarino_inimigo = Submarino()
global SU_inimigo_afundado; SU_inimigo_afundado = False

destroyer_inimigo = Destroyer()
global DE_inimigo_afundado; DE_inimigo_afundado = False

comecar_jogo:str = input("Começar jogo?(Y/N): ")
limpar_tela()

if comecar_jogo.upper() == 'Y':
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio(tabuleiro_jogador, porta_avioes)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio(tabuleiro_jogador, encouracado)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio(tabuleiro_jogador, cruzador)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio(tabuleiro_jogador, submarino)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio(tabuleiro_jogador, destroyer)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    #inimigo
    posiciona_navio_inimigo(tabuleiro_inimigo, porta_avioes_inimigo)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio_inimigo(tabuleiro_inimigo, encouracado_inimigo)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio_inimigo(tabuleiro_inimigo, cruzador_inimigo)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio_inimigo(tabuleiro_inimigo, submarino_inimigo)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    posiciona_navio_inimigo(tabuleiro_inimigo, destroyer_inimigo)
    limpar_tela()
    print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

    while(True):
        barco = "posicao_ja_jogada"
        while barco == "posicao_ja_jogada":
            print("Escolha uma posição para atirar")
            try: coluna = input("Coluna: ")
            except: print("linha precisa ser uma letra..."); continue
            coluna = coluna.upper()
            if coluna > 'J' or coluna < 'A': continue

            try: linha = int(input("Linha: "))
            except: print("linha precisa ser um numero..."); continue
            if linha > 10: continue
            barco = tabuleiro_inimigo.registrar_tiro(linha, coluna)
        
        limpar_tela()
        print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)
        
        if barco == 'P':
            porta_avioes_inimigo.barco_acertado(linha, coluna)
            if porta_avioes_inimigo.esta_afundando(): PA_inimigo_afundado = True

        if barco == 'E':
            encouracado_inimigo.barco_acertado(linha, coluna)
            if encouracado_inimigo.esta_afundando(): EN_inimigo_afundado = True

        if barco == 'C':
            cruzador_inimigo.barco_acertado(linha, coluna)
            if cruzador_inimigo.esta_afundando(): CR_inimigo_afundado = True

        if barco == 'S':
            submarino_inimigo.barco_acertado(linha, coluna)
            if submarino_inimigo.esta_afundando(): SU_inimigo_afundado = True

        if barco == 'D':
            destroyer_inimigo.barco_acertado(linha, coluna)
            if destroyer_inimigo.esta_afundando(): DE_inimigo_afundado = True
        
        if PA_inimigo_afundado and EN_inimigo_afundado and CR_inimigo_afundado and SU_inimigo_afundado and DE_inimigo_afundado:
            limpar_tela()
            print("FIM DE JOGO. VOCE GANHOU AFF")
            exit(0)

        ############################################################################################################################
        barco = "posicao_ja_jogada"
        while barco == "posicao_ja_jogada":
            coluna = chr(random.randint(65, 74))
            linha = random.randint(1, 10)
            barco = tabuleiro_jogador.registrar_tiro(linha, coluna)
        limpar_tela()
        print_tabuleiros(tabuleiro_jogador, tabuleiro_inimigo)

        if barco == 'P':
            porta_avioes.barco_acertado(linha, coluna)
            if porta_avioes.esta_afundando():
                PA_afundado = True

        if barco == 'E':
            encouracado.barco_acertado(linha, coluna)
            if encouracado.esta_afundando(): EN_afundado = True

        if barco == 'C':
            cruzador.barco_acertado(linha, coluna)
            if cruzador.esta_afundando(): CR_afundado = True

        if barco == 'S':
            submarino.barco_acertado(linha, coluna)
            if submarino.esta_afundando(): SU_afundado = True

        if barco == 'D':
            destroyer.barco_acertado(linha, coluna)
            if destroyer.esta_afundando(): DE_afundado = True
        
        if PA_afundado and EN_afundado and CR_afundado and SU_afundado and DE_afundado:
            limpar_tela()
            print("FIM DE JOGO. VOCE PERDEU KKKKKKKKKKKKKKKK")
            exit(0)
else:
    print("Saindo...")
    exit(0)


    #TODO adicionar quantos barcos faltam destruir