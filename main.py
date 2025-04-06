from tabuleiro import TabuleiroJogador, TabuleiroInimigo
from navios import PortaAvioes, Encouracado, Cruzador, Submarino, Destroyer
from utils import limpar_tela, posiciona_navio, posiciona_navio_inimigo, print_tabuleiros
import random

def main() -> None:
    tabuleiro_jogador = TabuleiroJogador()
    tabuleiro_inimigo = TabuleiroInimigo()

    porta_avioes = PortaAvioes()
    PA_afundado = False

    encouracado = Encouracado()
    EN_afundado = False

    cruzador = Cruzador()
    CR_afundado = False

    submarino = Submarino()
    SU_afundado = False

    destroyer = Destroyer()
    DE_afundado = False

    porta_avioes_inimigo = PortaAvioes()
    PA_inimigo_afundado = False

    encouracado_inimigo = Encouracado()
    EN_inimigo_afundado = False

    cruzador_inimigo = Cruzador()
    CR_inimigo_afundado = False

    submarino_inimigo = Submarino()
    SU_inimigo_afundado = False

    destroyer_inimigo = Destroyer()
    DE_inimigo_afundado = False

    comecar_jogo = input("Começar jogo?(Y/N): ")
    limpar_tela()

    if comecar_jogo.upper() == 'Y':
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio(tabuleiro_jogador, porta_avioes)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio(tabuleiro_jogador, encouracado)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio(tabuleiro_jogador, cruzador)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio(tabuleiro_jogador, submarino)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio(tabuleiro_jogador, destroyer)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio_inimigo(tabuleiro_inimigo, porta_avioes_inimigo)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio_inimigo(tabuleiro_inimigo, encouracado_inimigo)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio_inimigo(tabuleiro_inimigo, cruzador_inimigo)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio_inimigo(tabuleiro_inimigo, submarino_inimigo)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        posiciona_navio_inimigo(tabuleiro_inimigo, destroyer_inimigo)
        limpar_tela()
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        while(True):
            barco = "posicao_ja_jogada"
            while barco == "posicao_ja_jogada":
                print("Escolha uma posição para atirar")
                coluna_valida = False
                while not coluna_valida:
                    coluna_input = input("Coluna (A-J): ")
                    if len(coluna_input) != 1:
                        print("Por favor, digite apenas uma letra.")
                        continue
                    coluna = coluna_input.upper()
                    if coluna < 'A' or coluna > 'J':
                        print("Por favor, digite uma letra entre A e J.")
                        continue
                    coluna_valida = True
                
                linha_valida = False
                while not linha_valida:
                    try:
                        linha = int(input("Linha (1-10): "))
                        if linha < 1 or linha > 10:
                            print("Por favor, digite um número entre 1 e 10.")
                            continue
                        linha_valida = True
                    except ValueError:
                        print("Por favor, digite um número válido.")
                        continue
                
                barco = tabuleiro_inimigo.registrar_tiro(linha, coluna)
                if barco == "posicao_ja_jogada":
                    print("Você já atirou nessa posição. Tente outra.")
            
            limpar_tela()
            print_tabuleiros(
                tabuleiro_jogador, tabuleiro_inimigo,
                PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
                PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
                SU_inimigo_afundado, DE_inimigo_afundado
            )
            
            if barco == 'P':
                porta_avioes_inimigo.barco_acertado(linha, coluna)
                if porta_avioes_inimigo.esta_afundando(): PA_inimigo_afundado = True

            if barco == 'E':
                encouracado_inimigo.barco_acertado(linha, coluna)
                if encouracado_inimigo.esta_afundando(): EN_inimigo_afundado = True

            if barco == 'C':
                cruzador_inimigo.barco_acertado(linha, coluna)
                if cruzador_inimigo.esta_afundando(): CR_inimigo_afundado = True

            if barco == 'S':
                submarino_inimigo.barco_acertado(linha, coluna)
                if submarino_inimigo.esta_afundando(): SU_inimigo_afundado = True

            if barco == 'D':
                destroyer_inimigo.barco_acertado(linha, coluna)
                if destroyer_inimigo.esta_afundando(): DE_inimigo_afundado = True
            
            if PA_inimigo_afundado and EN_inimigo_afundado and CR_inimigo_afundado and SU_inimigo_afundado and DE_inimigo_afundado:
                limpar_tela()
                print("FIM DE JOGO. VOCE GANHOU AFF")
                exit(0)

            barco = "posicao_ja_jogada"
            while barco == "posicao_ja_jogada":
                coluna = chr(random.randint(65, 74))
                linha = random.randint(1, 10)
                barco = tabuleiro_jogador.registrar_tiro(linha, coluna)
            limpar_tela()
            print_tabuleiros(
                tabuleiro_jogador, tabuleiro_inimigo,
                PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
                PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
                SU_inimigo_afundado, DE_inimigo_afundado
            )

            if barco == 'P':
                porta_avioes.barco_acertado(linha, coluna)
                if porta_avioes.esta_afundando():
                    PA_afundado = True

            if barco == 'E':
                encouracado.barco_acertado(linha, coluna)
                if encouracado.esta_afundando(): EN_afundado = True

            if barco == 'C':
                cruzador.barco_acertado(linha, coluna)
                if cruzador.esta_afundando(): CR_afundado = True

            if barco == 'S':
                submarino.barco_acertado(linha, coluna)
                if submarino.esta_afundando(): SU_afundado = True

            if barco == 'D':
                destroyer.barco_acertado(linha, coluna)
                if destroyer.esta_afundando(): DE_afundado = True
            
            if PA_afundado and EN_afundado and CR_afundado and SU_afundado and DE_afundado:
                limpar_tela()
                print("FIM DE JOGO. VOCE PERDEU KKKKKKKKKKKKKKKK")
                exit(0)
    else:
        print("Saindo...")
        exit(0)

if __name__ == "__main__":
    main()