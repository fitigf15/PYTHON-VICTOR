# Cristhian Carmona Torres


import networkx as nx

def llegir_graf():
    '''lee el grafo de un fichero de texto'''
    global Grafo
    Grafo = nx.Graph()
    #nom = raw_input("Doneu el nom del graf: ")
    nom = "ge.txt"
    Grafo = nx.read_adjlist(nom,create_using=nx.DiGraph(),nodetype = int)
    return Grafo

def euleriano(G):
    esEuleriano = 0
    print "nodos", G.nodes()
    for n in G:
        act = len(G.neighbors(n))
        listaVecinos = G.neighbors(n)
        # print "nodo: ", n , "vecinos: ", listaVecinos
        tot = (act % 2)
        
        if (tot==0):                
            esEuleriano = 1
        else:
            esEuleriano = 0
            return 0
    return 1

