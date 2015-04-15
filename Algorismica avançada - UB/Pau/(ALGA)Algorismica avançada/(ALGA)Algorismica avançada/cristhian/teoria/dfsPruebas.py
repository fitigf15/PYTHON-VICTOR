import networkx as nx

def llegir_graf():
    '''lee el grafo de un fichero de texto'''
    global Grafo
    Grafo = nx.Graph()
    nom = raw_input("Doneu el nom del graf: ")
    nom = nom + ".txt"
    Grafo = nx.read_adjlist(nom,create_using=nx.DiGraph(),nodetype = int)
    return Grafo


def principal():
    G = llegir_graf()
    print "nodos"

    esBigrafo = True
    for n in G:
        G.node[n]['visited'] = False
        

    for n in G:
        print n
        for vec in G[n]:
            print "\t\tvecinos", vec



    return esBigrafo
    
print principal()
