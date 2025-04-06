class PosicaoBarco:
    def __init__(self, linha: int, coluna: str) -> None:
        self.__linha = linha
        self.__coluna = coluna.upper()
    
    @property
    def linha(self) -> int:
        return self.__linha
    
    @property
    def coluna(self) -> str:
        return self.__coluna
    
    def __str__(self) -> str:
        return f"{self.__linha}{self.__coluna}"
    
    def converte_indices(self) -> list[int]:
        coluna = ord(self.__coluna) - 65
        linha = self.__linha - 1
        return [linha, coluna]
    
    def pos_eh_valida(self, tamanho_tabuleiro: int) -> bool:
        if self.__linha > tamanho_tabuleiro or self.__linha <= 0:
            return False
        if ord(self.__coluna) - 64 > tamanho_tabuleiro or ord(self.__coluna) - 64 <= 0:
            return False
        return True