import networkx as nx

def llegir_graf():
    global G
    G = nx.Graph()


    nom = raw_input("Doneu el nom del graf: ")
    G = nx.read_adjlist(nom,create_using=nx.DiGraph(),nodetype = int)
    print 'Total de nodos: ', G.number_of_nodes()

    for n in G:
        print n

    for n in G:
        for nbr in G[n]:
            print 'nodo: ', n, ' tiene vecinos: ', nbr


    G.remove_node()
    

    for n in G:
        for nbr in G[n]:
            print 'nodo: ', n, ' tiene vecinos: ', nbr
    
    
    
llegir_graf()

