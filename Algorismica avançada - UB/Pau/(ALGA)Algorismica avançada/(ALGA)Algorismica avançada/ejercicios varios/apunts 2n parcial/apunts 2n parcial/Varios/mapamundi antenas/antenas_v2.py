'''
Cristhian Carmona Torres
'''

import networkx as nx

def llegir_graf():
    #nom = raw_input("Donam un nom pel graf: ")
    nom = "antenas_2.dat"
    G = nx.read_adjlist(nom, nodetype = int)    
    return G


def antenes():
    aris = [0]*(n+1)    # contienes vectores de aristas de cada nodo
    global control      # vector auxiliar para controlar nodo con cobertura
    control = [0]*(n+1)

    # creamos el vector con vectores de vecinos
    for nd in G:
        vecinos = []
        for v in G.neighbors(nd):
            vecinos.append(v)
        aris[nd] = vecinos

    
    final = []  # vector donde iran las antenas

    for nd in G:                                  
        if (control[nd]==0) and (len(aris[nd])>1) and (cobertura(aris[nd])):
            control[nd]=1
            for aux in aris[nd]:
                control[aux]=1
            final.append(nd)
    return final


def cobertura(vecaris):
    suma=0
    for i in vecaris:
        suma=suma+control[i]
    if suma==0:
        return True
    return False

# Ejercicio 2
class node:
    def __init__(self,n):
        self.i = 0
        self.x = [False]*(1+n) # solucio en el node.
    def z(self):                # retorna la cardinalitat de S.
        q = 0
        for j in range(1,self.i+1):
            if self.x[j]: q = q + 1
        return q


def cobert(i,c):
    '''retorna si el vertice i queda cubierto con la solucion c, o no '''

def factible(s):
    '''retorna si el node de exploracion s representa una solucion factible, o no'''

def explora(s):
    ''' hace el backtrackin a partir del nodo s'''
    global z, x     # valor de la mejor solucion encontrada.

    print '==========Datos de entrada======='
    print 's.i:', s.i
    print 'Solucion en el nodo:', s.x
    print 'retorna la cardinalidad de S: ', s.z()
    print '-----------------------------------'
    for a in G:
        print a
##        for vec in G.neighbors(a):
##            print 'vecinos ', vec

def main():
    global G,n # el graf, i el nombre de vertexos.
    global z,x # valor de la millor solucio trobada.
    G = llegir_graf()
    n = G.number_of_nodes()

    #print antenes()
    
    #z = oo
    #x = [False]*n
    s = node(n)
    explora(s)
    #escriu()
main()
