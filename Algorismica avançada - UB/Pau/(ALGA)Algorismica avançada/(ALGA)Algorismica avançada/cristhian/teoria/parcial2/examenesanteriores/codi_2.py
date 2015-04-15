# nom:

# ALGORISMICA AVANCADA - SEGON PARCIAL - 21/12/2011 8:00 - C
#  
# Poseu el vostre nom a la primera linia. I renomeneu aquest 
# fitxer al format P2_A_nom_cognoms.py.
#
# Un cop realitzada la prova, torneu-lo a penjar al campus.

import networkx as nx

def llegir_graf():						# O(V+E)
	nom = raw_input("Doneu el nom del graf: ")	# O(1)
	G = nx.read_adjlist(nom,nodetype = int)		# O(V+E)
	return G							# O(1)

# EXERCICI 1
def mapamundi():

	 # AFEGIU CODI AQUI

	return x

# EXERCICI 2
class node:
	def __init__(self):
		self.i = 0
		self.x = [0]*(1+n)	# per poder indexar els colors
						# a partir de l'1.
	def z(self):			# retorna el nombre de colors
						# de la solucio self.x
		q = 0
		for i in range(1,n+1):	# per cada color mirem
			nou = True		# si es nou a self.x...
			for j in range(1,i):
				if (self.x[i] == self.x[j]):
					nou = False
					break
			if nou: q = q + 1	# ...i si ho es, el contem.
		return q
	

def vertex_factible(v,c):		# retorna si el color 
						# assignat a v en el vector
						# c es diferent al dels 
						# seus veins, o no.
	 # AFEGIU CODI AQUI

	return True				# (modifiqueu aquesta linia)

def factible(s):				# retorna si la solucio repre-
						# sentada pel node d'exploracio
						# s es factible, o no.
	 # AFEGIU CODI AQUI

	return True				# (modifiqueu aquesta linia)

def explora(s):				# fa el backtracking a partir
						# del node d'exploracio s.

	global z,x				# millor solucio obtinguda.


	return				# (elimineu aquesta linia)


def escriu():				# escriu la solucio

	return				# (elimineu aquesta linia)

def main():
	global G,n				# el graf i el nombre de nodes.
	global z,x				# millor solucio obtinguda.


	G = llegir_graf()
	n = G.number_of_nodes()

	s = node()
	z = 10000				# inicialitzem un maxim a oo.
	x = [0]*(1+n)
	explora(s)
	escriu()


main()



