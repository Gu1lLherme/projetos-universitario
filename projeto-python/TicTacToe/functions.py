def guardaDados(nomeJogardor1, nomeJogardor2, scoreJogador1, scoreJogador2, valorRodada, empates):
    
    with open('historico.txt', 'w') as arquivo:
        # Escreve no arquivo
        
        arquivo.write(f'Nome 1 Jogador: {nomeJogardor1}\n')
        arquivo.write(f'Nome 2 Jogador: {nomeJogardor2}\n')
        arquivo.write(f'Score Final X: {scoreJogador1}\n')
        arquivo.write(f'Score Final O: {scoreJogador2}\n')
        arquivo.write(f'Empates: {empates}\n')
        arquivo.write(f'Numero Total de Rodadas: {valorRodada + 1}\n')

def salvarFotoTabela(tabuleiro, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for linha in tabuleiro:
            arquivo.write(" | ".join(linha) + "\n")
        arquivo.write("--" * 5 + "\n")

            
