# Practica 1
# Cristhian Carmona Torres


'''Internament tant les files com les columnes, comencen al 0. A l'hora de mostar resultats s'expresen tal com diu a la practica'''

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

tresors={} #Diccionari on es guarden els tresors trobats junt amb les seves coordenades
files=0	  #Nombre de files de l'arxiu de dades
cols=0	 #Nombre de columnes de l'arxiu de dades

def trobar_veins(nodo):
	'''Donat un node, retorna els seus nodes veins'''
	return G.neighbors(nodo['code'])

def print_trobat(n,G):
	'''
	Informa de la posicio i les passes necesaries per arribar als diferens tresors.Es possa apart com a funcio per fer el codi del algorisme més llegible i separar la sortida
	per pantalla de la logica del programa	
	'''
	print "Tresor a la fila "+str(tresors[n]['fila']+1)+" columna "+str(tresors[n]['columna']+1)+", accesible amb "+str(G.node[n]['distancia'])+" passes"

	
def print_inaccesibles():
	'''
	Informa dels tresors no accesibles al graf.Es possa apart com a funcio per fer el codi del algorisme més llegible i separar la sortida
	per pantalla de la logica del programa
	'''
	global tresors
	
	for tresor in tresors.keys():
		print "Tresor a la fila "+str(tresors[tresor]['fila']+1)+" columna "+str(tresors[tresor]['columna']+1)+" , innacesible."
	

def trobar_tresors(G,inici):
	global tresors
	
	cua=deque()
	cua.append(G.node[inici])
	G.node[inici]['visitat']=True
	pases=0
	
	while cua:

		node=cua.popleft()#treiem de la cua
		veins= trobar_veins(node)#mirem els nodes veins del node extret

		
		for  n in veins:
			if(G.node[n]['visitat']==False):
				G.node[n]['distancia']=node['distancia']+1
				if(G.node[n]['tipus']=='$'):
					print_trobat(n,G)
					del tresors[n]
				G.node[n]['visitat']=True
				cua.append(G.node[n])
				
def conecta(matriu,f,c,k):
	''' Conecta els nodes segons la informacio del arxiu de dades  '''
	valid_symb=['.','$']
	if(matriu[f][c] in valid_symb): #si es casella prohibida no la conectem
		try:
			
			if(c<(cols-1)):#Si estem a la última columna no cal mirar més a l'esquerra
				if((matriu[f][c+1] in valid_symb) ): #mirem a l'esquerra i si es casella valida afegim node
					G.add_edge(k,k+1)
		except:
			print "error buscant esquerra"+str(k)
		try:
			if(f<(files-1)):#Si es la ultima fila no busquem més avall
				if((matriu[f+1][c] in valid_symb) ):
					G.add_edge(k,k+12)
		except:
			print"error buscant avall"+str(k)

def print_matriu(matriu):
	'''Mostra un represntacion aproximada de la matriu amb les dades'''
	for linea in matriu:
		print linea

def omplir_graf(matriu,G):
	''' Recorre la matriu de dades i afegeix els nodes sense la codificacion de les caselles.Retorna un graf'''
	
	global files,cols,tresors
	
	k=0 #variable per enumerar els nodes
	for f in range(0,files):
		
		for c in range(0,cols):
			try:
				''' Recorre la matriu de dades i afegeix els nodes sense la codificacion de les caselles.Retorna un graf'''
				G.add_node(k,tipus=str(matriu[f][c]),visitat=False,code=int(k),distancia=0)
			except:
				print "Error creant node"
			else:
				if(matriu[f][c]=='$'):
					tresors[k]={'fila':f,'columna':c}
				conecta(matriu,f,c,k)
				k=k+1
	print "Hi ha "+str(len(tresors))+" tresors:"
	return G

	
G=nx.Graph()
omplir_graf(matriu,G)

trobar_tresors(G,0)
print_inaccesibles()


