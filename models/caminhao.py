# Arquivo: models/caminhao.py

class Caminhao:
    def __init__(self, capacidade, horas_disponiveis):
        self.capacidade = capacidade
        self.horas_disponiveis = horas_disponiveis
        self.entregas = []  # Lista de entregas atribuídas ao caminhão

    def adicionar_entrega(self, entrega):
        """
        Adiciona uma entrega ao caminhão.
        :param entrega: Objeto da classe Entrega.
        """
        self.entregas.append(entrega)
