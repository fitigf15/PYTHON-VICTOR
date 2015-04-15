import networkx as nx
  
def llegir_graf():
    #Lee el grafo de un fichero de texto
    global Grafo
    Grafo = nx.Graph()
    nom = raw_input("Doneu el nom del graf: ")
    Grafo = nx.read_adjlist(nom,nodetype = int)

def crea_mat_adj():
    #Crea una matriz de adjacencia inicializada toda a 0's
    #En esta podremos ver que nodo a visitado a quien y
    #si un nodo esta visitado por otro cuando estamos recorriendo
    #un camino.
    global mat_adj
    mat_adj = []
    num_nodes = Grafo.number_of_nodes() 
    mat_adj = [[0] * num_nodes for i in range(num_nodes)]
    
def busca_ciclo(origen,pila):
    #Funcion recursiva que obtiene el ciclo hamiltoniano o no en caso de que no existiera
    mat_adj[origen-1][origen-1] = 1                                 #Marcamos el nodo origen como visitado
    pila.append(origen)                                             #Anyadimos el nodo con el que trabajamos a la pila
    vecinos = Grafo.neighbors(origen)                               #Obtenemos los vecinos del nodo en el que trabajamos
    
    for i in range(len(vecinos)):
        if mat_adj[origen-1][vecinos[i]-1]!=1 and mat_adj[vecinos[i]-1][vecinos[i]-1]!=1: #Si El nodo actual no ha visitado al vecino, ni el vecino ha sido visitado por otro nodo:
            mat_adj[origen-1][vecinos[i]-1] = 1                     #Marco vecino que va a visitar
            mat_adj[vecinos[i]-1][origen-1] = 1                     #Marco el padre del vecino que va a visitar
            return busca_ciclo(vecinos[i],pila)                     #Llamamos a busca_ciclo con el nodo que va a visitar como nodo origen
        elif len(pila) == len(Grafo.nodes()) and vecinos[i] == 1:   #Si es ciclo hamiltoniano:
            pila.append(1)
            return pila

    if origen == 1:                                                 #Si ha llegado de nuevo al nodo 1 y sus vecinos ya estan todos visitados:
        return "Cal repassar arestes."
    
    for j in range(len(vecinos)):
        if mat_adj[origen-1][vecinos[j]-1]==1: mat_adj[origen-1][vecinos[j]-1] = 0                     #Marco vecinos como no visitados            
    mat_adj[origen-1][origen-1] = 0                                 #Marco el nodo actual como no visitado
    pila.pop()                                                      #Eliminamos el ultimo elemento de la pila
    return busca_ciclo(pila.pop(),pila)                             #Enviamos el nodo padre del nodo actual, lo eliminamos de la pila

def ciclo_ham():
    #Funcion principal que se encarga de crear y llamar las funciones necesarias para obtener el ciclo hamiltoniano
    llegir_graf()
    crea_mat_adj()
    pila = []
    ciclo = busca_ciclo(1,pila)
    return ciclo


ciclo = ciclo_ham()
print ciclo
