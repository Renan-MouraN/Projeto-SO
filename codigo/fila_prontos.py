from bcp import Bcp


class FilaProntos:

    def __init__(self, tabela_processos=[]):
        # Inicializa os atributos da Fila
        self.fila_prontos = tabela_processos
        self.ordena_fila_prontos()

    def add_processo(self, processo):
        # Adiciona processo à Fila
        self.fila_prontos.append(processo)

    def remove_processo(self, processo):
        # Remove processo da Fila
        self.fila_prontos.remove(processo)

    def ordena_fila_prontos(self, fila_bloqueados=[]):
        # Ordena Fila de acordo com os créditos dos processos
        self.verifica_fila(fila_bloqueados)
        self.fila_prontos.sort(key=Bcp.get_credito, reverse=True)

    def get_primeiro(self):
        # Retorna o primeiro processo da Fila
        return self.fila_prontos[0]

    def verifica_fila(self, fila_bloqueados=[]):
        # Verifica e ajusta as filas de processos prontos e bloqueados,
        # removendo processos da fila de prontos que não estão prontos
        # e resetando os créditos dos processos caso todos estejam sem.
        cont = 0
        for processo in self.fila_prontos:
            # Se o processo não estiver no estado "Pronto", ele é removido da fila de prontos.
            if processo.get_state() != "Pronto": 
                self.remove_processo(processo)

            # Se o crédito do processo for 0, ele é contabilizado.
            elif processo.get_credito() == 0:
                cont += 1

        for processo in fila_bloqueados:
            # Se o crédito do processo for 0, ele também é contabilizado.
            if processo.get_credito() == 0:
                cont += 1

        # Se todos os processos (prontos e bloqueados) tiverem crédito 0, reseta os créditos.
        if cont == (len(self.fila_prontos) + len(fila_bloqueados)):
            # Reseta o crédito dos processos prontos.
            for processo in self.fila_prontos:
                processo.reset_credit()

            # Reseta o crédito dos processos bloqueados.
            for processo in fila_bloqueados:
                processo.reset_credit()

    def get_fila(self):
        # Retorna a Lista
        return self.fila_prontos
