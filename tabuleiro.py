from typing import Literal, Union
from posicao import PosicaoBarco
from navios import Navio

class Tabuleiro:
    def __init__(self, tamanho: int = 10) -> None:
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
        else: caractere = '?'

        if direcao == 'V':
            for i in range(navio.tamanho):
                self.tabuleiro_matriz[posicao_numeros[0]+i][posicao_numeros[1]] = caractere
                
        if direcao == 'H':
            for i in range(navio.tamanho):
                self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]+i] = caractere
        return True

    def posicao_valida(self, navio: Navio, linha: int, coluna: str, direcao: str) -> bool:
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

    def registrar_tiro(self, linha: int, coluna: str) -> Union[Literal['P','E','C','S','D'], Literal[0], Literal['posicao_ja_jogada']]:
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
    def __init__(self, tamanho: int = 10) -> None:
        super().__init__(tamanho)
    
    def __str__(self) -> str:
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
    def __init__(self, tamanho: int = 10) -> None:
        super().__init__(tamanho)

    def __str__(self) -> str:
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