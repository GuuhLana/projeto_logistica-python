# Projeto de Otimização Logística com Múltiplos Centros de Distribuição

## Descrição
Este projeto é desenvolvido como parte da Avaliação A3 da disciplina de Estrutura de Dados e Análise de Algoritmos. O objetivo é implementar uma solução algorítmica para otimizar o processo de roteamento de entregas a partir de múltiplos centros de distribuição, minimizando o tempo e a distância percorrida pelos caminhões. Utilizamos estruturas de dados adequadas e algoritmos para alocar eficientemente os caminhões e calcular as rotas mais curtas.

## Cenário
Uma empresa de logística possui quatro centros de distribuição em **Belém (PA)**, **Recife (PE)**, **São Paulo (SP)** e **Curitiba (PR)**. A tarefa é alocar caminhões para realizar entregas em diversas regiões do Brasil. O projeto considera:

- O centro de distribuição mais próximo de cada destino.
- A capacidade de carga dos caminhões.
- O número de caminhões disponíveis.
- As distâncias percorridas.
- Os prazos de entrega.

## Objetivos
- **Minimizar o custo de transporte**: Encontrar rotas mais curtas e eficientes.
- **Garantir a entrega dentro do prazo**: Respeitar o limite de tempo para cada entrega.
- **Alocar caminhões eficientemente**: Distribuir as cargas entre os caminhões disponíveis.
- **Otimizar rotas**: Utilizar o centro de distribuição mais próximo e reduzir o tempo de transporte.
  
## Estrutura do Projeto
### Parte 1: Modelagem de Estruturas de Dados
- **Entregas**: Cada entrega tem um destino, prazo e peso.
- **Caminhões**: Cada caminhão possui capacidade máxima de carga e limite de horas de operação por dia.
- **Grafo**: Representa as distâncias entre os centros de distribuição e os destinos.

### Parte 2: Algoritmo de Roteamento
- **Centro mais próximo**: Algoritmo para determinar o centro de distribuição mais próximo de cada destino.
- **Rota ideal**: Calcular a rota ideal para cada caminhão, respeitando a capacidade de carga e o limite de horas.
- **Alocação de caminhões**: Definir quais caminhões serão alocados para cada centro de distribuição.

### Parte 3: Avaliação de Desempenho
- Testar diferentes cenários variando o número de entregas, caminhões e distâncias.
- Avaliar o tempo de execução e a eficiência das estruturas de dados.
- Comparar o desempenho com diferentes estruturas, como lista de adjacência vs. matriz
