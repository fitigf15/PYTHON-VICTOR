#Josep Boldu Quiros   niub:16287460
import networkx as nx

def arbre(G):
    connexo=nx.is_connected(G)                      #es comprova si el graf introduit es connex o no ([O(n)]
    if connexo == True:                             #Si el graf es connex:  [O(n)]
        if len(G.nodes()) > len(G.edges()):         #Es mira si el numero de vertes es mes gran que el numero de arestes perque per definicio un graf es un arbre si el seu numero d'arestes es inferior al seu numero de vertes i el graf es connex.   [O(n)]
            print "es un arbre"                     #com que hem cumplit les 2 condicions de que el graf es connex i el numero de vertex es inferior al numero de arestes podem dir que es un arbre.   [O(n)]
        else:                                       #Si no es aixi   [O(n)]
            print "no es un arbre"                  #Diem que el graf no es un arbre   [O(n)]
    else:                                           #I si no es cumpleix la primera condicio:   [O(n)]
        print "no es un arbre"                      #Directament ja es pot dir que el graf no es un arbre  [O(n)]
                

def main():
    G = nx.read_adjlist("arbres.txt",nodetype=int)  #Llegim el graf del arxiu arbres.txt   [O(n)]
    arbre(G)

main()
#COMENTARI: modifiqueu el arxiu "arbres.txt" per a fer les proves


#COMPLEXITAT: O(n)
#La complexitat es linial ja que nomes fem comprovacions de les dades introduides i no fem cap operacio complexa ni cap bucle dins de un altre bucle.
