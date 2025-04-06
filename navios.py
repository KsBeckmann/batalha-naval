from typing import Dict, List, Tuple

class Navio:
    def __init__(self, nome: str, tamanho: int) -> None:
        self.nome = nome
        self.tamanho = tamanho
        self.info = {
            "coordenadas": [],
            "atingidas": {}
        }

    def posicionar(self, tabuleiro, linha: int, coluna: str, direcao: str) -> bool:
        direcao = direcao.upper()
        if not tabuleiro.adicionar_navio(self, linha, coluna, direcao):
            return False
        self.info["coordenadas"] = [(linha, coluna)]
        return True
    
    def barco_acertado(self, linha: int, coluna: str) -> None:
        self.info["atingidas"][(linha, coluna)] = True
    
    def esta_afundando(self) -> bool:
        return len(self.info["atingidas"]) == self.tamanho

    def __str__(self) -> str:
        resultado = f"Nome: {self.nome}\nTamanho: {self.tamanho}\n"
        resultado += "Posições do navio:\n"
        for pos in self.info["coordenadas"]:
            resultado += f"  {pos}\n"
        resultado += f"Posições atingidas: {list(self.info['atingidas'].keys())}\n"
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