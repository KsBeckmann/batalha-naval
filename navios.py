from typing import Dict, List, Tuple
from abc import ABC, abstractmethod
from random import randint

class Navio:
    """
    Classe base que representa um navio no jogo de batalha naval.
    """
    def __init__(self, nome: str, tamanho: int) -> None:
        """
        Inicializa um navio com nome e tamanho.
        
        Args:
            nome: Nome do navio
            tamanho: Tamanho do navio (número de células ocupadas)
        """
        self.__nome = nome
        self.__tamanho = tamanho
        self.__coordenadas = []          # Lista para armazenar as coordenadas do navio
        self.__posicoes_atingidas = {}   # Dicionário para rastrear posições atingidas
    
    @abstractmethod
    def escudo_ativo(self):
        """
        Método abstrato para determinar se o escudo está ativo.
        Cada tipo de navio implementa sua própria chance de defesa.
        """
        pass

    @property
    def nome(self) -> str:
        """Retorna o nome do navio."""
        return self.__nome
    
    @property
    def tamanho(self) -> int:
        """Retorna o tamanho do navio."""
        return self.__tamanho
    
    @property
    def coordenadas(self) -> list:
        """Retorna uma cópia da lista de coordenadas do navio."""
        return self.__coordenadas.copy()
    
    @property
    def posicoes_atingidas(self) -> dict:
        """Retorna uma cópia do dicionário de posições atingidas."""
        return self.__posicoes_atingidas.copy()

    def posicionar(self, tabuleiro, linha: int, coluna: str, direcao: str) -> bool:
        """
        Posiciona o navio no tabuleiro.
        
        Args:
            tabuleiro: O tabuleiro onde posicionar o navio
            linha: Número da linha inicial
            coluna: Letra da coluna inicial
            direcao: Direção ('V' para vertical, 'H' para horizontal)
            
        Returns:
            True se o posicionamento for bem-sucedido, False caso contrário
        """
        direcao = direcao.upper()
        if not tabuleiro.adicionar_navio(self, linha, coluna, direcao):
            return False
        self.__coordenadas = [(linha, coluna)]
        return True
    
    def barco_acertado(self, linha: int, coluna: str) -> None:
        """
        Registra que o navio foi atingido em uma posição específica.
        
        Args:
            linha: Número da linha do tiro
            coluna: Letra da coluna do tiro
        """
        self.__posicoes_atingidas[(linha, coluna)] = True
    
    def esta_afundando(self) -> bool:
        """
        Verifica se o navio está afundando (todas as posições foram atingidas).
        
        Returns:
            True se o navio está afundando, False caso contrário
        """
        return len(self.__posicoes_atingidas) == self.__tamanho

    def __str__(self) -> str:
        """Representação em string do navio, incluindo suas posições e estado."""
        resultado = f"Nome: {self.__nome}\nTamanho: {self.__tamanho}\n"
        resultado += "Posições do navio:\n"
        for pos in self.__coordenadas:
            resultado += f"  {pos}\n"
        resultado += f"Posições atingidas: {list(self.__posicoes_atingidas.keys())}\n"
        return resultado

# Classes específicas de navios com diferentes chances de defesa (escudo)

class PortaAvioes(Navio):
    """Porta-aviões: navio de tamanho 5 com 10% de chance de defesa."""
    def __init__(self) -> None:
        super().__init__("PortaAvioes", 5)
    
    def escudo_ativo(self) -> bool:
        """10% de chance de bloquear um ataque."""
        numero_aleatorio = randint(1, 100)
        if numero_aleatorio <= 10:
            return True
        return False

class Encouracado(Navio):
    """Encouraçado: navio de tamanho 4 com 20% de chance de defesa."""
    def __init__(self) -> None:
        super().__init__("Encouracado", 4)

    def escudo_ativo(self) -> bool:
        """20% de chance de bloquear um ataque."""
        numero_aleatorio = randint(1, 100)
        if numero_aleatorio <= 20:
            return True
        return False

class Cruzador(Navio):
    """Cruzador: navio de tamanho 3 com 30% de chance de defesa."""
    def __init__(self) -> None:
        super().__init__("Cruzador", 3)

    def escudo_ativo(self) -> bool:
        """30% de chance de bloquear um ataque."""
        numero_aleatorio = randint(1, 100)
        if numero_aleatorio <= 30:
            return True
        return False

class Submarino(Navio):
    """Submarino: navio de tamanho 2 com 40% de chance de defesa."""
    def __init__(self) -> None:
        super().__init__("Submarino", 2)
        
    def escudo_ativo(self) -> bool:
        """40% de chance de bloquear um ataque."""
        numero_aleatorio = randint(1, 100)
        if numero_aleatorio <= 40:
            return True
        return False

class Destroyer(Navio):
    """Destroyer: navio de tamanho 1 com 50% de chance de defesa."""
    def __init__(self) -> None:
        super().__init__("Destroyer", 1)

    def escudo_ativo(self) -> bool:
        """50% de chance de bloquear um ataque."""
        numero_aleatorio = randint(1, 100)
        if numero_aleatorio <= 50:
            return True
        return False