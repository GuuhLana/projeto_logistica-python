from models.entrega import Entrega
from models.caminhao import Caminhao
from models.grafo import Grafo
from algoritmo_roteamento import alocar_caminhoes, calcular_distancia_total

def main():
    centros_distribuicao = ['Belem', 'Recife', 'Sao Paulo', 'Curitiba']
    destinos = ['Fortaleza', 'Brasilia', 'Rio de Janeiro', 'Porto Alegre']

    # Criar o grafo com as distâncias
    grafo = Grafo()
    grafo.adicionar_centro('Belem', 'Fortaleza', 1614)
    grafo.adicionar_centro('Recife', 'Brasilia', 2100)
    grafo.adicionar_centro('Sao Paulo', 'Rio de Janeiro', 429)
    grafo.adicionar_centro('Curitiba', 'Porto Alegre', 711)

    # Criar entregas
    entrega1 = Entrega(destino='Fortaleza', prazo='2024-09-20', peso=2.5)
    entrega2 = Entrega(destino='Brasilia', prazo='2024-09-22', peso=3.0)
    entrega3 = Entrega(destino='Rio de Janeiro', prazo='2024-09-23', peso=1.2)
    entrega4 = Entrega(destino='Porto Alegre', prazo='2024-09-24', peso=4.0)
    entregas = [entrega1, entrega2, entrega3, entrega4]

    # Criar caminhões
    caminhao1 = Caminhao(capacidade=5, horas_disponiveis=8)
    caminhao2 = Caminhao(capacidade=8, horas_disponiveis=10)
    caminhoes = [caminhao1, caminhao2]

    # Alocar caminhões
    alocacao = alocar_caminhoes(entregas, caminhoes, grafo, centros_distribuicao)

    # Exibir resultados
    for caminhao, centro in alocacao.items():
        distancia_total = calcular_distancia_total(caminhao, grafo, centro)
        print(f"Caminhão alocado ao centro {centro} percorreu {distancia_total} km com as seguintes entregas:")
        for entrega in caminhao.entregas:
            print(f"  {entrega}")

if __name__ == "__main__":
    main()
