class PosicaoBarco:
    """
    Classe que representa uma posição no tabuleiro do jogo de batalha naval.
    Converte entre notação de jogo (A1, B2, etc.) e índices de matriz (0,0), (1,1), etc.
    """
    def __init__(self, linha: int, coluna: str) -> None:
        """
        Inicializa uma posição com linha (número) e coluna (letra).
        
        Args:
            linha: Número da linha (1-10)
            coluna: Letra da coluna (A-J)
        """
        self.__linha = linha
        self.__coluna = coluna.upper()
    
    @property
    def linha(self) -> int:
        """Retorna o número da linha."""
        return self.__linha
    
    @property
    def coluna(self) -> str:
        """Retorna a letra da coluna."""
        return self.__coluna
    
    def __str__(self) -> str:
        """Representação em string da posição (ex: '1A')."""
        return f"{self.__linha}{self.__coluna}"
    
    def converte_indices(self) -> list[int]:
        """
        Converte a notação de jogo para índices de matriz.
        
        Returns:
            Uma lista contendo [linha, coluna] como índices para a matriz (0-based)
        """
        coluna = ord(self.__coluna) - 65  # Converte letra para número (A=0, B=1, ...)
        linha = self.__linha - 1         # Converte linha para índice 0-based
        return [linha, coluna]
    
    def pos_eh_valida(self, tamanho_tabuleiro: int) -> bool:
        """
        Verifica se a posição está dentro dos limites do tabuleiro.
        
        Args:
            tamanho_tabuleiro: Tamanho do tabuleiro (normalmente 10)
            
        Returns:
            True se a posição é válida, False caso contrário
        """
        if self.__linha > tamanho_tabuleiro or self.__linha <= 0:
            return False
        if ord(self.__coluna) - 64 > tamanho_tabuleiro or ord(self.__coluna) - 64 <= 0:
            return False
        return True