import networkx as nx


def llegir_graf():
    '''lee el grafo de un fichero de texto'''
    global Grafo
    Grafo = nx.Graph()
    nom = raw_input("Doneu el nom del graf: ")
    Grafo = nx.read_adjlist(nom,create_using=nx.DiGraph(),nodetype = int)
    return Grafo

class MyQUEUE:
    '''Clase Cola con funciones basicas para anadir, quitar y comprobar si tiene nodos'''
    def __init__(self):
        self.head = []
    def enqueue(self, nodo):
        self.head.append(nodo)
    def dequeue(self):
        self.probe = None
        try:
            self.probe = self.head[0]
            if len(self.head) == 1:
                self.head = []
            else:
                self.head = self.head[1:]	
        except:
               pass
        return self.probe	
            
    def IsEmpty(self):
            vacio = False
            if len(self.head) == 0:
                    vacio = True
            return vacio

def getVecinos(nodo):
    return G.neighbors(nodo['code'])

def iniDFS(G, inicio, path=[]):
    G.node()
    '''implementa el algoritmo dfs para un grafo de entrada'''
    q = [inicio]
    while q:
        v = q.pop(0)
        if v not in path:
            path = path + [v]
            q = grafo[v] + q
    return path


miQueue = MyQUEUE() # creamos una cola

iniDFS(grafo, "A", "D", miQueue)
#BFS(graph,"A","D",path_queue)





