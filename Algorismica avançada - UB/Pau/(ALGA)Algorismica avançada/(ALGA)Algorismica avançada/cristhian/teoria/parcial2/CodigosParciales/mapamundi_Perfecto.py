# nom: Cristhian Carmona Torres

import networkx as nx

def llegir_graf():						# O(V+E)
	#nom = raw_input("Doneu el nom del graf: ")	# O(1)
	nom = "cromatic_2.dat"
	G = nx.read_adjlist(nom,nodetype = int)		# O(V+E)
	return G							# O(1)

# EXERCICI 1
def mapamundi():
        todos = [0]*(G.number_of_nodes()+1)
        for n in G:
                colorVecinos = []
                
                for vec in G.neighbors(n):      # sacamos colores de vecinos
                        colorVecinos.append(todos[vec])
                ind = 1
                asignado = False

                while not(asignado):
                        if not(ind in colorVecinos):
                                todos[n] = ind
                                asignado = True                                
                        ind = ind + 1
                        
        return todos[1:]

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
	

def vertex_factible(v,c):
        '''retorna si el color asignado a v en el vector c es diferente al de sus vecinos, o no'''
        colores = []    # colores de vecinos de un nodo
        vertice_ok = False

        # si la posicion actual es cero(no ha sido visitada) entonces verifica vecinos
        if c[v]==0:

                # sacamos solo los colores de los vecinos
                for b in G.neighbors(v):
                        colores.append(c[b])

                # verificamos color a color si existe en sus vecinos
                i = 1
                while i<n:
                        if not(i in colores):
                                c[v]=i          # si no esta en los vecinos, lo agregamos y salimos
                                return True
                        i = i + 1
        #return vertice_ok
        return False


def factible(s):
        '''retorna si la solucion representada por el node de exploracion s es factible, o no'''
        fact = False

        # recorremos los nodos del grafo
        for nod in G:

                # verificamos si los vertices del nodo es factible
                if vertex_factible(nod, s.x):
                        return True
        return fact

def explora(s):
        '''hace el backtracking a partir del nodo de exploracion'''
        global z,x

##        print '======================'
##        print 'num nodos n:', n          # numero de nodos        
##        print 'num color i:', s.i          # numero de color
##        print 'vector colores x:', s.x          # vector para indexar los colores a partir del 1
##        print 'num colores de vector(x) z:', s.z()        # numero de colores de la solucion x
##        print '======================'

        # mejor de los casos
        if s.i==n:
                x = s.x
                z = s.z()
        else:
                # recorremos todos los nodos 
                for a in range(1, n):
                        
                        s.i = a         # informamos el campo del nodo
                        if factible(s): # enviamos nodo informado
                                s.i = s.i + 1   # sumamos uno al nodo actual
                                explora(s)
                                
        print 'Parte 2:', s.x

def escriu():			
        #print s.x
        
        return 0


def main():
	global G,n				# el graf i el nombre de nodes.
	global z,x				# millor solucio obtinguda.


	G = llegir_graf()
	n = G.number_of_nodes()

	s = node()
	z = 10000				# inicialitzem un maxim a oo.
	x = [0]*(1+n)                           # guardaremos los colores 
	print 'Parte 1: ', mapamundi()
	explora(s)
	#escriu()


main()



