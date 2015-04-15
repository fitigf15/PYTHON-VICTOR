#Practica Greedy
#Autor: Artur Palaso Cera
#08/11/2013
import networkx as nx
    
def llegir_graf():
    #Lee el grafo de un fichero de texto
    nom = raw_input("Doneu el nom del graf: ")
    g = nx.read_adjlist(nom,nodetype = int)
    return g
    
def info_nodos(g):
    #Crea un diccionario donde --> nodo: [cantidad_vecinos,[vecinos]]
    nodos=g.nodes()
    dic={}
    for i in range(len(nodos)):
        dic[nodos[i]]=[len(g.neighbors(nodos[i])),g.neighbors(nodos[i])]
    return dic

def recubre_g():
    #Funcion Que se encarga de recubrir el grafo
    g=llegir_graf()
    dic=info_nodos(g)
    antenas = []                                        #Antenas cubiertas
    resultado = []                                      #Antenas necesarias para cubrir el grafo
    while len(antenas) != len(g.nodes()):               #Mientras queden antenas por recubrir:
        num_antenas = len(antenas)                      #Cantidad de antenas cubiertas
        maximo = max(dic, key=(lambda key: dic[key]))   #Nodo con maximo de vecinos
        antenas.extend(dic[maximo][1])                  #Anyade vecinos cubiertos por el nodo maximo
        antenas = list(set(antenas))                    #Si hay nodos duplicados los elimino y ordeno
        if(num_antenas < len(antenas)):                 #Comprobamos que los nodos nuevos recubiertos no estubieran ya en la lista
            resultado.append(maximo)
        del(dic[maximo])                                #Eliminamos nodo de maximo de vecinos
    print resultado
    
recubre_g()
        

