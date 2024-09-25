class Bcp:
    # Inicializa os atributos do processo
    def __init__(self, process_name, priority, text_references=[], ID=None):   
        self.process_name = process_name
        self.pc = 0
        self.state = "Pronto"
        self.priority = priority
        self.credit = priority
        self.reg_x = 0
        self.reg_y = 0
        self.text_references = text_references
        self.ID = ID
        self.tempo_bloqueado = 0
        self.num_instrucoes_exec = 0
    

    def __str__(self):         
        # Retorna o número de instruções executadas pelo processo até o momento.                                                             
        return f"Nome do processo: {self.process_name}, Creditos: {self.credit}"    

    
     # Incrementa o contador de programa
    def incrementa_PC(self):                                                  
        self.pc += 1
    
    
    # Diminui o crédito do processo
    def diminui_credito(self):                                                 
        if self.credit > 0:
            self.credit -= 1

    
    # Diminui o tempo que processo fica bloqueado
    def diminui_tempo_bloqueado(self):                                         
        self.tempo_bloqueado -= 1


    # Restaura os créditos do processo
    def reset_credit(self):                                                    
        self.credit = self.priority
    

    # Criação de getters e setters para manipulação dos atributos
    def get_credito(self):                                                     
        return self.credit
    
    
    # Retorna o número de instruções executadas pelo processo até o momento.
    def get_num_intrucoes_exec(self):                                          
        return self.num_instrucoes_exec
    
    
    # Retorna o identificador único do processo
    def get_ID(self):                                                         
        return self.ID
    
    
     # Retorna a próxima instrução a ser executada pelo processo e incrementa o PC.
    def get_prox_comando(self):
        proxComando = self.text_references[self.pc]                          
        self.incrementa_PC()
        return proxComando


    # Retorna o nome do processo.
    def get_process_name(self):                                               
        return self.process_name

    
    # Retorna o valor armazenado no registrador X.   
    def get_reg_x(self):                                                             
        return self.reg_x

    
    # Retorna o valor armazenado no registrador Y.
    def get_reg_y(self):                                                      
        return self.reg_y
    
    
    # Retorna o tempo restante em que o processo está bloqueado.
    def get_tempo_bloqueado(self):                                            
        return self.tempo_bloqueado
    
    
    # Retorna o estado atual do processo (Pronto, Executando, Bloqueado, etc.).  
    def get_state(self):                                                      
        return self.state
    
    
    # Define o estado atual do processo.
    def set_state(self, state):                                               
        self.state = state
    
    # Define o tempo restante de bloqueio do processo.
    def set_tempo_bloqueado(self, tempo):                                     
        self.tempo_bloqueado = tempo
    
    
    # Define o valor do registrador X.
    def set_reg_x(self, x):                                                   
        self.reg_x = x

    
    #  Define o valor do registrador Y.
    def set_reg_y(self, y):                                                   
        self.reg_y = y 
    
    #   Define o número de instruções executadas pelo processo até o momento.
    def set_num_intrucoes_exec(self, instrucoes_exec):                        
        self.num_instrucoes_exec = instrucoes_exec 