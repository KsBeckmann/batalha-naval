from tabuleiro import TabuleiroJogador, TabuleiroInimigo
from navios import PortaAvioes, Encouracado, Cruzador, Submarino, Destroyer
from utils import limpar_tela, posiciona_navio, posiciona_navio_inimigo, print_tabuleiros
import random
from audio import Audio
import time

def main() -> None:
    """
    Função principal do jogo de Batalha Naval.
    Gerencia o fluxo do jogo, desde a inicialização até a condição de vitória ou derrota.
    """
    # Pergunta se o jogador quer iniciar o jogo
    limpar_tela()
    comecar_jogo = input("Começar jogo?(Y/N): ")
    limpar_tela()

    # Inicializa os tabuleiros
    tabuleiro_jogador = TabuleiroJogador()
    tabuleiro_inimigo = TabuleiroInimigo()

    # Inicializa os navios do jogador
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

    # Inicializa os navios do inimigo
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

    # Agrupa os navios em listas para facilitar o acesso
    barcos_jogador = [porta_avioes, encouracado, cruzador, submarino, destroyer]
    barcos_inimigo = [porta_avioes_inimigo, encouracado_inimigo, cruzador_inimigo, submarino_inimigo, destroyer_inimigo]

    if comecar_jogo.upper() == 'Y':
        # Exibe os tabuleiros iniciais
        print_tabuleiros(
            tabuleiro_jogador, tabuleiro_inimigo,
            PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
            PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
            SU_inimigo_afundado, DE_inimigo_afundado
        )

        # Fase de posicionamento: jogador posiciona seus navios
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

        # Fase de posicionamento: computador posiciona seus navios aleatoriamente
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

        # Loop principal do jogo
        while(True):
            # Vez do jogador
            barco_inimigo = "posicao_ja_jogada"
            while barco_inimigo == "posicao_ja_jogada":
                print("Escolha uma posição para atirar")
                
                # Solicita a coluna para o tiro
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
                
                # Solicita a linha para o tiro
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
                
                # Registra o tiro no tabuleiro inimigo
                Audio.tocar_efeito('tiro')
                time.sleep(1.0)
                barco_inimigo = tabuleiro_inimigo.registrar_tiro(linha, coluna, barcos_inimigo)
                if barco_inimigo == "posicao_ja_jogada":
                    print("Você já atirou nessa posição. Tente outra.")
                elif barco_inimigo == 0:
                    Audio.tocar_efeito('erro')
                elif barco_inimigo in ['P', 'E', 'C', 'S', 'D']:
                    Audio.tocar_efeito('acerto')
                elif barco_inimigo == 'barco_defendeu':
                    Audio.tocar_efeito('escudo')

            
            # Atualiza a visualização após o tiro do jogador
            limpar_tela()
            print_tabuleiros(
                tabuleiro_jogador, tabuleiro_inimigo,
                PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
                PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
                SU_inimigo_afundado, DE_inimigo_afundado
            )
            
            # Verifica e atualiza o estado dos navios inimigos
            if barco_inimigo == 'P':
                porta_avioes_inimigo.barco_acertado(linha, coluna)
                if porta_avioes_inimigo.esta_afundando(): PA_inimigo_afundado = True

            if barco_inimigo == 'E':
                encouracado_inimigo.barco_acertado(linha, coluna)
                if encouracado_inimigo.esta_afundando(): EN_inimigo_afundado = True

            if barco_inimigo == 'C':
                cruzador_inimigo.barco_acertado(linha, coluna)
                if cruzador_inimigo.esta_afundando(): CR_inimigo_afundado = True

            if barco_inimigo == 'S':
                submarino_inimigo.barco_acertado(linha, coluna)
                if submarino_inimigo.esta_afundando(): SU_inimigo_afundado = True

            if barco_inimigo == 'D':
                destroyer_inimigo.barco_acertado(linha, coluna)
                if destroyer_inimigo.esta_afundando(): DE_inimigo_afundado = True
            
            # Verifica condição de vitória do jogador (todos os navios inimigos afundados)
            if PA_inimigo_afundado and EN_inimigo_afundado and CR_inimigo_afundado and SU_inimigo_afundado and DE_inimigo_afundado:
                limpar_tela()
                print("FIM DE JOGO. VOCE GANHOU AFF")
                exit(0)

            # Vez do computador (tiros aleatórios)
            barco_jogador = "posicao_ja_jogada"
            while barco_jogador == "posicao_ja_jogada":
                # Gera posição aleatória para o tiro do computador
                coluna = chr(random.randint(65, 74))  # ASCII: A=65, J=74
                linha = random.randint(1, 10)
                barco_jogador = tabuleiro_jogador.registrar_tiro(linha, coluna, barcos_jogador)
            
            # Atualiza a visualização após o tiro do computador
            limpar_tela()
            print_tabuleiros(
                tabuleiro_jogador, tabuleiro_inimigo,
                PA_afundado, EN_afundado, CR_afundado, SU_afundado, DE_afundado,
                PA_inimigo_afundado, EN_inimigo_afundado, CR_inimigo_afundado, 
                SU_inimigo_afundado, DE_inimigo_afundado
            )

            # Exibe mensagens sobre escudos ativados
            if barco_inimigo == "barco_defendeu":
                print("Barco inimigo defendeu 😂🤏🤣🤏")
            if barco_jogador == "barco_defendeu":
                print("O seu barco defendeu 😷🤒🤮😴")

            # Verifica e atualiza o estado dos navios do jogador
            if barco_jogador == 'P':
                porta_avioes.barco_acertado(linha, coluna)
                if porta_avioes.esta_afundando():
                    PA_afundado = True

            if barco_jogador == 'E':
                encouracado.barco_acertado(linha, coluna)
                if encouracado.esta_afundando(): EN_afundado = True

            if barco_jogador == 'C':
                cruzador.barco_acertado(linha, coluna)
                if cruzador.esta_afundando(): CR_afundado = True

            if barco_jogador == 'S':
                submarino.barco_acertado(linha, coluna)
                if submarino.esta_afundando(): SU_afundado = True

            if barco_jogador == 'D':
                destroyer.barco_acertado(linha, coluna)
                if destroyer.esta_afundando(): DE_afundado = True
            
            # Verifica condição de derrota do jogador (todos os navios do jogador afundados)
            if PA_afundado and EN_afundado and CR_afundado and SU_afundado and DE_afundado:
                limpar_tela()
                print("FIM DE JOGO. VOCE PERDEU KKKKKKKKKKKKKKKK")
                exit(0)
    else:
        print("Saindo...")
        exit(0)

if __name__ == "__main__":
    main()