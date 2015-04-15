import networkx as nx
class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
class GraphNode:
    def __init__(self,data=None):
	self.data=data
	self.visited=False
    def __eq__(self,other):
	return (isinstance(other, self.__class__ ) and ( self.__dict__ == other.__dict__ ))
    def __ne__(self,other):
	return not __eq__(other)
    def __str__(self):
	return str(self.data)
class Queue:
        
    "Colección lineal ordenada donde los elementos se añaden por uno de los lados y se eliminan por el otro. "
    "Es First In First Out"
    "He considerado root el primer elemento elemento, ya que el puntero siempre irá “hacia el lado donde se añaden elementos”"
    "Entonces solamente el ultimo elemento no apuntara a nada."
    
    def __init__(self):
	    
	    "crea una cola vacía. No necesita argumentos y retorna una cola vacía."

	    self.root=None
	    self.size=0
    def isEmpty(self):
	    
	    "comprueba si la cola está vacía. No necesita parámetros y retorna un valor booleano."

	    return self.root==None        
    def enqueue(self,item):
	    
	    "añade un nuevo elemento node a la cola. Necesita el elemento como argumento y no retorna nada."
	    node=Node(item)
	    if self.root !=None:
		    probe=self.root
		    stop=False
		    while stop==False:
			    if probe.next!=None:
				    probe=probe.next
			    else:
				    probe.next=node
				    self.size+=1
				    stop=True
	    else:
		    self.root=node
		    self.size+=1

    def pop(self):
	"borra el primer elemento de la cola. No necesita parámetros y retorna el elemento."

	dequeuedItem=None
	if self.root !=None:
		dequeuedItem=self.root.data
		if self.root.next==None:
			
			self.root=None
						    
		
		else:
			probe=self.root
			self.root=probe.next
			dequeuedItem=probe.data
	    
	else:
		print "Empty Queue! Dequeue is not allowed!"
	return dequeuedItem
    def getItem(self,index):
	probe=self.root
	i=0
	item=None
	stop=False
	while stop==False:
	    if i==index:
		item=probe.data
		stop=True
	    else:
		i+=1
		probe=probe.next
	return item
    def getSize(self):
        return self.size
class Graph:
    def __init__(self):
	self.nodes=[]
	self.edges=[]
    def from_nodes_edges(self,n,e):
	"n = [1, 2, 3, 4, 5]"
	"e = [[1, 2], [1, 4], [2, 3], [2, 5], [3, 5]]"	
	for i in n:
	    self.nodes.append(GraphNode(i))
	for j in e:
	    self.edges.append([j[0],j[1]]) 
    def print_info(self):
	print "edges: "
	for i in self.edges:
	    print i
	print "nodes: "
	for j in self.nodes:
	    print j
	print "len edges: ",len(self.edges)
	print "len nodes: ",len(self.nodes)    
    def explore(self,n):
	if n in self.nodes:
	    visited=[]
	    print n.data
	    for i in self.edges:
		print i[0], "=",n
		print n.equals(i[0])
		visited.append(i[1])
	    return visited
	return None
def explore(nodes,edges,n):
    visited = [False]*len(nodes)
    if n in nodes:
	visited=[]
	print n
	for i in edges:
	    visited.append(n==i[0])
    return visited
def explore_r(g,v):
    n = GraphNode(v)
    n.visited = True
    for w in g.adjacentEdges(v)[v.data,len(g.edges)-1]:
	if(not w.visited): return explore_r(g,w)
def adjacency(nodes,edges,node=None):
    if node is None: return adjacency_all_r(nodes,edges,[])
    if node in nodes: return adjacency_r(edges,node,[])
    return "LOL"
def adjacency_all_r(nodes,edges,ad):
    if len(nodes)==0:
	ad.reverse()
	return ad
    
    a =edges[:]
    b = nodes.pop()
    ad.append(adjacency_r(a,b,[]))
    return adjacency_all_r(nodes,edges,ad)
    
def adjacency_r(edges,node,ad):
    if len(edges)==0:
	ad.reverse()
	return ad
    a = edges.pop()
    
    if(a[0]==node):
	ad.append(a[1])
    elif(a[1]==node):
	ad.append(a[0])
    print node, ad
    return adjacency_r(edges,node,ad)
    
    
g = Graph()
g1 = nx.Graph()
n = [1, 2, 3, 4, 5]
e = [[1,2],[1,3],[1,5],[2,4],[3,4],[3,5],[4,5]]
g1.add_nodes_from(n)
g1.add_edges_from(e)
#adj = adjacency(n,e,1)
adj2 = adjacency(n,e)
#g.from_nodes_edges(n,e)
#print explore(n,e,1)
	

