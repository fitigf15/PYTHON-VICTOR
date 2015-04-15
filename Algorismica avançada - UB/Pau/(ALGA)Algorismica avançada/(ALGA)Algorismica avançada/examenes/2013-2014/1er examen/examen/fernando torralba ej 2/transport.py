#FERNANDO TORRALBA BARRABES
import networkx as nx

def leer_grafo():
    
    G = nx.Graph()
    nom = raw_input("Doneu el nom del graf: ")
    G = nx.read_adjlist(nom,nodetype = int)
    return G


def transport():
    G = leer_grafo()
    p =[8,3,5]
    q =[9,7]
    num_nodos = G.nodes()
    medida_p = len(p) 
    medida_q = len(q) 
    while(len(p) > 0): #Complejidad bucle while 0(n)
      maximo_p = 0
      maximo_q = 0
      for i in range (len(p)): #Complejidad bucle for 0(n) 
        if (p[i] > maximo_p):
          maximo_p = p[i] # vectores comienzan por 0,nodos por 1
          nodo_maximo_p = i+1
      
      for j in (G.neighbors(nodo_maximo_p)): #Complejidad bucle for 0(n)      
        if (q[j-medida_p-1] > maximo_q):
          maximo_q = q[j-medida_p-1]
          nodo_maximo_q = j
        
      if (p[nodo_maximo_p-1] > q[nodo_maximo_q-1-medida_p]): #listas enmìezan por 0
        p[nodo_maximo_p-1] = p[nodo_maximo_p-1] - q[nodo_maximo_q-1-medida_p]
        q[nodo_maximo_q-1-medida_p] = 0
        q.remove(0)

      elif (p[nodo_maximo_p-1] < q[nodo_maximo_q-1-medida_p]):
        q[nodo_maximo_q-1-medida_p] = q[nodo_maximo_q-1-medida_p] - p[nodo_maximo_p-1]
        p[nodo_maximo_p-1] = 0
        p.remove(0)

      else:
         p[nodo_maximo_p-1] = 0
         q[nodo_maximo_q-1-medida_p] = 0
         p.remove(0)
         q.remove(0)
         #Muestro las listas en cada iteracion, busqueda del maximo
      print "p",p 
      print "q",q

      #Complejidad de este algoritmo Greedy 0(n) de bulce while y 0(n) bucle for: 0(n^2)
transport()      
  
    
