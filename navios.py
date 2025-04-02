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