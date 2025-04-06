from typing import Dict, List, Tuple

class Navio:
    def __init__(self, nome: str, tamanho: int) -> None:
        self.__nome = nome
        self.__tamanho = tamanho
        self.__coordenadas = []
        self.__posicoes_atingidas = {}

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def tamanho(self) -> int:
        return self.__tamanho
    
    @property
    def coordenadas(self) -> list:
        return self.__coordenadas.copy()
    
    @property
    def posicoes_atingidas(self) -> dict:
        return self.__posicoes_atingidas.copy()

    def posicionar(self, tabuleiro, linha: int, coluna: str, direcao: str) -> bool:
        direcao = direcao.upper()
        if not tabuleiro.adicionar_navio(self, linha, coluna, direcao):
            return False
        self.__coordenadas = [(linha, coluna)]
        return True
    
    def barco_acertado(self, linha: int, coluna: str) -> None:
        self.__posicoes_atingidas[(linha, coluna)] = True
    
    def esta_afundando(self) -> bool:
        return len(self.__posicoes_atingidas) == self.__tamanho

    def __str__(self) -> str:
        resultado = f"Nome: {self.__nome}\nTamanho: {self.__tamanho}\n"
        resultado += "Posições do navio:\n"
        for pos in self.__coordenadas:
            resultado += f"  {pos}\n"
        resultado += f"Posições atingidas: {list(self.__posicoes_atingidas.keys())}\n"
        return resultado

class PortaAvioes(Navio):
    def __init__(self) -> None:
        super().__init__("PortaAvioes", 5)

class Encouracado(Navio):
    def __init__(self) -> None:
        super().__init__("Encouracado", 4)

class Cruzador(Navio):
    def __init__(self) -> None:
        super().__init__("Cruzador", 3)

class Submarino(Navio):
    def __init__(self) -> None:
        super().__init__("Submarino", 2)

class Destroyer(Navio):
    def __init__(self) -> None:
        super().__init__("Destroyer", 1)