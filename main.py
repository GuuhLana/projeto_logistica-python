from algoritmo_roteamento import alocar_caminhoes, calcular_distancia_total
from models.caminhao import Caminhao
from models.entrega import Entrega
from models.grafo import Grafo

def main():
    centros_distribuicao = ['Belem', 'Recife']
    destinos = ['Fortaleza', 'Brasilia', 'Rio de Janeiro']

    grafo = Grafo()
    grafo.adicionar_centro('Belem', 'Fortaleza', 1614, 1000)
    grafo.adicionar_centro('Recife', 'Brasilia', 2100, 1500)
    grafo.adicionar_centro('Recife', 'Rio de Janeiro', 0, 0)

    for destino in destinos:
        if not grafo.grafo.has_node(destino):
            print(f"Destino {destino} não está no grafo")

    entrega1 = Entrega(destino='Fortaleza', prazo='2024-09-20', peso=10.0)
    entrega2 = Entrega(destino='Brasilia', prazo='2024-09-22', peso=5.0)
    entrega3 = Entrega(destino='Rio de Janeiro', prazo='2024-09-23', peso=3.0)
    entregas = [entrega1, entrega2, entrega3]

    caminhao1 = Caminhao(capacidade=3, horas_disponiveis=5)
    caminhao2 = Caminhao(capacidade=4, horas_disponiveis=6)
    caminhoes = [caminhao1, caminhao2]

    alocacao = alocar_caminhoes(entregas, caminhoes, grafo, centros_distribuicao)

    for caminhao, centro in alocacao.items():
        distancia_total = calcular_distancia_total(caminhao, grafo, centro)
        print(f"Caminhão alocado ao centro {centro} percorreu {distancia_total} km com as seguintes entregas:")
        for entrega in caminhao.entregas:
            print(f"- {entrega.destino}, Peso: {entrega.peso}, Prazo: {entrega.prazo}")

if __name__ == "__main__":
    main()

