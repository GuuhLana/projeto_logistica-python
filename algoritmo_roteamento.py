from models.entrega import Entrega
from models.caminhao import Caminhao
from models.grafo import Grafo


def encontrar_centro_mais_proximo(grafo, centros_distribuicao, destino):
    menor_distancia = float('inf')
    centro_mais_proximo = None
    for centro in centros_distribuicao:
        distancia = grafo.calcular_distancia(centro, destino)
        if distancia < menor_distancia:
            menor_distancia = distancia
            centro_mais_proximo = centro
    return centro_mais_proximo


def alocar_caminhoes(entregas, caminhoes, grafo, centros_distribuicao):
    """
    Aloca as entregas nos caminhões de acordo com a capacidade e proximidade dos centros de distribuição.
    :param entregas: Lista de entregas.
    :param caminhoes: Lista de caminhões.
    :param grafo: Grafo com distâncias.
    :param centros_distribuicao: Lista dos centros de distribuição.
    """
    # Alocar entregas para centros de distribuição
    alocacao_centros = {centro: [] for centro in centros_distribuicao}

    for entrega in entregas:
        centro_mais_proximo = encontrar_centro_mais_proximo(grafo, centros_distribuicao, entrega.destino)
        alocacao_centros[centro_mais_proximo].append(entrega)

    # Alocar caminhões para as entregas
    alocacao_caminhoes = {}

    for centro, entregas_no_centro in alocacao_centros.items():
        caminhoes_disponiveis = [caminhao for caminhao in caminhoes if caminhao not in alocacao_caminhoes]
        for entrega in entregas_no_centro:
            for caminhao in caminhoes_disponiveis:
                if caminhao.capacidade >= entrega.peso and caminhao.horas_disponiveis > 0:
                    caminhao.adicionar_entrega(entrega)
                    caminhao.capacidade -= entrega.peso
                    caminhao.horas_disponiveis -= grafo.calcular_distancia(centro,
                                                                           entrega.destino) / 60  # Tempo estimado de viagem
                    alocacao_caminhoes[caminhao] = centro
                    break
            else:
                print(f"Nenhum caminhão disponível para entrega {entrega.destino}")

    return alocacao_caminhoes


def calcular_distancia_total(caminhao, grafo, centro):
    """
    Calcula a distância total percorrida por um caminhão a partir de um centro de distribuição.
    :param caminhao: Instância do caminhão.
    :param grafo: Grafo de distâncias.
    :param centro: Centro de distribuição de origem.
    :return: Distância total percorrida.
    """
    distancia_total = 0
    for entrega in caminhao.entregas:
        distancia_total += grafo.calcular_distancia(centro, entrega.destino)
    return distancia_total
