# Importação da biblioteca Tkinter para contrução da GUI
from tkinter import *
from tkinter import ttk
from functions import *

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

janela = Tk()
janela.title("Jogo da Velha")
janela.geometry('400x550')
janela.configure(bg=fundo)
janela.resizable(width=False, height=False)

# Frame 1; Criando placar

frame_superior = Frame(janela, width=380, height=150, bg=co1, relief="raised")
frame_superior.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

#  Frame 2; Exibindo Tabuleiro
frame_inferior = Frame(janela, width=380, height=400, bg=fundo, relief="flat")
frame_inferior.grid(row=1, column=0, sticky=NW, padx=10)

# Determinando o jogador 1:
# Icone X
icon_x = Label(frame_superior, text="X", height=1, relief='flat', anchor='center', font=('Ivy 52 bold'), bg=co1, fg=co7)
icon_x.place(x=35, y= 25)
# jogador 1
icon_x = Label(frame_superior, text="Player 1", height=1, relief='flat', anchor='center', font=('Ivy 9 bold'), bg=co1, fg=co0)
icon_x.place(x=35, y= 100)
# Pontuação
icon_x_pontuacao = Label(frame_superior, text="0", height=1, relief='flat', anchor='center', font=('Ivy 42 bold'), bg=co1, fg=co0)
icon_x_pontuacao.place(x=120, y= 35)

# Divisor
divisor = Label(frame_superior, text=":", height=1, relief='flat', anchor='center', font=('Ivy 28 bold'), bg=co1, fg=co0)
divisor.place(x=190, y=45)

# Determinando jogador 2:
# Icone O
icon_O = Label(frame_superior, text="O", height=1, relief='flat', anchor='center', font=('Ivy 54 bold'), bg=co1, fg=co4)
icon_O.place(x=300, y= 23)
# jogador 2
icon_O = Label(frame_superior, text="Player 2", height=1, relief='flat', anchor='center', font=('Ivy 9 bold'), bg=co1, fg=co0)
icon_O.place(x=305, y= 100)
# Pontuação
icon_O_pontuacao = Label(frame_superior, text="0", height=1, relief='flat', anchor='center', font=('Ivy 42 bold'), bg=co1, fg=co0)
icon_O_pontuacao.place(x=235, y= 35)


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
contador = 0
def vencedor(i):
    print(i)

def iniciarJogo():
    
   

    def terminar():
        pass

    # função que coleta a posição a qual o jogador da vez escolheu adicionar seu X ou O
    def controlarJogo(respotajogador):
        # Comparar os valores recebidos
        global jogando 
        global jogar 
        global contador
        if respotajogador == str(1):
            # Verifica se a posição atual escolhida está vazia
            if botao_0['text'] == "":

                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_0['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_0['text'] = jogando
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
        if respotajogador == str(2):

            if botao_1['text'] == "":   
                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_1['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_1['text'] = jogando
                tabuleiro[0][1] = jogando

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
        if respotajogador == str(3):
            
            if botao_2['text'] == "":   
                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_2['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_2['text'] = jogando
                tabuleiro[0][2] = jogando

                # faz a verificação de quem será a proxima jogada
                if jogando  == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"
                # contador aumenta em 1
                contador += 1              
        if respotajogador == str(4):
            
            if botao_3['text'] == "":   
                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_3['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_3['text'] = jogando
                tabuleiro[1][0] = jogando

                # faz a verificação de quem será a proxima jogada
                if jogando  == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"
                # contador aumenta em 1
                contador += 1
        if respotajogador == str(5):
            
            if botao_4['text'] == "":   
                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_4['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_4['text'] = jogando
                tabuleiro[1][1] = jogando

                # faz a verificação de quem será a proxima jogada
                if jogando  == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"
                # contador aumenta em 1
                contador += 1               
        if respotajogador == str(6):
            
            if botao_5['text'] == "":   
                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_5['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_5['text'] = jogando
                tabuleiro[1][2] = jogando

                # faz a verificação de quem será a proxima jogada
                if jogando  == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"
                # contador aumenta em 1
                contador += 1
        if respotajogador == str(7):
            
            if botao_6['text'] == "":   
                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_6['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_6['text'] = jogando
                tabuleiro[2][0] = jogando

                # faz a verificação de quem será a proxima jogada
                if jogando  == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"
                # contador aumenta em 1
                contador += 1          
        if respotajogador == str(8):
            
            if botao_7['text'] == "":   
                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_7['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_7['text'] = jogando
                tabuleiro[2][1] = jogando

                # faz a verificação de quem será a proxima jogada
                if jogando  == "X":
                    jogando = "O"
                    jogar = "Jogador 1"
                else:
                    jogando = "X"
                    jogar = "Jogador 2"
                # contador aumenta em 1
                contador += 1
        if respotajogador == str(9):
            
            if botao_8['text'] == "":   
                # Faz a verificaçao de quem esta jogando e define a cor da posição escolhida
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8
                # Define a cor do texto
                botao_8['fg'] = cor
                
                # Marca a posição no tabuleiro com o valor do jogador atual
                botao_8['text'] = jogando
                tabuleiro[2][2] = jogando

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
        if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] != "":
            vencedor(jogando)
        elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] != "":
            vencedor(jogando)
        elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != "":
            vencedor(jogando)
        #Verificação de vitoria: COLUNAS

        if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] != "":
            vencedor(jogando)
        elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] != "":
            vencedor(jogando)
        elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != "":
            vencedor(jogando)

        # Verificação de vitoria: DIAGONAL

        if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "":
            vencedor(jogando)
        elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "":
            vencedor(jogando)
        
        # Verificação de EMPATE

        if contador>= 9:
            vencedor("Resultado EMPATE")
    
    # Montando tabuleiro 
    # Linhas Verticais/ rows
    linha_vertical = Label(frame_inferior, text="", width=1, height=25, relief='flat', pady=10, anchor='center', font=('Ivy 6 bold '), bg=co0)
    linha_vertical.place(x=115, y= 10)

    linha_vertical = Label(frame_inferior, text=" ", width=1, height=25, relief='flat', pady=10, anchor='center', font=('Ivy 6 bold '), bg=co0)
    linha_vertical.place(x=260, y= 10)

    # Linhas Horizontais/ columns
    linha_horizontal = Label(frame_inferior, text=" ", width=350, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'), bg=co0)
    linha_horizontal.place(x=15, y=95)

    linha_horizontal = Label(frame_inferior, text=" ", width=350, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'), bg=co0)
    linha_horizontal.place(x=15, y=200)


    # Botões do tabuleiro
    # linha 0 
    botao_0 = Button(frame_inferior, command=lambda:controlarJogo('1'), text="", height=1, width=4, pady=5, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_0.place(x=15, y=10)

    botao_1 = Button(frame_inferior, command=lambda:controlarJogo('2'), text="", height=1, width=5, pady=5, padx=3, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_1.place(x=126, y=10)

    botao_2 = Button(frame_inferior, command=lambda:controlarJogo('3'), text="", height=1, width=4, pady=5, padx=3, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_2.place(x=265, y=10)

    # linha 1
    botao_3= Button(frame_inferior, command=lambda:controlarJogo('4'), text="", height=1, width=4, pady=9, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_3.place(x=15, y=103)

    botao_4 = Button(frame_inferior, command=lambda:controlarJogo('5'), text="", height=1, width=5, pady=9, padx=3, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_4.place(x=127, y=104)

    botao_5= Button(frame_inferior, command=lambda:controlarJogo('6'), text="", height=1, width=4, pady=9, padx=3, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_5.place(x=265, y=103)
    # linha 2

    botao_6 = Button(frame_inferior, command=lambda:controlarJogo('7'), text="", height=1, width=4, pady=1, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_6.place(x=15, y=203)

    botao_7 = Button(frame_inferior, command=lambda:controlarJogo('8'), text="", height=1, width=5, pady=1, padx=3, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_7.place(x=126, y=204)

    botao_8 = Button(frame_inferior, command=lambda:controlarJogo('9'), text="", height=1, width=4, pady=1, padx=3, font=('Ivy 30 bold'), overrelief=RIDGE, relief='flat', bg=fundo)
    botao_8.place(x=265, y=203)


# Botão jogar 
botao_jogar= Button(frame_inferior, command=iniciarJogo, text="JOGAR", height=1, width=10, font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
botao_jogar.place(x=150, y=320)


janela.mainloop()