# --------------- cores -------------------
co0 = "#FFFFFF"  # branca
co1 = "#333333"  # preta pesado
co2 = "#fcc058"  # laranja
co3 = "#38576b"  # valor
co4 = "#3297a8"   # azul
co5 = "#fff873"   # amarela
co6 = "#fcc058"  # laranja
co7 = "#e85151"   # vermelha
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta

# Logica do Jogo

Jogador_1 = 'X'
Jogador_2 = 'O'

score_1 = 0
score_2 = 0

tabuleiro = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']]

jogando = 'X'
jogar = ''
contador= 0

def vencedor():
    pass

def terminar():
    pass

# função que coleta a posição a qual o jogador da vez escolheu adicionar seu X ou O
def controlarJogo(respotajogador):
    # Comparar os valores recebidos

    if respotajogador == str(1):
        # Verifica se a posição atual escolhida está vazia
        if 'botao_0' in respotajogador and respotajogador['botao_0']['text'] == " ":
            # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
            if jogando == "X":
                cor = co7
            if jogando == "O":
                cor = co8
            # Define a cor do texto
            respotajogador['botao_0']['fg'] = cor
            
            # Marca a posição no tabuleiro com o valor do jogador atual
            respotajogador['botao_0']['text'] = jogando
            tabuleiro[0][0] = jogando

            # faz a verificação de quem será a proxima jogada
            if jogando  == "X":
                jogando = "O"
                jogar = "Jogador 1"
            else:
                jogando = "X"
                jogar = "Jogador 2"
            # contador aumenta em 1
            contador += 1

            # Quandodo o contador ser Maior ou igual a 5
            # Será realizado um verificação se ouve algum vencedor de acordo com os padroes de vitorio do jogo
            if contador >= 5:
                #Verificação de vitoria: LINHAS
                if (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]) != "":
                    vencedor(jogando)
                elif (tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]) != "":
                    vencedor(jogando)
                elif (tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]) != "":
                    vencedor(jogando)
                #Verificação de vitoria: COLUNAS

                if (tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]) != "":
                    vencedor(jogando)
                elif (tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]) != "":
                    vencedor(jogando)
                elif (tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]) != "":
                    vencedor(jogando)

                # Verificação de vitoria: DIAGONAL

                if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]) != "":
                    vencedor(jogando)
                elif (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]) != "":
                    vencedor(jogando)
                
                # Verificação de EMPATE

                if contador>= 9:
                    vencedor("Resultado EMPATE")
    print(respotajogador)
    