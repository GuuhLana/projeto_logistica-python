import networkx as nx

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

    def adicionar_centro(self, origem, destino, distancia, custo):
        """
        Adiciona uma conexão entre o centro e o destino com distância e custo.
        :param origem: String, nome da cidade de origem (centro de distribuição).
        :param destino: String, nome da cidade de destino.
        :param distancia: Float, distância entre origem e destino em quilômetros.
        :param custo: Float, custo de transporte entre origem e destino.
        """
        self.grafo.add_edge(origem, destino, distance=distancia, cost=custo)

    def calcular_distancia(self, origem, destino):
        """
        Calcula a distância entre dois pontos no grafo.
        :param origem: String, nome da cidade de origem.
        :param destino: String, nome da cidade de destino.
        :return: Float, distância em quilômetros.
        """
        try:
            return nx.shortest_path_length(self.grafo, source=origem, target=destino, weight='distance')
        except nx.NetworkXNoPath:
            print(f"Não há caminho entre {origem} e {destino}.")
            return float('inf')  # Retorna infinito se não houver caminho

    def calcular_custo(self, origem, destino):
        """
        Calcula o custo entre dois pontos no grafo.
        :param origem: String, nome da cidade de origem.
        :param destino: String, nome da cidade de destino.
        :return: Float, custo em unidades monetárias.
        """
        try:
            return nx.shortest_path_length(self.grafo, source=origem, target=destino, weight='cost')
        except nx.NetworkXNoPath:
            print(f"Não há caminho entre {origem} e {destino}.")
            return float('inf')  # Retorna infinito se não houver caminho
