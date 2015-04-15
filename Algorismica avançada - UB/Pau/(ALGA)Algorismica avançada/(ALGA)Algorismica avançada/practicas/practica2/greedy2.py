#Practica 2
#Autor: Artur Palaso Cera
#08/11/2013
#Complejidad en el peor de los casos: O(n^2)
#Complejidad en la mayoria de los casos: O(|V|*n)
import networkx as nx
    
def llegir_graf():
    #Lee el grafo de un fichero de texto
    #Complejidad O(n)
    nom = raw_input("Doneu el nom del graf: ")
    g = nx.read_adjlist(nom,nodetype = int)
    return g

def recubre_g():
    #Complejidad:
    #En el peor de los casos seria
    # O(n^2) que seria en el caso de que cada nodo estubiera sin conexion alguna.
    #Aunque este ejercicio trata de aprobechar las conexiones directas
    #para recubrir la mayor cantidad de nodos posibles por lo que en principio
    #siempre deberian haber conexiones.
    #Complejidad en la media de los casos(No se como representar bien el simbolo):
    # -O(|V|*n) como cada recubrimiento que hace recubre varios de su alrededor este nunca
    #lo hara el maximo de veces.
    g=llegir_graf()
    antenas = []                                        #Antenas cubiertas
    resultado = []
    num_nodos= len(g.nodes())                           #Totalidad de nodos del grafo
    while len(antenas) < num_nodos:                     #Mientras queden antenas por recubrir:
        a=[]
        for i in g.nodes(): a.append([len(g.neighbors(i)),g.neighbors(i),i]) #Vector de la forma: [num_vecinos,[vecinos], nodo],...
        maximo = max(a)                                 #Informacion del maximo
        num_antenas=len(antenas)                        #Cantidad de antenas cubiertas
        antenas.extend(maximo[1])                       #Anyade vecinos cubiertos por el nodo maximo
        antenas.append(maximo[2])                       #Anyadimos a el mismo como nodo recubierto
        antenas = list(set(antenas))                    #Si hay nodos duplicados los elimino y ordeno
        if(num_antenas < len(antenas)):                 #Comprobamos que los nodos nuevos recubiertos no estubieran ya en la lista
            resultado.append(maximo[2])
        g.remove_node(maximo[2])                        #Eliminamos nodo del grafo
    print resultado

recubre_g()
