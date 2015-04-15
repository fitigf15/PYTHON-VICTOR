# Practica1 Ordenacion topologica de un grafo G.
# Cristhian Carmona Torres

# README! Ingresar fichero con extension. Ex: nombreFichero.txt

import networkx as nx


def llegir_graf():
    '''lee el grafo de un fichero de texto'''
    global Grafo
    Grafo = nx.Graph()
    nom = raw_input("Doneu el nom del graf: ")
    Grafo = nx.read_adjlist(nom,create_using=nx.DiGraph(),nodetype = int)
    return Grafo

def visit(G, n, visitados):
    '''Evalua el nodo del grafo si esta visitado o no'''
    visitados.add(n)
    for nbr in G.neighbors(n):
        if nbr not in visitados:
            visit(G, nbr, visitados)


def ordenTopo(G):
    """Recorre los nodos del grafo, devolviendo una lista de todos los nodos visitados"""
    visitados = set()
    for n in G:
        if n not in visitados:
            visit(G, n, visitados)            
    return visitados
            


G = llegir_graf()
print "Resultado de ordenacion topologica:"
# Imprimimos la lista de nodos
for x in ordenTopo(G):
    print x



"""
Analisis de eficiencia
----------------------------
Como el tiempo de ejecucion depende del ordenador utilizado y del compilador, no es posible
calcular su eficiencia exacta, sino que, lo estudiaremos para las siguientes situaciones:
i)Peor caso:
Numero de nodos sea n

ii)Mejor caso:
Numero de nodos sea 1

iii)Caso promedio: media(peor, mejor)
"""
