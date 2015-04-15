def llegit_graf():
    import networkx as nx
    G=nx.Graph()
    
#    nom=raw_input(" entreu el nom del fitxer amb el graf: ")
    nom="graf.txt"
    G = nx.read_adjlist(nom,nodetype=int)
#    G = nx.read_adjlist("graf.txt",nodetype=int)
    return G

def dfs(G,node):
    global visitats
    
    visitats.append(node)
    for u in G.neighbors(node):
        if (not u in visitats):
            dfs(G,u)
    return visitats

                

def main():
    G=llegit_graf()
    n = G.number_of_nodes()

    global visitats
    visitats = []
    final= G.number_of_nodes()
    cami= dfs(G,1)
    if 1 in G.neighbors(final):
        cami=cami+[1]
    else:
        print "Cal representar arestes"
 

    print "nodes :",(G.nodes())
    print "edges :",(G.edges())

    print "cami euleria :", cami
   
    
main()

