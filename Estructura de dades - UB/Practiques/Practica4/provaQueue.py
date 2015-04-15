class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
    def __str__(self):
	return str(["DATA="+str(self.data),self.next])

class PriorityQueue:
        
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
        def enqueue(self,item):
                
		"añade un nuevo elemento node a la cola. Necesita el elemento como argumento y no retorna nada."
		node=Node(data=item)
		if self.root !=None:
                        probe=self.root
                        stop=False
                        while stop==False:
			    if probe.next!=None:
				if probe.data<node.data:
				    tmp=Node(data=probe.data,next=probe.next)
				    probe.data=node.data
				    probe.next=tmp
				    stop=True
				    self.size+=1
				else:
				    probe=probe.next
			    else:
				if probe.data<node.data:
				    tmp=Node(data=probe.data,next=probe.next)
				    probe.data=node.data
				    probe.next=tmp
				    self.size+=1
				else:
				    probe.next=node	    
				    self.size+=1
				    
				stop=True
		else:
		    self.root=node
		    self.size+=1
		print self.size
		

        def dequeue(self):
		"borra el primer elemento de la cola. No necesita parámetros y retorna el elemento."

		dequeuedItem=None
		if self.root !=None:
                        dequeuedItem=self.root.data
                        if self.root.next==None:
			    self.root=None
                        else:
			    self.root=self.root.next
		else:
                        print "Empty Queue! Dequeue is not allowed!"
		return dequeuedItem
	
q=PriorityQueue()
q.enqueue(3)
q.enqueue(5)

q.enqueue(12)
q.enqueue(55)
q.enqueue(54)
q.enqueue(79)
q.enqueue(11)
q.enqueue(53)
q.enqueue(123)
q.enqueue(0)
q.printQ()