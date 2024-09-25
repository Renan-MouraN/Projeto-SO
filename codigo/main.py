from escalonador import Escalonador
from leitor_arquivos import LeitorArquivos

# Lendo o valor do quantum diretamente do arquivo 'quantum.txt'

with open('../arquivos/quantum.txt', 'r') as arquivo:
    # Converte o valor lido para inteiro e remove espaços ou quebras de linha
    quantum = int(arquivo.read().strip())  

leitor_arquivos = LeitorArquivos()
escalonador = Escalonador(leitor_arquivos.get_prio(), leitor_arquivos.get_filelines_array(), quantum)

escalonador.executa_processos()
escalonador.escreve_saida()
