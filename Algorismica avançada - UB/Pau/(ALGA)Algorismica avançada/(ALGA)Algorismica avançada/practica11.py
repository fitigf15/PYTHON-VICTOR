import networkx as nx
  
def llegir_graf():
    '''lee el grafo de un fichero de texto'''
    global Grafo
    Grafo = nx.Graph()
    nom = raw_input("Doneu el nom del graf: ")
    Grafo = nx.read_adjlist(nom,create_using=nx.DiGraph(),nodetype = int)

def crea_mat_adj():
    global mat_adj
    mat_adj = []
    num_nodes = Grafo.number_of_nodes()
    #mat_adj = [range(number_of_nodes) for i in range(number_of_nodes)]
    
    for i in range(num_nodes):
        mat_adj.append([])
        for j in range(num_nodes):
            mat_adj[i].append(0)
    
def busca_ciclo(origen):
    mat_adj[origen-1][origen-1] = 1 #Marcamos el nodo origen como visitado
    #print mat_adj
    #mat_adj[0][2]= 1
    vecinos = Grafo.neighbors(origen)
    print "Nodo: ",origen,": vecinos: ", vecinos
    if vecinos != []:
        for i in range(len(vecinos)):
            if mat_adj[origen-1][vecinos[i]-1]!=1:
                print "ESTA VISITADO? : ", origen-1," ", vecinos[i]-1
                mat_adj[origen-1][vecinos[i]-1] = 1
                print "vecinos[i]-1: ", vecinos[i]-1
                return busca_ciclo(vecinos[i])
    else:
        print "Vuelve hacia atras!!"
        return origen-2
    
llegir_graf()
crea_mat_adj()

busca_ciclo(1)
print mat_adj
#print Grafo.nodes()
#print Grafo.edges()
