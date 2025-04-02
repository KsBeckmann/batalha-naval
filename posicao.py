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