from fila_prontos import FilaProntos
from fila_bloqueados import FilaBloqueados
from tabela_processos import TabelaProcessos   


# Módulo: escalonador.py
# Descrição: Implementa o algoritmo de escalonamento de processos.
# Funções: escalonar, ajustar_prioridades.

class Escalonador:
    
    def __init__(self, prio, filelines, quantum, num_processos=10):
        # Inicializa o escalonador com as filas de processos e variáveis de controle.
        self.quantum = quantum
        self.nome_saida = f"log{self.quantum:02}.txt"  # Cria nome do arquivo de saída
        self.log = []  # Cria array para escrever saída
        self.tabela_processos = TabelaProcessos(prio, filelines)  # Cria a Tabela de Processos
        self.fila_prontos = FilaProntos(self.tabela_processos.get_tabela())  # Cria a Fila de Processos Prontos
        self.fila_bloqueados = FilaBloqueados()  # Cria a Fila de Processos Bloqueados
        self.num_interrupcoes = 0  # Contador de interrupções
        self.num_instrucoes_exec_total = 0  # Contador de instruções executadas no total
        self.num_quatum_exec = 0  # Contador de quanta executados
        self.num_processos = num_processos  # Número total de processos

    def get_media_trocas(self):
        # Calcula a média de trocas por processo.
        return round(self.num_interrupcoes / self.num_processos, 1)
    
    def get_media_instrucoes(self):
        # Calcula a média de instruções executadas por quantum.
        return round(self.num_instrucoes_exec_total / self.num_quatum_exec, 1)
    
    def get_quantum(self):
        # Retorna o valor do quantum.
        return self.quantum
        
    def executa_processos(self):
        # Método principal que executa o ciclo de escalonamento dos processos.
        # Verifica e executa os processos até que todos os processos tenham terminado.
        self.mensagem_carrega_processos()  # Registra no log o carregamento dos processos

        # Enquanto ainda tiver processos a serem executados
        while self.tabela_processos.get_tabela() or self.fila_prontos.get_fila() or self.fila_bloqueados.get_fila():

            # Caso não tenha mais processos prontos, atualiza os bloqueados
            if not self.tabela_processos.get_tabela() and self.fila_bloqueados.get_fila():
                while not self.fila_prontos.get_fila() and self.fila_bloqueados.get_fila():
                    self.fila_bloqueados.atualiza_tempo_bloqueados(self.fila_prontos)
            
            # Executa o primeiro processo da fila de prontos
            processo_exec = self.fila_prontos.get_primeiro()            
            processo_exec.set_state("Executando")            
            processo_exec.diminui_credito()            
            self.mensagem_processo_executando(processo_exec.get_process_name())
            self.num_quatum_exec += 1
            self.fila_bloqueados.atualiza_tempo_bloqueados(self.fila_prontos, self.log)
            
            # Loop que executa instruções do processo
            for i in range(self.get_quantum()):
                instrucao = processo_exec.get_prox_comando()  # Pega a instrução a ser executada
                processo_exec.set_num_intrucoes_exec(i + 1)

                # Caso a instrução seja "SAIDA", o processo termina
                if instrucao == "SAIDA":
                    self.mensagem_processo_terminado(processo_exec.get_process_name(),processo_exec.get_reg_x(),processo_exec.get_reg_y())
                    # Remove o processo da tabela, fila de prontos e fila de bloqueados, se estiver em alguma delas
                    if processo_exec in self.tabela_processos.get_tabela(): self.tabela_processos.remove_processo(processo_exec)
                    if processo_exec in self.fila_bloqueados.get_fila(): self.fila_bloqueados.remove_processo(processo_exec)
                    if processo_exec in self.fila_prontos.get_fila(): self.fila_prontos.remove_processo(processo_exec)
                    break
                
                # Caso a instrução seja "E/S", o processo é bloqueado
                elif instrucao == "E/S":
                    self.fila_bloqueados.add_processo(processo_exec, self.log)
                    self.fila_prontos.remove_processo(processo_exec)
                    processo_exec.set_state("Bloqueado")
                    processo_exec.set_tempo_bloqueado(2)              
                    self.mensagem_processo_interrompido(processo_exec.get_process_name(), processo_exec.get_num_intrucoes_exec())               
                    break

                # Instruções que afetam os registradores X e Y
                elif instrucao[0] == "X":
                    processo_exec.set_reg_x(int(instrucao[2:]))
                
                elif instrucao[0] == "Y":
                    processo_exec.set_reg_y(int(instrucao[2:]))
                
                elif instrucao == "COM":
                    ...

            # Atualiza o contador de instruções executadas
            self.num_instrucoes_exec_total += processo_exec.get_num_intrucoes_exec()

            # Se o processo ainda estiver "Executando", é interrompido e volta para a fila de prontos
            if processo_exec.get_state() == "Executando" and processo_exec in self.tabela_processos.get_tabela():
                self.mensagem_processo_interrompido(processo_exec.get_process_name(), processo_exec.get_num_intrucoes_exec())
                processo_exec.set_state("Pronto")
            
            # Reordena a fila de prontos após possíveis mudanças
            self.fila_prontos.ordena_fila_prontos(self.fila_bloqueados.get_fila())

    
    def mensagem_carrega_processos(self):
        # Adiciona ao log os processos carregados
        for processo in self.tabela_processos.get_tabela():
            self.log.append(f"Carregando {processo.get_process_name()}")

    def mensagem_processo_interrompido(self, processo_interrompido, instrucoes_executadas):
        # Adiciona ao log o processo interrompido
        self.num_interrupcoes += 1
        self.log.append(f"Interrompendo {processo_interrompido} após {instrucoes_executadas} instruções")                 
            
    def mensagem_processo_executando(self, processo_executado):
        # Adiciona ao log o processo que está executando       
        self.log.append(f"Executando {processo_executado}")          
        
    def mensagem_processo_terminado(self, processo_terminado, reg_x, reg_y):
        # Adiciona ao log o processo que terminou
        self.num_interrupcoes += 1
        self.log.append(f"{processo_terminado} terminado. X={reg_x}. Y={reg_y}")

    def mensagem_final_log(self):
        # Adiciona ao log as médias calculadas
        self.log.append(f"MEDIA DE TROCAS: {self.get_media_trocas()}")
        self.log.append(f"MEDIA DE INSTRUCOES: {self.get_media_instrucoes()}")
        self.log.append(f"QUANTUM: {self.get_quantum()}")

    def escreve_saida(self):
        # Escreve o arquivo de saída
        self.mensagem_final_log()
        with open(f"../saidas/{self.nome_saida}", 'w') as arquivo:
            arquivo.write("\n".join(self.log))
