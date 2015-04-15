import networkx as nx
    
def llegir_graf():
    #Lee el grafo de un fichero de texto
    nom = raw_input("Doneu el nom del graf: ")
    g = nx.read_adjlist(nom,nodetype = int)
    return g
    
def info_nodos(g):
    nodos=g.nodes()
    dic={}
    for i in range(len(nodos)):
        dic[nodos[i]]=[len(g.neighbors(nodos[i])),g.neighbors(nodos[i])] # NODO: [Num vecinos, Vecinos]
    #for i in range(len(nodos)):
    #    print nodos[i], ": ", dic[nodos[i]][1]
    return dic

def recubre_g():
    g=llegir_graf()
    dic=info_nodos(g)
    antenas = []                                        #Vector de antenas cubiertas
    resultado = []                                      #Vector con antenas necesarias para cubrir todo el grafo
    while len(antenas) != len(g.nodes()):               #Mientras queden antenas por recubrir:
        maximo = max(dic, key=(lambda key: dic[key]))   #Nodo con maximo de vecinos
        num_antenas = len(antenas)                      #Cantidad de antenas cubiertas
        antenas.extend(dic[maximo][1])                  #Anyade nodos cubiertos por el nodo de maximo de vecinos
        antenas = list(set(antenas))                    #Si hay elementos duplicados los elimino y ordeno
        del(dic[maximo])                                #Eliminamos nodo de maximo devecinos
        
        #resultado.append(maximo)
        
#        print dic

#g=llegir_graf()
#dic=info_nodos(g)

recubre_g()
        

