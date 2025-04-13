from typing import Literal, Union
from posicao import PosicaoBarco
from navios import Navio

class Tabuleiro:
    """
    Classe base que representa um tabuleiro de batalha naval.
    Implementa a lógica básica do tabuleiro de jogo.
    """
    def __init__(self, tamanho: int = 10) -> None:
        """
        Inicializa um tabuleiro com tamanho especificado (padrão: 10x10).
        
        Args:
            tamanho: Tamanho do tabuleiro (número de células em cada lado)
        """
        self.__tamanho = tamanho
        # Inicializa matriz do tabuleiro com zeros (posições vazias)
        self.__tabuleiro_matriz = [[0 for _ in range(self.__tamanho)] for _ in range(self.__tamanho)]
    
    @property
    def tamanho(self) -> int:
        """Retorna o tamanho do tabuleiro."""
        return self.__tamanho
    
    @property
    def matriz(self) -> list:
        """Retorna uma cópia da matriz do tabuleiro."""
        return [linha.copy() for linha in self.__tabuleiro_matriz]

    def adicionar_navio(self, navio: Navio, linha: int, coluna: str, direcao: str) -> bool:
        """
        Adiciona um navio ao tabuleiro na posição e direção especificadas.
        
        Args:
            navio: O navio a ser adicionado
            linha: Número da linha inicial
            coluna: Letra da coluna inicial
            direcao: Direção ('V' para vertical, 'H' para horizontal)
            
        Returns:
            True se o navio foi adicionado com sucesso, False caso contrário
        """
        if not self.posicao_valida(navio, linha, coluna, direcao):
            return False
        direcao = direcao.upper()
        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()
        
        # Define o caractere de representação baseado no tipo de navio
        if navio.nome == 'PortaAvioes': caractere = 'P'
        elif navio.nome == 'Encouracado': caractere = 'E'
        elif navio.nome == 'Cruzador': caractere = 'C'
        elif navio.nome == 'Submarino': caractere = 'S'
        elif navio.nome == 'Destroyer': caractere = 'D'
        else: caractere = '?'

        # Posiciona o navio verticalmente
        if direcao == 'V':
            for i in range(navio.tamanho):
                self.__tabuleiro_matriz[posicao_numeros[0]+i][posicao_numeros[1]] = caractere
                
        # Posiciona o navio horizontalmente
        if direcao == 'H':
            for i in range(navio.tamanho):
                self.__tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]+i] = caractere
        return True

    def posicao_valida(self, navio: Navio, linha: int, coluna: str, direcao: str) -> bool:
        """
        Verifica se a posição é válida para adicionar um navio.
        
        Args:
            navio: O navio a ser adicionado
            linha: Número da linha inicial
            coluna: Letra da coluna inicial
            direcao: Direção ('V' para vertical, 'H' para horizontal)
            
        Returns:
            True se a posição é válida, False caso contrário
        """
        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()

        # Verifica se a posição inicial está dentro do tabuleiro
        if posicao_numeros[0] < 0 or posicao_numeros[1] < 0:
            return False

        # Verifica posicionamento vertical
        if direcao == 'V':
            for i in range(navio.tamanho):
                posicao_numeros[0] = posicao_numeros[0]+1
                # Verifica se passa dos limites ou se já há outro navio na posição
                if posicao_numeros[0] > self.__tamanho or self.__tabuleiro_matriz[posicao_numeros[0]-1][posicao_numeros[1]] != 0:
                    return False
            
        # Verifica posicionamento horizontal
        if direcao == 'H':
            for i in range(navio.tamanho):
                posicao_numeros[1] = posicao_numeros[1]+1
                # Verifica se passa dos limites ou se já há outro navio na posição
                if posicao_numeros[1] > self.__tamanho or self.__tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]-1] != 0:
                    return False
        return True

    def registrar_tiro(self, linha: int, coluna: str, barcos_vetor: list) -> Union[Literal['P','E','C','S','D'], Literal[0], Literal['posicao_ja_jogada']]:
        """
        Registra um tiro no tabuleiro e retorna o resultado.
        
        Args:
            linha: Número da linha do tiro
            coluna: Letra da coluna do tiro
            barcos_vetor: Lista de navios para verificar escudo
            
        Returns:
            - Caractere do barco ('P', 'E', 'C', 'S', 'D') se acertou um navio
            - 0 se errou (água)
            - 'posicao_ja_jogada' se a posição já foi alvo de tiro anteriormente
            - 'barco_defendeu' se o escudo do barco defendeu o tiro
        """
        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()
        caracteres_barcos = ['P','E','C','S','D']

        # Verifica se a posição já foi alvo de tiro
        if self.__tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] == '~':
            return "posicao_ja_jogada"
        if self.__tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] == 'X':
            return "posicao_ja_jogada"

        # Se há um navio na posição
        if self.__tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] != 0:
            barco_atingido = self.__tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]]
            # Verifica se o escudo do barco está ativo
            for i in range(0,5):
                if caracteres_barcos[i] == barco_atingido:
                    if barcos_vetor[i].escudo_ativo():
                        return "barco_defendeu"
            # Marca a posição como atingida ('X')
            self.__tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] = 'X'
            return barco_atingido
        
        # Se errou o tiro (água)
        self.__tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] = '~'
        return 0

class TabuleiroJogador(Tabuleiro):
    """
    Classe que representa o tabuleiro do jogador.
    Mostra todos os detalhes, incluindo posições dos navios.
    """
    def __str__(self) -> str:
        """
        Representação em string do tabuleiro do jogador, mostrando todos os elementos.
        
        Returns:
            String formatada do tabuleiro
        """
        coord_num = 1
        tabuleiro_desenho = "    A   B   C   D   E   F   G   H   I   J\n"
        tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
        for linha in self.matriz:
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
    """
    Classe que representa o tabuleiro do inimigo.
    Mostra apenas os tiros acertados ('X') e errados ('~'), ocultando as posições dos navios.
    """
    def __str__(self) -> str:
        """
        Representação em string do tabuleiro inimigo, mostrando apenas os tiros.
        
        Returns:
            String formatada do tabuleiro
        """
        coord_num = 1
        tabuleiro_desenho = "    A   B   C   D   E   F   G   H   I   J\n"
        tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
        for linha in self.matriz:
            tabuleiro_desenho += f"{coord_num}"
            if coord_num != 10: tabuleiro_desenho += " "
            for caractere in linha:
                # Mostra apenas 'X' e '~', esconde posições de navios
                if caractere == '~' or caractere == 'X':
                    tabuleiro_desenho += f"| {caractere} "
                    continue
                tabuleiro_desenho += "|   "
            tabuleiro_desenho += "|"
            tabuleiro_desenho += "\n"
            tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
            coord_num += 1
        return tabuleiro_desenho

    # Versão alternativa comentada do método que mostraria todas as posições (para depuração)
    # def __str__(self) -> str:
    #     coord_num = 1
    #     tabuleiro_desenho = "    A   B   C   D   E   F   G   H   I   J\n"
    #     tabuleiro_desenho += "  +---+---+---+---+---+---+---+---+---+---+\n"
    #     for linha in self.matriz:
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