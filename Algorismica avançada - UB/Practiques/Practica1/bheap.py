import networkx as nx

class BinaryHeap(object):
    __slots__=["__list","__size"]
    def __init__(self):
        self.__list = [0]
        self.__size=0
    def insert(self,k):
        self.__list.append(k)
        self.__size+=1
        self.percUp(self.__size)
        return
    def percUp(self,i):
        while i // 2 > 0:
            if self.__list[i] < self.__list[i//2]:
                tmp = self.__list[i//2] = self.__list[i]
                self.__list[i]=tmp
            i = i // 2
    def percDown(self,i):
        while (i*2) <=self.__size:
            mc = self.minChild(i)
            if self.__list[i] > self.__list[mc]:
                tmp  = self.__list[i]
                self.__list[i] = self.__list[mc]
                self.__list[mc] = tmp
            i = mc
    def minChild(self,i):
        if i*2+1>self.__size:
            return i*2
        else:
            if self.__list[i*2] < self.__list[i*2+1]:
                return i*2
            else:
                return i*2+1
    def popMin(self):
        if self.isEmpty():
            return None
        retVal = self.__list[1]
        self.__list[1]=self.__list[self.__size]
        self.__size -=1
        self.__list.pop()
        self.percDown(1)
        return retVal
    def isEmpty(self):
        return self.__size==0
    def isNotEmpty(self):
        return self.__size>0
    def fromList(self,otherList):
        i = len(otherList) // 2
        self.__size = len(otherList)
        self.__list = [0]+otherList[:]
        while i>0:
            self.percDown(i)
            i -=1
    def __len__(self):
        return self.__size
    
def dijkstra(graph,start):
    pqueue = BinaryHeap()
    distances = {}
    paths={start:[start]}
    visited = {start:0}
    count = 1
    pqueue.insert((0,count,start))
    itCount=0
    while pqueue.isNotEmpty():
        itCount+=1
        print "ITERATION NUMBER:",itCount
        (currentDistance,_,currentNode) = pqueue.popMin()
        print "-WORKING ON NODE:",currentNode, "WITH EDGES:" , graph[currentNode].items()
        if currentNode in distances:
            continue
        distances[currentNode]=currentDistance
        print "-CURRENT DISTANCE FROM START:",currentDistance
        iterator = iter(graph[currentNode].items())
        for currentEdge, edgeData in iterator:
            print "--WORKING ON EDGE:",currentEdge,"WITH DISTANCE FROM START:",distances[currentNode]
            newDistance = distances[currentNode] + edgeData.get("weight",1)
            print "--CHECKING NEW POSSIBLE DISTANCE:",newDistance
            if currentEdge not in visited or newDistance<visited[currentEdge]:
                print "---THE EDGE:",currentEdge,"WAS NOT CHECKED BEFORE OR HAS A NEW DISTANCE FROM START:",newDistance
                visited[currentEdge]=newDistance
                count+=1
                pqueue.insert((newDistance,count,currentEdge))
                paths[currentEdge] = paths[currentNode] + [currentEdge]
            else:
                print "---FOUND NOTHING INTERESTING"
        print "-DISTANCES: ", distances
        print "-PATHS: ", paths
    return [distances,paths]

def bellman_ford(graph,start):
    return 
    
            
                    
            
        

g = nx.Graph()
g.add_edge(1,2,weight=8)
g.add_edge(1,3,weight=1)
g.add_edge(2,3,weight=4)
g.add_edge(2,4,weight=4)
g.add_edge(3,4,weight=7)
g.add_edge(3,5,weight=5)
g.add_edge(3,6,weight=12)
g.add_edge(4,7,weight=1)
g.add_edge(5,6,weight=6)
g.add_edge(5,7,weight=4)
print dijkstra(g,3)
print nx.single_source_shortest_path(g,1)