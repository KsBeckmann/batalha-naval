class PosicaoBarco():
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna.upper()
    
    def __str__(self):
        return f"{self.linha}{self.coluna}"
    
    def converte_indices(self):
        coluna = ord(self.coluna) - 64
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

    def posicionar(self, posicoes):
        if len(posicoes) != self.tamanho:
            print(f"O navio {self.nome} requer {self.tamanho} posições, mas {len(posicoes)} foram fornecidas.")
            return False
        
        for pos in posicoes:
            linha, coluna = pos
            posicao_obj = PosicaoBarco(linha, coluna)
            self.posicoes.append(posicao_obj)
        return True
    
    def acertou_tiro(self, posicao_tiro):
        for posicao in self.posicoes:
            if posicao.linha == posicao_tiro[0] and posicao.coluna == posicao_tiro[1].upper():
                    self.posicoes_atingidas.append((posicao_tiro[0], posicao_tiro[1]))
                    return True
        return False
    
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
        super().__init__("Encouracado", 5)

class Cruzador(Navio):
    def __init__(self):
        super().__init__("Cruzador", 5)

class Submarino(Navio):
    def __init__(self):
        super().__init__("Submarino", 5)

class Destroyer(Navio):
    def __init__(self):
        super().__init__("Destroyer", 5)

class Tabuleiro:
    def __init__(self, tiros, tamanho=10):
        self.tiros = tiros
        self.tamanho = tamanho
        self.tabuleiro_matriz = [[0 for _ in range(self.tamanho)] for _ in range(self.tamanho)]
    
    def adicionar_navio(self, navio, linha, coluna, direcao):

        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()
        if navio.nome == 'PortaAvioes': caractere = 'P'
        if navio.nome == 'Encouracado': caractere = 'E'
        if navio.nome == 'Cruzador': caractere = 'C'
        if navio.nome == 'Submarino': caractere = 'S'
        if navio.nome == 'Destroyer': caractere = 'D'
        if direcao == 'V':
            for i in range(navio.tamanho):
                self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] = caractere
                posicao_numeros[0] = posicao_numeros[0]+1

        if direcao == 'H':
            for i in range(navio.tamanho):
                self.tabuleiro_matriz[posicao_numeros[0]][posicao_numeros[1]] = caractere
                posicao_numeros[1] = posicao_numeros[1]+1

    def posicao_valida(self, navio, linha, coluna, direcao):
        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()

        if posicao_numeros[0] < 0 or posicao_numeros[1] < 0:
            return False

        if direcao == 'V':
            for i in range(navio.tamanho):
                posicao_numeros[0] = posicao_numeros[0]+1
            if posicao_numeros[0] > self.tamanho-1:
                return False
            
        if direcao == 'H':
            for i in range(navio.tamanho):
                posicao_numeros[1] = posicao_numeros[1]+1
            if posicao_numeros[1] > self.tamanho-1:
                return False
        return True

    def registrar_tiro(self, navio, linha, coluna):
        posicao = PosicaoBarco(linha, coluna)
        posicao_numeros = posicao.converte_indices()

        if navio.acertou_tiro(posicao_numeros):
            self.tabuleiro_matriz[linha][coluna] = "X"
        else:
            self.tabuleiro_matriz[linha][coluna] = '~'
            
    # def __str__(self):
    #     for linha in self.tabuleiro_matriz:
    #         print(*linha)


#MAIN ------------------------------------------------------------------

aaa = PortaAvioes()

aaa.posicionar(((3, 'b'), (3, 'c'), (3, 'd'), (3, 'e'), (3, 'f')))

aaa.acertou_tiro((3, 'b'))
aaa.acertou_tiro((3, 'c'))
aaa.acertou_tiro((3, 'd'))
aaa.acertou_tiro((3, 'e'))
aaa.acertou_tiro((3, 'f'))

if aaa.esta_afundando():
    print("oi")
else:
    print("oo")