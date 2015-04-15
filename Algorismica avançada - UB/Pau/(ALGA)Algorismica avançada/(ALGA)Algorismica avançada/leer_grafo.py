import networkx as nx
  
def llegir_graf():
    '''lee el grafo de un fichero de texto'''
    global Grafo
    Grafo = nx.Graph()
    nom = raw_input("Doneu el nom del graf: ")
    Grafo = nx.read_adjlist(nom,nodetype = int)
llegir_graf()
print Grafo.nodes()
print Grafo.edges()
