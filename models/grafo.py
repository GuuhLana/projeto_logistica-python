# Arquivo: models/grafo.py

import networkx as nx

class Grafo:
    def __init__(self):
        """
        Classe para representar as distâncias entre centros de distribuição e destinos usando um grafo.
        """
        self.grafo = nx.Graph()
        self.inicializar_grafo()

    def adicionar_centro(self, origem, destino, distancia):
        """
        Adiciona uma conexão entre um centro de distribuição e um destino.
        :param origem: String, nome da cidade de origem (centro de distribuição).
        :param destino: String, nome da cidade de destino.
        :param distancia: Float, distância entre origem e destino em quilômetros.
        """
        self.grafo.add_edge(origem, destino, distance=distancia)

    def calcular_distancia(self, origem, destino):
        """
        Calcula a distância entre dois pontos no grafo.
        :param origem: String, nome da cidade de origem.
        :param destino: String, nome da cidade de destino.
        :return: Float, distância em quilômetros. Retorna float('inf') se não houver caminho.
        """
        try:
            return nx.shortest_path_length(self.grafo, source=origem, target=destino, weight='distance')
        except nx.NetworkXNoPath:
            print(f"Não há caminho entre {origem} e {destino}.")
            return float('inf')  # Retorna um valor alto indicando que o caminho não é viável

    def inicializar_grafo(self):
        """
        Inicializa o grafo com as distâncias entre os centros de distribuição e destinos.
        """
        # Exemplo de adição de conexões
        self.adicionar_centro('Belém', 'Recife', 1300)
        self.adicionar_centro('Belém', 'São Paulo', 2500)
        self.adicionar_centro('Belém', 'Curitiba', 2400)
        self.adicionar_centro('Recife', 'São Paulo', 2000)
        self.adicionar_centro('Recife', 'Curitiba', 1900)
        self.adicionar_centro('São Paulo', 'Curitiba', 350)
        self.adicionar_centro('Recife', 'Fortaleza', 800)
        self.adicionar_centro('São Paulo', 'Fortaleza', 2200)
        self.adicionar_centro('Curitiba', 'Fortaleza', 2100)
        self.adicionar_centro('Belém', 'Rio de Janeiro', 2000)
        self.adicionar_centro('Recife', 'Rio de Janeiro', 1500)
        self.adicionar_centro('São Paulo', 'Rio de Janeiro', 400)
        self.adicionar_centro('Curitiba', 'Rio de Janeiro', 800)
        self.adicionar_centro('Belém', 'Porto Alegre', 2500)
        self.adicionar_centro('Recife', 'Porto Alegre', 2000)
        self.adicionar_centro('São Paulo', 'Porto Alegre', 700)
        self.adicionar_centro('Curitiba', 'Porto Alegre', 400)
