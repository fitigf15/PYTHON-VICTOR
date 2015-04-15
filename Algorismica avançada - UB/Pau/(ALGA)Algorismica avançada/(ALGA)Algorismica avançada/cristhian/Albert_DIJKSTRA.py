import networkx as nx
import matplotlib.pyplot as plt

##def llegir_graf():
##    global G
##
####    nom = raw_input("Doneu el nom del graf: ")
####    nom = "mec.txt"
##    nom = "K:/Dropbox/3 any uni/AA/Practica/Dijkstra/graph.edgelist.txt"
##    G = nx.read_weighted_edgelist(nom,create_using=nx.Graph(),nodetype = int)
##    print G.nodes(data=True)
##    return G

def crear_graf():
    G=nx.Graph()
    G.add_edge(1,2,weight=8)
    G.add_edge(1,3,weight=1)
    G.add_edge(2,3,weight=4)
    G.add_edge(2,4,weight=2)
    G.add_edge(3,4,weight=7)
    G.add_edge(3,5,weight=5)
    G.add_edge(3,6,weight=12)
    G.add_edge(4,7,weight=1)
    G.add_edge(5,7,weight=4)
    G.add_edge(5,6,weight=6)

    print G.nodes(data=True)
    return G
    
def heap(G):
    h = []
    for node in G:
        h.append(node)
    return h

def deletemin(G,H):
    print "h: ",H
    u = H[0]
    for element in H:       #element es l' identificador del node 1,2,3,4,5,6...
        if G.node[element]['distancia']<G.node[u]['distancia']:
            u = element
    H.remove(u)
    print "min:",u,G.node[u]
    return u


    
def dijkstra(G,s):
    for node in G.nodes():
        G.node[node]['distancia'] = float('inf')
        G.node[node]['pare'] = None
        
    G.node[s]['distancia'] = 0

    H = heap(G)
    while H:            #mentres la cua de prioritats estigui plena
        u = deletemin(G,H)
        print "veins(u): ",G.neighbors(u)
        for vei in G.neighbors(u):
            weight = G[u][vei]['weight']
            if G.node[vei]['distancia'] > (G.node[u]['distancia']+weight):
                if G.node[vei]['distancia'] == float('inf'):
                    G.node[vei]['distancia'] = 0
                else:
                    G.node[vei]['distancia'] = G.node[u]['distancia']+weight
                    G.node[vei]['pare'] = u
          
    for i in range(0,len(G)):
        print G.nodes(data=True)[i]

            
def pinta_Graf(G):
    nx.draw(G)
    plt.show()






def main():
##    G = llegir_graf()
    G = crear_graf()
    dijkstra(G,3)
    
    
main()

