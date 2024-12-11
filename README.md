# COMPARAÇÃO DE ALGORITIMOS A-ESTRELA E BUSCA GULOSA: TRABALHO_2 INTELIGÊNCIA ARTIFICIAL 📚

## DESCRIÇÃO DO PROBLEMA 📖

O objetivo do trabalho a seguir é a comparação de dois algoritmos de Busca: A-estrela(A*) e Busca Gulosa(Greedy). Através do seguinte Labirinto

![Labirinto 1](</img/Labirinto.png>)

Foi montado um grafo para a realização das Buscas; Os pesos de cada Aresta foi associado como 1, e, a linguagem de implementação foi o Python.

## DESCRIÇÃO DE ALGORITMOS 🔧

### A-estrela (A*)

O algoritmo __A*__ equilibra os custos acumulados até o momento com a estimativa até o objetivo, garantindo que encontre o caminho mais curto se a heurística for admissível não superestimando o custo real. Sua função de avaliação é: __f(n) = g(n) + h(n)__;
* __g(n)__: É o custo real do caminho do nó inicial até o nó _n_.
* __h(n)__: É o custo do nó _n_ até o nó Objetivo (Calculado com a Heurística de Manhattam).

A escolha de nó se dá pelo que possui a menor __f(n)__.

### Busca Gulosa (Greedy) 

A Busca Gulosa foca exclusivamente em minimizar o custo estimado até o objetivo, ignorando os custos acumulados até o momento. Ela utiliza uma função heurística __h(n)__ que estima o custo do nó atual __n__ até o objetivo. A escolha de nós se dá pelo menor número calculado pela Heurística __H__, o algoritmo vai escolhendo o nó mais promissor até chegar no Objetivo.

## RESULTADOS 📉
### CAMINHOS ENCONTRADOS 🏴

* Busca Gulosa: __U->V->Q->L->M->N->I->H->C->D->E__.
* A-estrela:    __U->V->Q->L->M->N->I->H->C->D->E__.

Devido a implementação das arestas possuirem apenas peso '1', o valor avaliado nos dois algoritmos em suas funções de avaliação foi mesmo, no caso o valor feito pela heuristica de Manhattam (__h(n)__).

### COMPARAÇÃO TEMPO DE EXECUÇÃO ⏱️

* Busca Gulosa: 0.000020(±0.000008) segundos. 
* A-estrela:    0.000042(±0.000021) segundos.

Pela complexidade maior do A-estrela o seu tempo de execução foi maior, o caso em questão é um grafo simples onde as arestas possuem o mesmo peso, ABusca Gulosa obteve o mesmo resultado, que foi ótimo, com menor tempo que o A-estrela que garante o resultado ótimo, porém é mais custoso. A média do tempo e o desvio padrão foi calculado em 100 execuções.
### COMPARAÇÃO CUSTO DE MEMÓRIA 🧠

* Busca Gulosa: 0.10KB, 1.65KB (pico).
* A-estrela:    0.10KB, 3.11   (pico).

No algoritmo A-estrela há a necessidade de mais estruturas auxiliares, necessitando um maior uso de memória alocada, diferentemente da Busca Gulosa onde há a necessidade de menos estruturas auxiliares e calculos um pouco menos complexos.

### CONCLUSÕES 

Nos dois casos foi atingido o resultado ótimo, porém a Busca Gulosa se mostrou mais eficiente em tempo de exeução e custo de memória, devido àsimplicidade do problema; Em problemas mais complexos onde há grafos maiores e pesos diferentes associados à arestas, o algoritmo A-estrela sempre vai encontrar o resultado ótimo, já a Busca Gulosa não é garantida encontrar o resultado ótimo, porém vai possuir menor tempo de execução e memória.

### EXECUÇÃO
Clone o Repositório:

```
git clone git@github.com:joaopedrofreitas/Busca_Comparada-Greedy-A_star.git
```

Entre no diretório __src/__:

```
cd src
```

Execute o programa:

```
python3 main.py
```
