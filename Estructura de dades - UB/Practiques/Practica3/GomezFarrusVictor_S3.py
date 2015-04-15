##ENTREGA 3
##VICTOR GOMEZ FARRUS
##NIUB:16304886
##DNI:49184353A


#import random #no entiendo a que viene este import, lo pongo en comentario

#NODO
class Node:
        
	"Nodo simple enlazado necesario para implementar Stack y Queue"
	def __init__(self,data,next=None):
                
		"Inicializa un nodo con al menos un parámetro, data(información del nodo), el otro parámetro es opcional"
		"Ambos parámetros se pueden modificar. next es el puntero del nodo."
		self.data=data
		self.next=next
#PILA		
class Stack:
        
	"Secuencia de objetos ordenados donde los objetos se añaden y borran del mismo extremo (“top”)."
	"Es Last In First Out"
	"He considerado root el elemento del extremo top, ya que el puntero siempre irá “hacia abajo”."
	"Entonces solamente el primer elemento no apuntara a nada."
	def __init__(self):
                
		"Crea una pila vacía. No necesita parámetros y retorna una pila vacía."
		self.root=None
		
	def isEmpty(self):
                
		"Comprueba si la pila está vacía. No necesita parámetros y retorna un valor booleano."
		return self.root==None
	def printStack(self):
                
		"Imprime todos los elementos de la pila, en el caso que este vacía, avisará"
		#He implementado esto pensando que tenga uso general y no solamente para Movie
		#Los elementos en este caso son objetos Movie y se imprimen como tales
		#Hay en comentario un .getTitle() para imprimir el titulo de la pelicula acorde a lo que se pide en el pdf
		#Ya he comprobado anteriormente con elementos mas sencillos el funcionamiento de stack y es correcto
		print "---------------"
		if self.root == None:
                        
			print "Stack is empty!"
		else:
                        
			probe=self.root
			while probe!=None:
                                
				print probe.data#.getTitle() #-> imprimiria el titulo
				probe=probe.next
		print "_______________"
		print "_______________"
	def push(self,node):
                
		"Añade un nuevo elemento node al top de la pila. Necesita el elemento como parámetro y no retorna nada"
    
		newNext=self.root
		self.root=node
		self.root.next=newNext
		      
	def pop(self):
                
		"Borra el elemento del top de la pila. No necesita parámetros y retorna el elemento borrado del top."
    
		poppedItem=None
		if self.root!=None:
                        
                        poppedItem = self.root.data
                        if self.root.next is None:
                                
                                self.root = None
                        else:
                                
                                self.root.data=self.root.next.data
                                self.root.next=self.root.next.next
                        
		    
		else:
                        
                        print "Empty stack! Pop is not allowed!"
		return poppedItem

#COLA
class Queue:
        
	"Colección lineal ordenada donde los elementos se añaden por uno de los lados y se eliminan por el otro. "
	"Es First In First Out"
	"He considerado root el primer elemento elemento, ya que el puntero siempre irá “hacia el lado donde se añaden elementos”"
	"Entonces solamente el ultimo elemento no apuntara a nada."
	
        def __init__(self):
                
		"crea una cola vacía. No necesita argumentos y retorna una cola vacía."

		self.root=None
        def isEmpty(self):
                
		"comprueba si la cola está vacía. No necesita parámetros y retorna un valor booleano."

		return self.root==None
        def printQ(self):
                
		"Imprime todos los elementos de la cola, en el caso que este vacía, avisará"
		#He implementado esto pensando que tenga uso general y no solamente para Movie
		#Los elementos en este caso son objetos Movie y se imprimen como tales
		#Hay en comentario un .getTitle() para imprimir el titulo de la pelicula acorde a lo que se pide en el pdf
		#Ya he comprobado anteriormente con elementos mas sencillos el funcionamiento de queue y es correcto
		print "---------------"
		if self.root !=None:
                        
		    probe=self.root
		    while probe!=None:
                            
                            if probe.next==None:
                                    
                                    print probe.data#.getTitle() #-> imprimiria el titulo
                                    probe=None
                        
                            else:
                                    
                                    print probe.data#.getTitle() #-> imprimiria el titulo
                                    probe=probe.next
                else:
                        
                        print "Queue is empty"
                print "_______________"
                print "_______________"            
        def enqueue(self,node):
                
		"añade un nuevo elemento node a la cola. Necesita el elemento como argumento y no retorna nada."

		if self.root !=None:
                        probe=self.root
                        stop=False
                        while stop==False:
                                if probe.next!=None:
                                        probe=probe.next
                                else:
                                        probe.next=node
                                        stop=True
		else:
                        self.root=node

        def dequeue(self):
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
	
# MOVIE CLASS
class Movie:
	def __init__(self, title="emptyTitle",director=["emptyDirector"],cast = ["emptyCast"],
		         producer = ["emptyProducer"],writer = ["emptyWriter"],country = ["emptyCountry"],
		         language = ["emptyLanguage"],year = "emptyYear",genres = ["emptyGenres"],
		         votes = "emptyVotes", rating = "emptyRating", runtime = ["emptyRuntime"],
		         plot = ["emptyPlot"], cover_url = "emptyCorver"):
		
		    
		self.title = title
		self.director = director.split("&&")
		self.cast = cast.split("&&")
		self.producer = producer.split("&&")
		self.writer = writer.split("&&")
		self.country = country.split("&&")
		self.language = language.split("&&")
		self.year = year
		self.genres = genres.split("&&")
		self.votes = votes
		self.rating = rating
		self.runtime = runtime.split("&&")
		self.plot = plot.split("&&")
		self.cover_url = cover_url
	
	def getTitle(self):
		return self.title
		

# MAIN
def loadMovieList(filename):
	
	basedades=[]
	with open(filename,"r") as db:
		for line in db:                               #Creamos una base de datos de objetos Pelicula y devolvemos
			dades=line.split("|")
			movie=Movie(title=dades[0],director=dades[1],cast=dades[2],producer=dades[3],
		                    writer=dades[4],country=dades[5],language=dades[6],year=dades[7],
		                    genres=dades[8],votes=dades[9],rating=dades[10],runtime=dades[11],
		                    plot=dades[12],cover_url=dades[13])
			basedades.append(movie)
	
	return basedades


movieList = loadMovieList('peliculas100.dat')
## Reduce MovieList to 20 elements
movieList = movieList[0:20]

print "\n..................................\nTHIS IS TO TEST YOUR CODE - STACK\n..................................\n"
newStack = Stack()
newStack.printStack()

newNode = Node(movieList[0])
newStack.push(newNode)
newStack.printStack()

newStack.push(Node(movieList[1]))
newStack.printStack()

newStack.push(Node(movieList[2]))
newStack.printStack()

m1 = newStack.pop()
newStack.printStack()

m2 = newStack.pop()
newStack.printStack()

m3 = newStack.pop()
newStack.printStack()

m4 = newStack.pop()
newStack.printStack()

print m1.getTitle()
print m2.getTitle()
print m3.getTitle()

#print m4.getTitle() #Como que m4 es None, no tiene atributos y da error

print "\n..................................\nTHIS IS TO TEST YOUR CODE - QUEUE\n..................................\n"

newQ = Queue()
newQ.printQ()

newNode = Node(movieList[0])
newQ.enqueue(newNode)
newQ.printQ()

newQ.enqueue(Node(movieList[1]))
newQ.printQ()

newQ.enqueue(Node(movieList[2]))
newQ.printQ()

m1 = newQ.dequeue()
newQ.printQ()

m2 = newQ.dequeue()
newQ.printQ()

m3 = newQ.dequeue()
newQ.printQ()

m4 = newQ.dequeue()
newQ.printQ()

print m1.getTitle()
print m2.getTitle()
print m3.getTitle()
#print m4.GetTitle() #Como que m4 es None, no tiene atributos y da error
