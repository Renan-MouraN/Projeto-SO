class LeitorArquivos:

    def __init__(self):
        # Inicializa os atributos do Leitor
        self.prioridades = [] 
        self.filelines_array = []
        self.quantum = 0 

        # Lê a prioridade dos processos do arquivo
        with open('../arquivos/prioridades.txt', 'r') as arquivo:
            self.prioridades = [int(linha.strip()) for linha in arquivo]

        # Loop que carrega as linhas dos arquivos dos processos
        for i in range(1, 11):
            file_name = f"../arquivos/{i:02}.txt"
            with open(file_name, 'r') as arquivo:
                linhas = arquivo.readlines()
                self.filelines_array.append([linha.strip() for linha in linhas])
        
        # Lê o valor do quantum
        with open('../arquivos/quantum.txt', 'r') as arquivo:
            self.quantum = int(arquivo.readline().strip())                    
            
    def get_prio(self):
        # Retorna a lista de prioridades
        return self.prioridades
    
    def get_quantum(self):
        # Retorna o valor de quantum
        return self.quantum

    def get_filelines_array(self):
        # Retorna as linhas dos arquivos de processo que foram lidos
        return self.filelines_array
