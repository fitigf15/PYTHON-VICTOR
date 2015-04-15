import networkx as nx
  
def llegir_graf():
    '''lee el grafo de un fichero de texto'''
    global Grafo
    Grafo = nx.Graph()
    nom = raw_input("Doneu el nom del graf: ")
    Grafo = nx.read_adjlist(nom,nodetype = int)

def crea_mat_adj():
    global mat_adj
    mat_adj = []
    num_nodes = Grafo.number_of_nodes()
    #mat_adj = [range(number_of_nodes) for i in range(number_of_nodes)]
    
    for i in range(num_nodes):
        mat_adj.append([])
        for j in range(num_nodes):
            mat_adj[i].append(0)
    
def busca_ciclo(origen,pila):
    print " "
    print "Origen: ", origen
    mat_adj[origen-1][origen-1] = 1 #Marcamos el nodo origen como visitado
    pila.append(origen) #Anyadimos el nodo con el que trabajamos a la pila
    print "Pila: ", pila
    #print mat_adj
    #mat_adj[0][2]= 1
    vecinos = Grafo.neighbors(origen)
    print "Nodo: ",origen,": vecinos: ", vecinos
    for i in range(len(vecinos)):
        print "Visitado? : vecino:", vecinos[i]
        if mat_adj[origen-1][vecinos[i]-1]!=1 and mat_adj[vecinos[i]-1][vecinos[i]-1]!=1: #Si El nodo actual no ha visitado al vecino, ni el vecino ha sido visitado por otro nodo:
            print "NO!"
            mat_adj[origen-1][vecinos[i]-1] = 1 #Marco vecino que va a visitar
            mat_adj[vecinos[i]-1][origen-1] = 1 #Marco al vecino que va a visitar de que nodo viene

            print mat_adj[0]
            print mat_adj[1]
            print mat_adj[2]
            print mat_adj[3]
            print mat_adj[4]
            
            return busca_ciclo(vecinos[i],pila)
        elif len(pila) == len(Grafo.nodes()) and vecinos[i] == 1: #Si es ciclo hamiltoniano:
            pila.append(1)
            return pila
            
    print "Vuelve nodo anterior!!"
    for j in range(len(vecinos)):
        if mat_adj[origen-1][vecinos[j]-1]==1:
            mat_adj[origen-1][vecinos[j]-1] = 0 #Marco vecino que va a visitar
            #mat_adj[vecinos[j]-1][origen-1] = 0 #Marco al vecino que va a visitar de que nodo viene
    mat_adj[origen-1][origen-1] = 0 #Marco el nodo actual como no visitado

    print mat_adj[0]
    print mat_adj[1]
    print mat_adj[2]
    print mat_adj[3]
    print mat_adj[4]
    pila.pop() #Eliminamos el ultimo elemento de la pila
    return busca_ciclo(pila.pop(),pila) #Enviamos el nodo padre del nodo actual, lo eliminamos de la pila 
llegir_graf()
crea_mat_adj()
pila = []
print Grafo.neighbors(3)
print Grafo.neighbors(4)
print Grafo.neighbors(5)
print Grafo.nodes()
print Grafo.edges()
ciclo = busca_ciclo(1,pila)
print ciclo
#print Grafo.nodes()
#print Grafo.edges()
