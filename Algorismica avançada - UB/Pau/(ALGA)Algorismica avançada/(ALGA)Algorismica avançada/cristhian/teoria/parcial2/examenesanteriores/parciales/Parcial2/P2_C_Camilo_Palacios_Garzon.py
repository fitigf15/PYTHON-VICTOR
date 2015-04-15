

# ALGORISMICA AVANCADA - SEGON PARCIAL - 21/12/2011 8:00 - C
#  
# Poseu el vostre nom a la primera linia. I renomeneu aquest 
# fitxer al format P2_A_nom_cognoms.py.
#
# Un cop realitzada la prova, torneu-lo a penjar al campus.

import networkx as nx

def llegir_graf():                      # O(V+E)
    #nom = raw_input("Doneu el nom del graf: ") # O(1)
    nom="cromatic_2.dat"
    G = nx.read_adjlist(nom,nodetype = int)     # O(V+E)
    return G                            # O(1)

# EXERCICI 1
def mapamundi():#O(n*m) n = num nodes, m = veins del node
        #utilitzo el vector X pels colors
        #Recorrem tots els nodes
        for n in G: #O(n)
                #Si el color es 0 voldra dir que no te cap color assignat
                if x[n]==0:
                        #Aqui guardo els colors dels veins
                        colorVeins=[]
                        #Recorrem els veins i guardem els seus colors.
                        for v in G.neighbors(n): #O(m)
                                colorVeins.append(x[v])
                        #Ara anem comprovant els colors que no podem repetir fins a arribar a un que no s'hagi utilitzat encara.
                        assignat=False
                        color=1
                        while(not(assignat)):
                                if not(color in colorVeins):
                                        x[n]=color
                                        assignat=True
                                else: color+=1
        return x

# EXERCICI 2
class node:
    def __init__(self):
        self.i = 0
        self.x = [0]*(1+n)  # per poder indexar els colors
                        # a partir de l'1.
    def z(self):            # retorna el nombre de colors
                        # de la solucio self.x
        q = 0
        for i in range(1,n+1):  # per cada color mirem
            nou = True      # si es nou a self.x...
            for j in range(1,i):
                if (self.x[i] == self.x[j]):
                    nou = False
                    break
            if nou: q = q + 1   # ...i si ho es, el contem.
        return q
    

def vertex_factible(v,c):#O(n) n--> num veins
        # retorna si el color
        # assignat a v en el vector
        # c es diferent al dels
        # seus veins, o no.
        for vei in G.neighbors(v):
                if c[vei]==c[v]and c[vei]!=0: return False
        return True

def factible(s):#O(n^2)
        # retorna si la solucio repre-
        # sentada pel node d'exploracio
        # s es factible, o no.
        for v in G: #O(n^2)
                if not(vertex_factible(v,s.x)): return False
        return True

def explora(s): # fa el backtracking a partir
        # del node d'exploracio s.
        global z,x # millor solucio obtinguda.
        # Cas trivial, tots tenen color assignat.
        if s.i==n:
                x=s.x
                z=s.z()
        #Cas no trivial
        else:
                print s.x
                #he posat aixo per pausar el programa
                raw_input("...")
                for q in range(1,n):
                        s.x[s.i+1]=q
                        if factible(s):
                                s.i=s.z()-1
                                explora(s)

def escriu():
        
        print "Exercici 2:\n",x
        
        
        

def main():
    global G,n              # el graf i el nombre de nodes.
    global z,x              # millor solucio obtinguda.


    G = llegir_graf()
    n = G.number_of_nodes()
    s = node()
    z = 10000               # inicialitzem un minim a oo.
    # 1)
    x = [0]*(1+n)
    #Guardo la sortida de la funcio mapamundi i trec el primer element que es un 0 sempre.
    colors = mapamundi()
    colors=colors[1:]
    print "Exercici 1:\n",colors,"\n\n"
    print "Exercici 2:\n"
    x = [0]*(1+n)
    explora(s)
    escriu()


main()


