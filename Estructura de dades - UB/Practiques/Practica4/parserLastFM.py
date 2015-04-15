import time

class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
#COLA
class Queue:
        def __init__(self):
		self.root=None
        def isEmpty(self):
		return self.root==None
        def printQ(self):
		print "---------------"
		if self.root !=None:
                        
		    probe=self.root
		    while probe!=None:
                            if probe.next==None:
                                    print probe.data
                                    probe=None
                            else:
                                    print probe.data
                                    probe=probe.next
                else:
                        print "Queue is empty"
                print "_______________"
                print "_______________"            
        def enqueue(self,item):
		node=Node(item)
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
#COLA DE PRIORIDAD
class PriorityQueue:
        def __init__(self):
		self.root=None
		self.size=0
        def isEmpty(self):
		return self.root==None
        def printQ(self):
		print "---------------"
		if self.root !=None:
		    probe=self.root
		    while probe!=None:
                            if probe.next==None:
                                    
                                    print probe.data.relevance
                                    probe=None
                            else:
                                    
                                    print probe.data.relevance
                                    probe=probe.next
                else:
                        print "Queue is empty"
                print "_______________"
                print "_______________"            
        def enqueue(self,item):
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
        def dequeue(self):
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
	def get(self,index):
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
#PARSER DE COLA NORMAL
def parser(user_file):
	"Parses the file of users"
	estructuraDeDatos = Queue()
	with open(user_file,'r') as usersFile:
	    for i in range(100):
		line=usersFile.readline()
		disks_played = []
		user_first = line.split("||")
		user_second = map(lambda x: x.split("&&"), user_first)
		user_disks = map(lambda x: x.split("::"), user_second[4])
		bestArtist=Artist("",0)
		for disk in user_disks:
			artist=Artist(name=disk[0],playedSongs=disk[1])
			disks_played.append(artist)
		user=User(name=user_second[0][0],gender=user_second[1][0],age=user_second[2][0],country=user_second[3][0],songs_played=disks_played,most_played=Artist(user_second[5][0],user_second[5][1]))
			      
		estructuraDeDatos.enqueue(user)
	return estructuraDeDatos
#PARSER DE COLA DE PRIORIDAD
#Prueba de diferencias entre yield y return
def priorityParser(user_file):
    estructuraDeDatos = PriorityQueue()
    with open(user_file,'r') as usersFile:
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
			  
	    yield user
def priorityParser2(user_file):
    estructuraDeDatos = PriorityQueue()
    with open(user_file,'r') as usersFile:
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
			  
	    estructuraDeDatos.enqueue(user)
    return estructuraDeDatos
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
		return str(self.name)
	def __cmp__(self,other):
	    #print [float(self.relevance),"VS",float(other.relevance),"->",float(self.relevance)>float(other.relevance)]
	    if float(self.relevance)==float(other.relevance):
		    return 0
	    if float(self.relevance)>float(other.relevance):
		    return 1
	    if float(self.relevance)<float(other.relevance):
		    return -1
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
#CODIGO DE PRUEBAS
t1=time.time()
a=parser("LastFM_small.dat")
print time.time()-t1
t1=time.time()		
b=PriorityQueue()
for i in priorityParser("LastFM_small.dat"):
    a.enqueue(i)
print time.time()-t1
t1=time.time()
c=priorityParser2("LastFM_small.dat")
print time.time()-t1