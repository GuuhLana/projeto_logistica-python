import networkx as nx

def encontrar_centro_mais_proximo(grafo, centros_distribuicao, destino):
    """
    Encontra o centro de distribuição mais próximo do destino.
    :param grafo: Objeto da classe Grafo.
    :param centros_distribuicao: Lista de centros de distribuição.
    :param destino: String, nome da cidade de destino.
    :return: String, nome do centro de distribuição mais próximo.
    """
    menor_distancia = float('inf')
    centro_mais_proximo = None

    for centro in centros_distribuicao:
        if nx.has_path(grafo.grafo, centro, destino):
            distancia = grafo.calcular_distancia(centro, destino)
            if distancia < menor_distancia:
                menor_distancia = distancia
                centro_mais_proximo = centro

    return centro_mais_proximo

def alocar_caminhoes(entregas, caminhoes, grafo, centros_distribuicao):
    """
    Aloca caminhões para as entregas com base na proximidade dos centros de distribuição e capacidade dos caminhões.
    :param entregas: Lista de objetos Entrega.
    :param caminhoes: Lista de objetos Caminhao.
    :param grafo: Objeto da classe Grafo.
    :param centros_distribuicao: Lista de centros de distribuição.
    :return: Dicionário com caminhões como chaves e centros de distribuição como valores.
    """
    alocacao = {}

    for entrega in entregas:
        centro_mais_proximo = encontrar_centro_mais_proximo(grafo, centros_distribuicao, entrega.destino)

        if centro_mais_proximo is None:
            print(f"Não há caminho para a entrega {entrega.destino} a partir dos centros de distribuição.")
            continue

        caminhão_alocado = None
        for caminhao in caminhoes:
            if caminhao.pode_realizar_entrega(entrega, grafo, centro_mais_proximo):
                caminhão_alocado = caminhao
                caminhao.adicionar_entrega(entrega)
                break

        if caminhão_alocado:
            alocacao[caminhão_alocado] = centro_mais_proximo
        else:
            print(f"Não há caminhão disponível para a entrega {entrega.destino}.")

    return alocacao

def calcular_distancia_total(caminhao, grafo, centro):
    """
    Calcula a distância total percorrida pelo caminhão.
    :param caminhao: Objeto da classe Caminhao.
    :param grafo: Objeto da classe Grafo.
    :param centro: Nome do centro de distribuição.
    :return: Float, distância total percorrida em quilômetros.
    """
    distancia_total = 0
    for entrega in caminhao.entregas:
        try:
            distancia_total += grafo.calcular_distancia(centro, entrega.destino)
        except nx.NetworkXNoPath:
            print(f"Não há caminho para a entrega {entrega.destino} a partir do centro {centro}.")
    return distancia_total
