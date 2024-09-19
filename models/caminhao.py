class Caminhao:
    def __init__(self, capacidade, horas_disponiveis):
        self.capacidade = capacidade
        self.horas_disponiveis = horas_disponiveis
        self.entregas = []
        self.capacidade_atual = capacidade
        self.horas_utilizadas = 0

    def adicionar_entrega(self, entrega):
        if self.capacidade_atual >= entrega.peso and self.horas_utilizadas + entrega.tempo_estimado <= self.horas_disponiveis:
            self.entregas.append(entrega)
            self.capacidade_atual -= entrega.peso
            self.horas_utilizadas += entrega.tempo_estimado
        else:
            raise ValueError("Capacidade ou horas insuficientes para a entrega")

    def pode_realizar_entrega(self, entrega, grafo, centro):
        """
        Verifica se o caminhão pode realizar a entrega considerando capacidade e horas.
        """
        custo = grafo.calcular_custo(centro, entrega.destino)
        tempo_estimado = custo / 60  # Exemplo: 1 km leva 1 minuto
        return (self.capacidade_atual >= entrega.peso and
                self.horas_utilizadas + tempo_estimado <= self.horas_disponiveis)
