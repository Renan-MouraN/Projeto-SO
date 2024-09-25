class FilaBloqueados:

    def __init__(self):
        # Inicializa os atributos da Fila
        self.fila_bloqueados = []

    def get_primeiro(self):
        # Retorna o primeiro processo da Fila
        return self.fila_bloqueados[0]
    
    def add_processo(self, processo, log=[]):
        # Adiciona processo à Fila
        self.fila_bloqueados.append(processo)
        if len(self.fila_bloqueados) == 1:
            log.append(f"E/S iniciada em {processo.get_process_name()}")

    def remove_processo(self, processo):
        # Remove processo da Fila
        self.fila_bloqueados.remove(processo)

    def atualiza_tempo_bloqueados(self, fila_prontos, log=[]):
        # Atualiza a Fila, diminuindo o tempo bloqueado e movendo para a fila de prontos se necessário
        for bloqueado in self.fila_bloqueados:
            bloqueado.diminui_tempo_bloqueado()
            if bloqueado.get_tempo_bloqueado() == 0:
                fila_prontos.add_processo(bloqueado)
                self.fila_bloqueados.remove(bloqueado)
                if self.fila_bloqueados:
                    log.append(f"E/S iniciada em {self.get_primeiro().get_process_name()}")
                bloqueado.set_state("Pronto")

    def get_fila(self):
        # Retorna a Fila de Bloqueados
        return self.fila_bloqueados
