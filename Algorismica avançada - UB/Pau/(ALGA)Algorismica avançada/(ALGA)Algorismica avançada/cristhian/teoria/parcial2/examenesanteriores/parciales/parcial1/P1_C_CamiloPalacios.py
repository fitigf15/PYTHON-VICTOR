# nom: Angel Camilo Palacios Garzon

# ALGORISMICA AVANCADA - PRIMER PARCIAL - 02/11/2011 10:00 - C
#  
# Poseu el vostre nom a la primera linia. I renomeneu aquest 
# fitxer al format P1_A_nom_cognoms.py.
#
# Un cop realitzada la prova, torneu-lo a penjar al campus.

import networkx as nx
import heapq as pq

def main():
        G = llegir_graf() # O(V+E)
        #print biconnexe(G) # O(V+E)
        #print camins(G,1,4) #O(E log V)
        assegurarConnexions(G) # O(V^2)
        
        

# O(V+E)
def biconnexe(G):
        #Fem servir el return de la funcio punt_d_articulacio(G), si no hi ha cap punt d'articulacio es biconnex.
        if punt_d_articulacio(G)==-1: return True # O(V+E)
        else: return False

# O(4*(E log V)) = O(E log V)
def camins(G,u,v):
        G2=G.copy()
        cami1=dijkstra(G,u,v) # O(E log V)
        # Si el node de desti no es vei del d'origen esborrem tots els nodes entre l'origen i el desti
        # i trobem un cami amb els nodes restants.
        if v != cami1[1][1]:
                for i in cami1[1]:  #O(E log V)
                        if i!=u and i!= v:
                                G2.remove_node(i) #O(1)
                cami2=dijkstra(G2,u,v) # O(E log V)
        #Si el node de desti es vei del d'origen esborrem l'arista i trobem un nou cami.
        else:
                G2.remove_edge(u,v) #O(1)
                cami2=dijkstra(G2,u,v) # O(E log V)
        caminsTrobats=[]
        caminsTrobats.append(cami1[1]) # O(1)
        caminsTrobats.append(cami2[1]) # O(1)
        return caminsTrobats # O(1)

# O(V^2)
def assegurarConnexions(G):
        if biconnexe(G): # O(V+E)
                print "El graf es biconnexe"
                return 0
        else:
                G2=G.copy()
                u=punt_d_articulacio(G) # O(V(E+V))
                print "El node",u,"es un punt d'articulacio"
                #Si trobem un punt d'articulacio ens quedem amb els seus veins i l'esborrem
                G2.remove_node(u) # O(1)
                veins=[]
                for a in G.neighbors(u):
                        veins.append(a) # O(1)
                # Anem buscant camins amb dijkstra als nodes del graf sense el punt d'articulacio,
                # si no hi ha cami vol dir que estan a dos components connexes diferents, en tal cas
                # afegim una arista al graf inicial(amb el punt d'articulacio) i calculem els camins resultants
                # amb la funcio que haviem fet abans.
                for u in veins:
                        for v in veins:
                                cami= dijkstra(G2,u,v)[0] # O(E log V)
                                if not(cami):
                                        print "Afegeixo una aresta de",u,"a",v
                                        G.add_edge(u,v) # O(1)
                                        print camins(G,u,v) #O(E log V)
                                        return 0
                
        

def llegir_graf():						# O(V+E)

	#nom = input("Dona'm un nom pel graf: ")	# O(1)
	#nom = "ex1_biconnexe.dat"
	nom = "ex2_no_biconnexe.dat"
	P = nx.read_adjlist(nom,nodetype = int)	# O(V+E)				
	return P # O(1)

oo = 10000
def dijkstra(G,s,t):						# O(E log V)
	n = G.number_of_nodes()+1				# O(1)
	D = [oo]*(n+1)						# O(V)
	P = [-1]*(n+1)						# O(V)
	Q = []							# O(1)
	D[s] = 0							# O(1)
	pq.heappush(Q,[0,s])					# O(log V)
	for u in G:						# O(V)
		if (u != s):					# O(1)
			pq.heappush(Q,[oo,u])			# O(log V)

	while len(Q) > 0:					# O(V)
		d,u = pq.heappop(Q)				# O(log V)
		for v in G.neighbors(u):			# O(E/V)
			if (D[v] > D[u] + 1):			# O(1)
				D[v] = D[u] + 1			# O(1)
				P[v] = u     			# O(1)
				pq.heappush(Q,[D[v],v])	# O(log V)
	C = []							# O(1)
	hi_ha_cami = False					# O(1)
	if D[t] != oo:						# O(1)
		hi_ha_cami = True				# O(1)
		p = t							# O(1)
		while p != s:					# O(V)
			p = P[p]					# O(1)
			C.append(p)				# O(1)

		C.reverse()					# O(V)
		C.append(t)					# O(1)

	return hi_ha_cami,C					# O(1)

def dfs_visit(G,v): 						# O(E/V)

	global vistos
	vistos.append(v)						# O(log V)
	for u in G.neighbors(v):				# O(E/V)
		if u not in vistos:				# O(log V)
			dfs_visit(G,u)	

def dfs(G):							# O(V+E)

	global vistos
	q = 0								# O(1)
	vistos = []					
	for v in G:						# O(V)
		if v not in vistos:				# O(log V)
			q = q + 1
			dfs_visit(G,v)				# O(E/V)		
	return q							# O(1)

def numero_de_components(G): 				# O(V+E)

	return dfs(G)						# O(1)


def punt_d_articulacio(G):					# O(V(E+V))

	p = numero_de_components(G)				# O(V+E)
	for u in G:						# O(V)
		G2 = G.copy()					# O(V+E)
		G2.remove_node(u) 				# O(V)
		q = numero_de_components(G2)		# O(V+E)
		if q == p+1:					# O(1)
			return u					# O(1)

	return -1							# O(1)

main()
