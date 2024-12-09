
#Sujestão para modelagem e leitura do grafo

from pandas import read_csv

Alphabet = {
    'A' : 0,
    'B' : 1,
    'C' : 2,
    'D' : 3,
    'E' : 4,
    'F' : 5,
    'G' : 6,
    'H' : 7,
    'I' : 8,
    'J' : 9,
    'K' : 10,
    'L' : 11,
    'M' : 12,
    'N' : 13,
    'O' : 14,
    'P' : 15,
    'Q' : 16,
    'R' : 17,
    'S' : 18,
    'T' : 19,
    'U' : 20,
    'V' : 21,
    'X' : 22,
    'Y' : 23,
    'Z' : 24
 }

#Adjascency List:
graph = {
    'U' : ['P', 'V'],
    'V' : ['U', 'Q', 'X'],
    'P' : ['K', 'U'],
    'K' : ['P'],
    'Q' : ['L', 'V'],
    'X' : ['Y', 'V'],
    'F' : ['G', 'A'],
    'L' : ['M', 'Q'],
    'E' : ['M', 'S'],
    'Y' : ['X', 'Z'],
    'A' : ['B', 'A'],
    'G' : ['F', 'H'],
    'M' : ['L', 'N'],
    'S' : ['E', 'T'],
    'Z' : ['Y', 'T'],
    'B' : ['A'],
    'H' : ['G', 'C', 'I'],
    'N' : ['M', 'I','O'],
    'T' : ['S', 'Z'],
    'C' : ['H', 'D'],
    'I' : ['H', 'N'],
    'O' : ['N'],
    'D' : ['C', 'E'],
    'J' : ['E'],
    'E' : ['D', 'J'],
}


node_positions = {
    'U': (0, 0), 'V': (0, 1), 'X': (0, 2), 'Y': (0, 3), 'Z': (0, 4),
    'P': (1, 0), 'Q': (1, 1), 'E': (1, 2), 'S': (1, 3), 'T': (1, 4),
    'K': (2, 0), 'L': (2, 1), 'M': (2, 2), 'N': (2, 3), 'O': (2, 4),
    'F': (3, 0), 'G': (3, 1), 'H': (3, 2), 'I': (3, 3), 'J': (3, 4),
    'A': (4, 0), 'B': (4, 1), 'C': (4, 2), 'D': (4, 3), 'E': (4, 4)
}


def Graph():    #Consumindo o grafo em csv e retornando em matriz
    graph = read_csv('./data/Maze.csv')  #Consumindo csv
    graph.drop(['Unnamed: 0'], axis=1, inplace=True)
    return graph.to_numpy()



#graph = Graph()

# print(graph)

# print(graph[Alphabet['A']][Alphabet['F']])      # Verificando se existe uma aresta entre 2 vértices
