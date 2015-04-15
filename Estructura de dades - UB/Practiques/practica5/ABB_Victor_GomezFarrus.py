import time
#ARTISTA
class SimpleNode:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Stack:
    def __init__(self):
        self.root=None
	self.items=0
    def isEmpty(self):
	return self.root==None
    def push(self,item):
        self.root=SimpleNode(data=item,next=self.root)
	self.items+=1
    def __getitem__(self,position):
	probe=self.root
	for i in range(position):
	    probe=probe.next
	return probe
    def __setitem__(self,position,value):
	probe=self.root
	for i in range(position):
	    probe=probe.next
	probe.data=value
    def pop(self):
	poppedItem=None
	if self.root:
	    poppedItem=self.root.data
	    self.root=self.root.next
	    self.items-=1
	else:
	    print "EMPTY STACK"
	return poppedItem
    def peek(self):
	if self.root:
	    return self.root.data
	else:
	    print "EMPTY STACK"
class ABBNode:
    def __init__(self,val,key,left=None,right=None):
	self.val=val
	self.key=key
	self.right=right
	self.left=left
    def addVal(self,value):
	if isinstance(self.val,list):
	    self.val.append(value)
	else:
	    self.val=[self.val,value]
    def children_count(self):
	count=0
	if not self.val or not self.key:
	    return None
	if self.left:
	    count+=1
	if self.right:
	    count+=1
	return count
    def __str__(self):
	if isinstance(self.val,list):
	    val=[]
	    for i in self.val:
		val.append(str(i))
	else:
	    val=self.val
	return "[VAL(S):"+str(val)+", KEY:"+str(self.key)+"]"

class ABB:
    #INICIALIZACION
    def __init__(self):
	self.root=None
	self.items=0
    #OBTENER TAMAÑO
    def getSize(self):
	return self.items
    #SABER SI ESTA VACIO
    def isEmpty(self):
	return self.root==None
    #PARA INSERTAR UN ELEMENTO
    def insert(self,val,key):
	if not(self.root):
	    self.root=ABBNode(val,key)
	    self.items+=1
	else:
	    actual=self.root
	    while actual:
		parent=actual
		if actual.key == key:
		    actual=None
		elif actual.key<key:
		    actual=actual.right
		else:
		    actual=actual.left
	    if parent:
		if parent.key>key:
		    parent.left=ABBNode(val,key)
		    self.items+=1
		elif parent.key<key:
		    parent.right=ABBNode(val,key)
		    self.items+=1
		else:
		    parent.addVal(val)
		    self.items+=1
    #PARA OBTENER UN ELEMENTO
    def search(self,key):
	n=self.root
	while True:
	    if n is None:
		return None
	    elif n.key == key:
		return n
	    elif n.key > key:
		n=n.left
	    else:
		n=n.right
    #PARA OBTENER UN SUBARBOL QUE CUMPLA UNAS CONDICIONES
    def from_to_search(self,fr,to):
	a=ABB()
	for i in self.inorder_conditioned(minim=fr,maxim=to):
	    if i.key>fr and i.key<to:
		a.insert(i.val,i.key)
	return a
    #PARA OBTENER UN ITEM COMO SI SE TRATASE DE UN ARRAY(ORDENADO)
    def __getitem__(self,position):
	index=0
	for i in self.inorder():
	    if position==index:
		return i
	    index+=1
    #BUSQUEDA DE UN ELEMENTO CON SU "PROGENITOR"
    def searchWithParent(self,key):
	parent=self.root
	node=parent
	if key>parent.key:
	    node=parent.right
	if key<parent.key:
	    node=parent.left
	while True:
	    if node is None:
		return None
	    elif node.key == key:
		if node is parent:
		    return node,None
		return node,parent
	    elif node.key >key:
		parent=node
		node=node.left
	    else:
		parent=node
		node=node.right
    #ELIMINAR ELEMENTO
    def remove(self,key):
	node,parent=self.searchWithParent(key)
	if node is not None:
	    if isinstance(node.val,list):
		if len(node.val)>1:
		    node.val=node.val[0:len(node.val)-1]
		    self.items-=1
		else:
		    node.val=node.val[0]
	    else:
		children_count=node.children_count()
		if children_count==0:
		    if not parent:
			self.root=None
		    elif parent.left is node:
			parent.left =None
		    else:
			parent.right=None
		    self.items-=1
		    #del node
		if children_count==1:
		    n=None
		    if node.left:
			n=node.left
		    else:
			n=node.right
		    if not parent:
			self.root=n		    
		    else:
			if parent.left is node:
			    parent.left=n
			else:
			    parent.right=n
		    self.items-=1
		    del node
		if children_count==2:
		    parent=node
		    successor=node.right
		    while successor.left:
			parent=successor
			successor=successor.left
		    node.key=successor.key
		    node.val=successor.val
		    if parent.left is successor:
			parent.left=successor.right
		    else:
			parent.right=successor.right
		    self.items-=1
	else:
	    print "THE KEY DOESNT EXIST"
    def from_to_remove(self,fr,to):
	for i in self.inorder_conditioned(minim=fr,maxim=to):
	    if i.key>fr and i.key<to:
		self.remove(i.key)
    #DE PRUEBAS, NO NECESARIO PARA LA PRACTICA
    def preorder(self):
	if self.root is not None:
	    stop=False
	    stack=Stack()
	    node=self.root
	    
	    while not stop:
		if node!=None:
		    if isinstance(node.val,list):
			for i in node.val:
			    yield ABBNode(i,node.key)
		    else:
			yield node
		    stack.push(node)
		    node=node.left
		else:
		    if not stack.isEmpty():
			node=stack.pop()
			node=node.right
		    else:
			stop=True  
    def inorder_conditioned(self,minim=0,maxim=0):
	if self.root is not None:
	    stop=False
	    stack=Stack()
	    node=self.root
	    while not stop:
		if node is not None:
		    stack.push(node)
		    node=node.left
		else:
		    if not stack.isEmpty():
			node=stack.pop()
			if node.key>minim and node.key<maxim:
			    if isinstance(node.val,list):
				for i in node.val:
				    yield ABBNode(i,node.key)
				    
			    else:
				yield node
			node=node.right
		    else:
			stop=True
    def inorder(self):
	if self.root is not None:
	    stop=False
	    stack=Stack()
	    node=self.root
	    while not stop:
		if node is not None:
		    stack.push(node)
		    node=node.left
		else:
		    if not stack.isEmpty():
			node=stack.pop()
			if isinstance(node.val,list):
			    for i in node.val:
				yield ABBNode(i,node.key)
			else:
			    yield node
			node=node.right
		    else:
			stop=True
#ARTISTA
class Artist:
    def __init__(self,name="EmptyName",playedSongs=0):
        self.name=name
        self.playedSongs=playedSongs
    def __cmp__(self,other):
        if self.playedSongs==other.playedSongs:
            return 0
        if self.playedSongs>other.playedSongs:
            return 1
        if self.playedSongs<other.playedSongs:
            return -1
    def getPlayedSongs(self):
        return self.playedSongs
    def __str__(self):
        return str(str(self.name)+" "+str(self.playedSongs)+"%")
#USUARIO
class User:
    def __init__(self,name="EmptyName",gender="emptyGender",age="EmptyAge",country="EmptyCountry", songs_played=[],most_played=[]):
        self.name=name
        self.gender=gender
        self.age=age
        self.country=country
        self.songs_played=songs_played
        self.most_played=most_played
        self.relevance=most_played.playedSongs
    def __str__(self):
        return "User:"+str(self.name)+"\nCountry:"+str(self.country)+"\nAge:"+str(self.age)+"\nMost Played:"+str(self.most_played)  
    def getMostPlayed(self):
        return "Artist:"+str(self.most_played.name)+"\nRelevance:"+str(self.relevance)
    def __cmp__(self,other):
        if float(self.relevance)==float(other.relevance):
            return 0
        if float(self.relevance)>float(other.relevance):
            return 1
        if float(self.relevance)<float(other.relevance):
            return -1
def inorderPrint(ABB):
    for i in ABB.inorder():
	print i.key
def preorderPrint(ABB):
    for i in ABB.preorder():
	print i.key
#EJECUCION DE CODIGO
#a=ABB()
#hacer las acciones correspondientes para testar y luego printar
#inorderPrint(a)
#preorderPrint(a)