# Arquivo: models/entrega.py

class Entrega:
    def __init__(self, destino, prazo, peso):
        self.destino = destino
        self.prazo = prazo
        self.peso = peso

    def __repr__(self):
        return f"Entrega(destino='{self.destino}', prazo='{self.prazo}', peso={self.peso})"
