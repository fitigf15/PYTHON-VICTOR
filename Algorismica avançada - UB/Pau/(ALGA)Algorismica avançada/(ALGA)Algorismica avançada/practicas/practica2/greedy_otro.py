import networkx as nx
def ex1():
	G= nx.Graph();
	G=nx.read_adjlist("gr.txt", nodetype=int)
	nodos=[]
	for nodo in G.nodes():
		nodos.append((len(G.neighbors(nodo)),nodo,G.neighbors(nodo)))
	
	#nodos.sort()
	wifi=[]
	re=[]
	while(len(wifi)!=len(G.nodes())):
		n=max(nodos)
		print "while", len(wifi),"!=",len(G.nodes())
		print "nodo max: ", n[1]
		m=len(wifi)
		print "len(wifi)-->m:", m
		wifi.extend(n[2])
		print "wifi1: ", wifi
		wifi = list(set(wifi)) #quita duplicados
		print "wifi2: ", wifi
		
		nodos.remove(n)
		print "nodos: ", nodos
		print "if(", m,"<",len(wifi),")"
		
		if(m<len(wifi)):        #Si hemos anyadido algun nodo recubierto nuevo
			re.append(n[1])
		print "RESULTADO: ", re
		print " "
	print re
ex1()
