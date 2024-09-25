from bcp import Bcp


class TabelaProcessos:

    def __init__(self, prioridades=[], filelines_array=[]):
        # Inicializa os atributos da Tabela
        self.tabela_processos = []

        # Loop que cria e adiciona os processos à Tabela
        for i in range(0, 10):
            prio = prioridades[i]
            nome = filelines_array[i][0]
            comandos = filelines_array[i][1:]
            bcp = Bcp(nome, prio, comandos, i)  # Cria processo
            self.add_processo(bcp)

    def add_processo(self, processo):
        # Método que adiciona o processo à Tabela
        self.tabela_processos.append(processo)

    def remove_processo(self, processo):
        # Remove processo da Tabela
        self.tabela_processos.remove(processo)

    def get_tabela(self):
        # Retorna a Tabela de Processos
        return self.tabela_processos
