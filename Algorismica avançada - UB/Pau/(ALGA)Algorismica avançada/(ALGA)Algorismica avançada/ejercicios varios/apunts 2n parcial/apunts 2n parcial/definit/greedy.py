import networkx as nx
def ex1():
	G=nx.read_adjlist("g.txt", nodetype=int)
	nodos=[]
	for nodo in G.nodes():
		nodos.append((len(G.neighbors(nodo)),nodo,G.neighbors(nodo)))
	
	#nodos.sort()
	wifi=[]
	re=[]
	while(len(wifi)!=len(G.nodes())):
		n=max(nodos)
		m=len(wifi)
		wifi.extend(n[2])
		wifi = list(set(wifi)) #quita duplicados
		nodos.remove(n)
		if(m<len(wifi)):
			re.append(n[1])
	print re
ex1()
