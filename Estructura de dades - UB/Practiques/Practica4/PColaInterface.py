from Tkinter import *
import random
import time
#NODO
class Node:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next
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
        #print [float(self.relevance),"VS",float(other.relevance),"->",float(self.relevance)>float(other.relevance)]
        if float(self.relevance)==float(other.relevance):
            return 0
        if float(self.relevance)>float(other.relevance):
            return 1
        if float(self.relevance)<float(other.relevance):
            return -1
#COLA DE PRIORIDAD
class PriorityQueue:
    def __init__(self):
        self.root=None
        self.size=0
    def isEmpty(self):
        return self.root==None         
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
#INTERFAZ GRAFICA    
class userApp:
    def __init__(self,master,filepath):
        #FRAME
        self.frame=Frame(master)
        self.frame.pack()
        #STRINGVARS
        self.dataVar=StringVar()
        self.dataVar.set("User:"+"\nCountry:"+"\nAge:"+"\nMost Played:")
        self.addCostsVar=StringVar()
        self.addCostsVar.set("ADDING cost:")
        self.searchCostsVar=StringVar()
        self.searchCostsVar.set("SEARCHING cost:")        
        self.artistVar=StringVar()
        self.artistVar.set("Artist:"+"\n"+"Relevance:"+"\n")
        #ENTRIES
        self.fromRelevance=Entry(self.frame)
        self.fromRelevance.grid(row=1,column=1)
        self.toRelevance=Entry(self.frame)
        self.toRelevance.grid(row=2,column=1)
        #BUTTONS     
        self.addButton = Button(self.frame, text="ADD", command=lambda:self.addUser(filepath))
        self.addButton.grid(row=0,column=0,rowspan=3)
        self.searchButton = Button(self.frame, text="SEARCH",command=lambda:self.search(self.fromRelevance.get(),self.toRelevance.get(),filepath))
        self.searchButton.grid(row=0,column=1,sticky=W)
        self.displayNextButton = Button(self.frame, text="DISPLAY NEXT",command=lambda:self.dispNext())
        self.displayNextButton.grid(row=5,column=1)    
	##self.oneShotButton= Button(self.frame,text="ONESHOT",command=lambda:self.oneShot(filepath))
	##self.oneShotButton.grid(row=4,column=2,rowspan=2)
        
        #LABELS
        self.dataLabel=Label(self.frame, textvariable=self.dataVar)
        self.dataLabel.grid(row=4,column=0,rowspan=3)
        self.artistLabel=Label(self.frame, textvariable=self.artistVar)
        self.artistLabel.grid(row=4,column=1)
        self.addCostsLabel=Label(self.frame, textvariable=self.addCostsVar)
        self.addCostsLabel.grid(row=0,column=2,rowspan=2)
        self.searchCostsLabel=Label(self.frame, textvariable=self.searchCostsVar)
        self.searchCostsLabel.grid(row=2,column=2,rowspan=2)
        #OTHER ATTRIBUTES
        self.userList=PriorityQueue()
        self.idxItem=0
	#BOTON ONESHOT PARA COMPARACIONES
	##COSTS DATA
	##self.add_search_costs=[[],[]]
    ##def oneShot(self,filepath):
	##self.addUser(filepath)
	##self.addUser(filepath)
	##self.addUser(filepath)
	##self.addUser(filepath)
	##self.addUser(filepath)
	##print "ADDING COSTS:"+str(self.add_search_costs[0])
	##self.search(0,999,filepath)
	##self.search(0,1999,filepath)
	##self.search(0,2999,filepath)
	##self.search(0,3999,filepath)
	##self.search(0,4999,filepath)
	##print "SEARCHING COSTS:"+str(self.add_search_costs[1])        
    def addUser(self,filepath):
        t1=time.time()
        with open(filepath,'r') as usersFile:
            lines=usersFile.readlines()
            if(self.userList.getSize()+999>len(lines)):
                maxAdd=len(lines)-1
            else:
                maxAdd=self.userList.getSize()+999
            lines=lines[self.userList.getSize():maxAdd]
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
                self.userList.enqueue(user)
        self.dataVar.set(str(self.userList.getItem(self.idxItem)))
        self.artistVar.set(str(self.userList.getItem(self.idxItem).getMostPlayed()))     
	t2=time.time()-t1
        self.addCostsVar.set("ADDING cost:"+str(t2))  
	##self.add_search_costs[0].append(t2)
    def search(self,fromR,toR,filepath):
	if fromR!='' and toR!='':
	    t1=time.time()
	    self.userList=PriorityQueue()
	    with open(filepath,'r') as usersFile:
		lines=usersFile.readlines()
		for line in lines[int(fromR):int(toR)]:
		    disks_played = []
		    user_first = line.split("||")
		    user_second = map(lambda x: x.split("&&"), user_first)
		    user_disks = map(lambda x: x.split("::"), user_second[4])
		    bestArtist=Artist("",0)
		    for disk in user_disks:
			artist=Artist(name=disk[0],playedSongs=disk[1])
			disks_played.append(artist)
		    user=User(name=user_second[0][0],gender=user_second[1][0],age=user_second[2][0],country=user_second[3][0],songs_played=disks_played,most_played=Artist(user_second[5][0],user_second[5][1]))
		    self.userList.enqueue(user)
	    self.dataVar.set(str(self.userList.getItem(0)))
	    self.artistVar.set(str(self.userList.getItem(self.idxItem).getMostPlayed()))
	    t2=time.time()-t1
	    self.searchCostsVar.set("SEARCHING cost:"+str(t2))
	    ##self.add_search_costs[1].append(t2)
    def dispNext(self):
	if not self.userList.isEmpty():
	    self.idxItem+=1
	    if self.idxItem>=self.userList.getSize():
		self.idxItem=0
	    self.dataVar.set(str(self.userList.getItem(self.idxItem)))
	    self.artistVar.set(str(self.userList.getItem(self.idxItem).getMostPlayed()))
#EJECUCION DE CODIGO                      
root=Tk()
root.title("Users LastFM")
app=userApp(root,"LastFM_big.dat")
root.mainloop()