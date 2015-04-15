#NOTA: POR ALGUN ERROR QUE DEBO HABER COMETIDO NO ME FUNCIONABA TODO CON ARCHIVOS
#DIFERENTES ASI QUE LO HE UNIFICADO TODO EN ESTE ARCHIVO, DISCULPA LAS MOLESTIAS

from Tkinter import *
import random
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
    #HAY ALGO QUE NO ACABA DE FUNCIONAR BIEN Y NO ENCUENTRO QUE ES
    def from_to_remove(self,fr,to):
	for i in self.inorder_conditioned(minim=fr,maxim=to):
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

#INTERFAZ GRAFICA    
class userApp:
    def __init__(self,master,filepath):
        #FRAME
	self.filepath=filepath
        self.frame=Frame(master)
        self.frame.pack()
        #STRINGVARS
        self.dataVar=StringVar()
        self.dataVar.set("User:"+"\nCountry:"+"\nAge:"+"\nMost Played:")
        self.addCostsVar=StringVar()
        self.addCostsVar.set("ADDING cost:")
        self.searchCostsVar=StringVar()
        self.searchCostsVar.set("SEARCHING cost:")
	self.removeCostsVar=StringVar()
	self.removeCostsVar.set("REMOVING cost:")
        self.artistVar=StringVar()
        self.artistVar.set("Artist:"+"\n"+"Relevance:"+"\n")
        #ENTRIES
        self.fromRelevance=Entry(self.frame)
        self.fromRelevance.grid(row=1,column=1)
        self.toRelevance=Entry(self.frame)
        self.toRelevance.grid(row=2,column=1)
        #BUTTONS     
        self.addButton = Button(self.frame, text="ADD", command=lambda:self.addUser())
        self.addButton.grid(row=0,column=0,rowspan=3)
        self.searchButton = Button(self.frame, text="SEARCH",command=lambda:self.search(self.fromRelevance.get(),self.toRelevance.get()))
        self.searchButton.grid(row=0,column=1,sticky=W)
	self.removeButton=Button(self.frame,text="REMOVE",command=lambda:self.remove(self.fromRelevance.get(),self.toRelevance.get()))
	self.removeButton.grid(row=0,column=1,sticky=E)
        self.displayNextButton = Button(self.frame, text="DISPLAY NEXT",command=lambda:self.dispNext())
        self.displayNextButton.grid(row=5,column=1)    
	##BOTON ONESHOT PARA COMPARACIONES
	##self.oneShotButton= Button(self.frame,text="ONESHOT",command=lambda:self.oneShot())
	##self.oneShotButton.grid(row=5,column=2,rowspan=2)
        
        #LABELS
        self.dataLabel=Label(self.frame, textvariable=self.dataVar)
        self.dataLabel.grid(row=4,column=0,rowspan=3)
        self.artistLabel=Label(self.frame, textvariable=self.artistVar)
        self.artistLabel.grid(row=4,column=1)
        self.addCostsLabel=Label(self.frame, textvariable=self.addCostsVar)
        self.addCostsLabel.grid(row=0,column=2,rowspan=2)
        self.searchCostsLabel=Label(self.frame, textvariable=self.searchCostsVar)
        self.searchCostsLabel.grid(row=2,column=2,rowspan=2)
	self.removeCostsLabel=Label(self.frame,textvariable=self.removeCostsVar)
	self.removeCostsLabel.grid(row=3,column=2,rowspan=2)
        #OTHER ATTRIBUTES
        self.userList=None
        self.idxItem=0
	
	##COSTS DATA
	##self.add_search_remove_costs=[[],[],[]]
    ##def oneShot(self):
	##self.addUser()
	##self.remove(0,20)
	##self.search(0,20)
	##self.addUser()
	##self.remove(0,40)
	##self.search(0,40)
	##self.addUser()
	##self.remove(0,60)
	##self.search(0,60)
	##self.addUser()
	##self.remove(0,80)
	##self.search(0,80)
	##self.addUser()
	##self.remove(0,100)
	##self.search(0,100)
	##print "SEARCHING COSTS:"+str(self.add_search_remove_costs[1])
	##print "ADDING COSTS:"+str(self.add_search_remove_costs[0])
	##print "REMOVING COSTS:"+str(self.add_search_remove_costs[2])	
    def parser(self, fr=0,to=100):
	#NO TIENE SENTIDO AÑADIR DE 5000 EN 5000, porque el fichero solo contiene 5000 items
	#CADA VEZ QUE AÑADIMOS, EN VEZ DE AÑADIR HACEMOS UNA NUEVA LISTA
	self.userList=ABB()
	with open(self.filepath,'r') as usersFile:
	    lines=usersFile.readlines()
	    for line in lines:
		disks_played = []
		user_first = line.split("||")
		user_second = map(lambda x: x.split("&&"), user_first)
		user_disks = map(lambda x: x.split("::"), user_second[4])
		bestArtist=Artist("",0)
		for disk in user_disks:
		    artist=Artist(name=disk[0],playedSongs=disk[1])
		    disks_played.append(artist)
		user=User(name=user_second[0][0],gender=user_second[1][0],age=user_second[2][0],country=user_second[3][0],songs_played=disks_played,most_played=Artist(user_second[5][0],user_second[5][1]))
		if float(user.relevance)>float(fr) and float(user.relevance)<float(to):
		    self.userList.insert(user,int(float(user.relevance)*1000))	
    def addUser(self):
        t1=time.time()
	self.parser()
	self.idxItem=0
	self.dataVar.set(str(self.userList[self.idxItem].val))
        self.artistVar.set(str(self.userList[self.idxItem].val.getMostPlayed()))     
	t2=time.time()-t1
        self.addCostsVar.set("ADDING cost:"+str(t2))  
	#self.add_search_remove_costs[0].append(t2)
    def search(self,fromR,toR): 
	if fromR!='' and toR!='':
	    #EN ESTE CASO ES MAS EIFICIENTE AÑADIR CON CONDICIONES QUE CREAR UN SUBARBOL CON CONDICIONES
	    t1=time.time()
	    #ESTA ACCION AÑADE ELEMENTOS CON CONDICIONES AUNQUE NO CUMPLE CON LA DEFINICION DE "BUSCAR"
	    self.parser(fromR,toR)		  
	    #LA SIGUIENTE ACCION COMENTADA CREARIA UN SUBARBOL CON CONDICIONES CUMPLIENDO LA DEFINICION DE "BUSCAR"
	    #self.userList=self.userList.from_to_search(int(float(fromR)*1000),int(float(toR)*1000))
	    self.idxItem=0
	    self.dataVar.set(str(self.userList[self.idxItem].val))
	    self.artistVar.set(str(self.userList[self.idxItem].val.getMostPlayed()))
	    t2=time.time()-t1
	    self.searchCostsVar.set("SEARCHING cost:"+str(t2))
	    #self.add_search_remove_costs[1].append(t2)
    def remove(self,fromR,toR):
	if fromR!='' and toR!='':
	    #SE PODRIA AÑADIR CON CONDICIONES TAMBIEN AUNQUE NO CUMPLE LA DEFINICION DE "ELIMINAR"
	    t1=time.time()
	    #ESTA ACCION ELIMINA DEL ARBOL CON UNAS CONDICIONES, CUMPLIENDO LA DEFINICION DE "ELIMINAR"
	    self.userList.from_to_remove(int(float(fromR)*1000),int(float(toR)*1000))
	    if self.userList.items==0:
		self.dataVar.set("User:"+"\nCountry:"+"\nAge:"+"\nMost Played:")
		self.artistVar.set("Artist:"+"\n"+"Relevance:"+"\n")
		self.userList=None
	    else:
		self.idxItem=0
		self.dataVar.set(str(self.userList[self.idxItem].val))
		self.artistVar.set(str(self.userList[self.idxItem].val.getMostPlayed()))
	    t2=time.time()-t1
	    self.removeCostsVar.set("REMOVING cost:"+str(t2)) 
	    #self.add_search_remove_costs[2].append(t2)
    def dispNext(self):
	if self.userList:
	    self.idxItem+=1
	    if self.idxItem>=self.userList.items:
		self.idxItem=0
	    self.dataVar.set(str(self.userList[self.idxItem].val))
	    self.artistVar.set(str(self.userList[self.idxItem].val.getMostPlayed()))
#EJECUCION DE CODIGO                      
root=Tk()
root.title("Users LastFM")
app=userApp(root,"LastFM_small.dat")
root.mainloop()
