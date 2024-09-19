# Arquivo: models/entrega.py

from datetime import datetime

class Entrega:
    def __init__(self, destino, prazo, peso):
        self.destino = destino
        self.prazo = datetime.strptime(prazo, "%Y-%m-%d")
        self.peso = peso
        self.tempo_estimado = 0  # Tempo estimado para a entrega em horas

    def calcular_tempo_estimado(self, grafo, centro):
        """
        Calcula o tempo estimado para a entrega considerando a distância.
        """
        distancia = grafo.calcular_distancia(centro, self.destino)
        self.tempo_estimado = distancia / 60  # Exemplo: 1 km leva 1 minuto
