# Oriol Suils Perez
# -*- coding: utf-8 -*-
import networkx as nx

# Aquest metode s'encarrega de llegir el fitxer on esta el graf i el posa a una variable,
# tambe agafa el primer node per poder començar.
def llegir_graf(): 
    global G, nodo #(1)
    nom = raw_input("Doneu el nom del graf: ") #(1)
    G = nx.read_adjlist(nom, create_using=nx.DiGraph(),nodetype= int) #()
    nodo = G.nodes()[0] #()

# Aquest es el metode que s'encarrega de fer l'ordenacio.
def inverted_topsort(G, vertex):
      sorted_list = [] #(1)
      visitat = {} #(1)

      for v in G.nodes(): #(V)
           visitat[v] = False #(1)

      dfs(G, vertex, visitat, sorted_list) #()

      return sorted_list #(1)

# Aquest metode es l'algorisme dfs una mica retocat.
def dfs(G, v, visitat, sorted_list):
      visitat[v] = True #(1)
      
      for w in G.neighbors(v): #()
           if not visitat[w]: #()
                dfs(G, w, visitat, sorted_list) #()

      sorted_list.append(v) #()

# Aquest es el metode principal i s'encarrega d'executar els metodes i executar la sortida
def main():
    llegir_graf() #()
    final = inverted_topsort(G, nodo) #(1)
    final.reverse() #(1)
    print final #(1)
 
main()
