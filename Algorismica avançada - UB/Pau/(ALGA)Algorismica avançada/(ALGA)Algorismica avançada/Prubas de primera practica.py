import networkx as nx
A = nx.Graph()#Creamos un grafo
A.add_node("spam")#Anade nodo
A.add_edge("spam","spam2")#anade relacion, si el nodo relacionado no existe, lo crea.
A.add_node("spam3")
A.add_edge("spam4","spam5")
A.add_edge("spam","spam5")
print A.nodes()#Muestra Nombre nodos y su valor asi
print A.edges()#Muestra relaciones
print A.number_of_edges()#Muestra cantidad de arestas(relaciones)
print A.number_of_nodes()#Muestra cantidad de Nodos 
print "Vecinos del nodo 'spam': ", A.neighbors("spam") #Muestra vecinos de un nodo


#G=nx.read_adjlist("Nombre_fichero",nodetype=int) #Lee grafos en ficheros

G = nx.Graph()
G.add_edges_from([(1,2),(1,3),(2,3)])
print G.edges()
