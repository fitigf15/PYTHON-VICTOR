import networkx as nx

def llegir_graf():
    nom = raw_input("Dona un nom pel graf: ")
    G = nx.read_adjlist(nom)
    return G

def numero_de_components(G):
    return dfs(G)

def dfs(G):
    #Se puede modificar para guardar camino
    global vistos
    q = 0
    vistos = []
    for v in G:
        if v not in vistos:
            q = q + 1
            dfs_visit(G,v)
    return q

def dfs_visit(G,v):
    #avanza
    global vistos
    vistos.append(v)
    for u in G.neighbors(v):
        if u not in vistos:
            dfs_visit(G,u)

#------------------------------------------------

def punt_d_articulacio(G):
    p = numero_de_components(G)
    for u in G:
        G2 = G.copy()
        G2.remove_node(u)
        q = numero_de_components(G2)
        if q == p+1:
            return u
    return -1

G=llegir_graf()
num = numero_de_components(G)
print "Numero de componentes conexas= ", num
articulacio = punt_d_articulacio(G)
print "Articulacio: ", articulacio
