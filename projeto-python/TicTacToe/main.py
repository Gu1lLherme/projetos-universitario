# Importando biblioteca Tkinter para GUI
import tkinter
from tkinter import *
from tkinter import ttk
# Importando biblioteca functions para armazenar os dados
from functions import guardaDados, salvarFotoTabela

#  -------- cores --------
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# criando janela principal
janela = Tk()
janela.title('Jogo da Velha')
janela.geometry('260x400')
janela.resizable(width=False, height=False)
janela.configure(bg=fundo)

#  logica do app 

jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['','',''] , ['','',''] , ['','','']]

jogando = 'X'
joga =''
contador = 0
contador_de_rodada = 0
contador_empates = 0

def iniciar_jogo():
    b_jogar.place(x=800, y=350)
    # Alterando o valor do nomes
    global entradaJogador1
    global entradaJogador2
    entradaJogador1 = entrada_nome_jogador1.get().strip()
    entradaJogador2 = entrada_nome_jogador2.get().strip()
    if entradaJogador1 != '' and entrada_nome_jogador2 != '':
        app_player_x['text'] = entradaJogador1
        app_player_o['text'] = entradaJogador2
    else:
        app_player_x['text'] = 'Jogador 1'
        app_player_o['text'] = 'Jogador 2'



    def controlar(posicaoTAbuleiro):
        global jogando
        global contador
        global jogar
        global contador_empates
        
        
        # comparando o valor recebido
        if posicaoTAbuleiro==str(1):
            # verificando se aquela posicao esta vazia ou nao
            if b_0['text']=='':
                # verificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
                   
        if posicaoTAbuleiro==str(2):
            # verificando se aquela posicao esta vazia ou nao
            if b_1['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
                             
        if posicaoTAbuleiro==str(3):
            # verificando se aquela posicao esta vazia ou nao
            if b_2['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2]= jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1   
                   
        if posicaoTAbuleiro==str(4):
            # verificando se aquela posicao esta vazia ou nao
            if b_3['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
                                      
        if posicaoTAbuleiro==str(5):
            # verificando se aquela posicao esta vazia ou nao
            if b_4['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
                       
        if posicaoTAbuleiro==str(6):
            # verificando se aquela posicao esta vazia ou nao
            if b_5['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1   
                        
        if posicaoTAbuleiro==str(7):
            # verificando se aquela posicao esta vazia ou nao
            if b_6['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
                     
        if posicaoTAbuleiro==str(8):
            # verificando se aquela posicao esta vazia ou nao
            if b_7['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1      
        
        if posicaoTAbuleiro==str(9):
            # verificando se aquela posicao esta vazia ou nao
            if b_8['text']=='':
                # varificando quem esta jogar e assim definir a cor do smbolo
                if jogando =='X':
                    cor=co7
                if jogando =='O':
                    cor=co8
                
                # definindo a cor do text do botao
                # e marcar aquela posicao da tabela 
                # com o valor do jogador atual
                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando
                
                # verificando quem esta a jogar ,
                # para poder trocar de jogador
                if jogando =='X':
                    jogando = 'O'
                    joga = 'Jogador 1'
                else:
                    jogando = 'X'
                    joga = 'Jogador 2'
                
                # incrementar o contador para proxima rodada
                contador+=1
        
        salvarFotoTabela(tabela, f"jogo_da_velha_{contador_de_rodada+1}.txt")        
        
        # Apos o contador ser maior ou igual a 5, 
        # verifica se ouve algum vencedor de acordo 
        # com os padroes seguintes dentro da tabela
        if contador>=5:
            # linhas
            if tabela[0][0]==tabela[0][1]==tabela[0][2]!="":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1]==tabela[1][2]!="":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1]==tabela[2][2]!="":
                vencedor(jogando)
            
            # colunas
            if tabela[0][0] == tabela[1][0]==tabela[2][0]!="":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1]==tabela[2][1]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2]==tabela[2][2]!="":
                vencedor(jogando)
                
                
            # diagonais
            if tabela[0][0] == tabela[1][1]==tabela[2][2]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1]==tabela[2][0]!="":
                vencedor(jogando)
            
            # Empate 
            if contador>=9:
                vencedor('Foi empate') 
                contador_empates += 1        
        
    # pra decidir o vencedor
    def vencedor(resultadoVencedor):
        global tabela
        global score_1
        global score_2
        global contador_de_rodada
        global contador
        
        # bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        app_vencedor = Label(frame_baixo, text='', width=20, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_vencedor.place(x=25, y=240)
        # Determina quem é o vencedor e adiciona a ponto 
        if resultadoVencedor == 'X':
            score_2+=1
            app_vencedor['text'] = f'{app_player_o['text']} venceu'
            app_o_pontos['text'] = score_2
            
        if resultadoVencedor == 'O':
            score_1+=1
            app_vencedor['text'] = f'{app_player_x['text']} venceu'
            app_x_pontos['text'] = score_1
        
        if resultadoVencedor == 'Foi empate':
            app_vencedor['text'] = 'Foi um empate'
            
            
        def start():
            # limpando os botoes
            b_0['text']=''
            b_1['text']=''
            b_2['text']=''
            b_3['text']=''
            b_4['text']=''
            b_5['text']=''
            b_6['text']=''
            b_7['text']=''
            b_8['text']=''
            # Reabilitando os botões após 1 roda finalizada
            b_0['state']='normal'
            b_1['state']='normal'
            b_2['state']='normal'
            b_3['state']='normal'
            b_4['state']='normal'
            b_5['state']='normal'
            b_6['state']='normal'
            b_7['state']='normal'
            b_8['state']='normal'
            # Faz o reset da tela pra iniciar outra partida
            # zerando a contagem
            app_vencedor.destroy()
            b_jogar.destroy()
            
        # Botao jogar
        b_jogar = Button(frame_baixo, command=start, text='Proxima rodada', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        b_jogar.place(x=70, y=200)
        
        # Função para indicar a finalização
        def jogo_acabou():
            b_jogar.destroy()
            app_vencedor.destroy()
            
            terminar()
        # Número de rodadas até finalizar a partida
        if contador_de_rodada == 4:
            jogo_acabou()
        else:
            contador_de_rodada+=1
            # reiniciando a tabela
            tabela = [['','',''] , ['','',''] , ['','','']]
            contador = 0
            
           
    
    # pra terminar o jogo atual
    def terminar():
        
        global contador_de_rodada
        global score_1
        global score_2
        global contador
        # Função para armazenar dados ao final da partida
        guardaDados(app_player_x['text'], app_player_o['text'], app_x_pontos['text'], app_o_pontos['text'], contador_de_rodada, contador_empates)
        
        
        contador_de_rodada = 0
        score_1 = 0
        score_2 = 0
        contador = 0
        
        # bloqueando os botoes
        b_0['state']='disable'
        b_1['state']='disable'
        b_2['state']='disable'
        b_3['state']='disable'
        b_4['state']='disable'
        b_5['state']='disable'
        b_6['state']='disable'
        b_7['state']='disable'
        b_8['state']='disable'
        
        app_fim = Label(frame_baixo, text='Jogo Acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2 )
        app_fim.place(x=40, y=90)
        
        # jogar de novo
        def jogar_denovo():
            
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()
            
            # chamando a funcao iniciar o jogo
            iniciar_jogo()
        
        # Botao jogar denovo
        b_jogar = Button(frame_baixo, command=jogar_denovo, text='Jogar de novo', height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
        b_jogar.place(x=75, y=200)
        
    
    # linhas verticais 
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=90, y=15)
    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=157, y=15)

    # linhas horizontais 
    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=30, y=63)
    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7 )
    app_.place(x=30, y=127)
    
    # linha 0
    b_0 = Button(frame_baixo,command=lambda:controlar('1'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_0.place(x=30, y=15)
    b_1 = Button(frame_baixo,command=lambda:controlar('2'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_1.place(x=96, y=15)
    b_2 = Button(frame_baixo,command=lambda:controlar('3'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_2.place(x=163, y=15)


    # linha 1
    b_3 = Button(frame_baixo,command=lambda:controlar('4'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_3.place(x=30, y=75)
    b_4 = Button(frame_baixo,command=lambda:controlar('5'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_4.place(x=96, y=75)
    b_5 = Button(frame_baixo,command=lambda:controlar('6'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_5.place(x=163, y=75)

    # linha 2
    b_6 = Button(frame_baixo,command=lambda:controlar('7'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_6.place(x=30, y=135)
    b_7 = Button(frame_baixo,command=lambda:controlar('8'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_7.place(x=96, y=135)
    b_8 = Button(frame_baixo,command=lambda:controlar('9'), text='', width=3, height=1,  font=('Ivy 20 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7 )
    b_8.place(x=163, y=135)

# Repartindo a janela principal em 2 Frame - superior/inferior

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW)

# Configurando o frame cima -
# Icone X
app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7 )
app_x.place(x=25, y=10)
# Nome do 1° Jogador
app_player_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_player_x.place(x=19, y=70)
# Exibe a contagem de pontos
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_x_pontos.place(x=80, y=20)
# Icone para separar um lado do outro
app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_separador.place(x=110, y=20)
# Icone O
app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4 )
app_o.place(x=170, y=10)
# Nome 2° Jogador
app_player_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0 )
app_player_o.place(x=170, y=70)
# Exibe a contagem de pontos
app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0 )
app_o_pontos.place(x=130, y=20)

# Label para informar oq deve ser digitado no campo abaixo.
nome_jogador_1 = Label(frame_baixo, width=19, height=1, text='Nome jogador 1', font=('Ivy 8 bold'), relief='flat', bg=fundo, fg=co0, anchor='w')
nome_jogador_1.place(x=88, y=35)
# caixa de entrada 
entrada_nome_jogador1 = Entry(frame_baixo, width=20, font=('Ivy 10 bold'), relief='flat')
entrada_nome_jogador1.place(x=60, y=55)
# Label para informar oq deve ser digitado no campo abaixo.
nome_jogador_2 = Label(frame_baixo, width=19, height=1,  text='Nome jogador 2', font=('Ivy 8 bold'), relief='flat', bg=fundo, fg=co0, anchor='w')
nome_jogador_2.place(x=88, y=80)
# caixa de entrada 
entrada_nome_jogador2 = Entry(frame_baixo, width=20, font=('Ivy 10 bold'), relief='flat')
entrada_nome_jogador2.place(x=60, y=100)

# Botao jogar

b_jogar = Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, height=1,  font=('Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0 )
b_jogar.place(x=85, y=197)



janela.mainloop()