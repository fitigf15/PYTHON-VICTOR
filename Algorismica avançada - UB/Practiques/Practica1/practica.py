
import matplotlib.pyplot as plt
import networkx as nx


def bfs(g,s):
    level=0
    nextLevel={s:1}
    paths={s:[s]}
    path=[s]
    while nextLevel:
        print "LEVEL:",level
        print "NEXTLEVEL:",nextLevel
        
        actualLevel=nextLevel
        nextLevel={}
        for v in actualLevel:
            print "G[",v,"]:",g[v]
            for w in g[v]:
                if w not in paths:
                    print w, "NOT IN",paths
                    paths[w]=paths[v]+[w]
                    nextLevel[w]=1
                    path.append(w)
        print "PATHS",paths
        print "CURRENT PATH",path
        level+=1
    return path

def dfs(g):
    visited={}
    path=[]
    for v in g:
        if(v not in visited):
            explore(g,v,visited,path)
    return path
def explore(g,v,visited,path):
    visited[v]=True
    path.append(v)
    print "INSPECTING NODE:",v
    for u in g[v]:
        print "-NODE EDGES TO INSPECT:", g[v]
        print "-INSPECTING EDGE:",u,"OF NODE:",v
        if u not in visited:
            print "--EDGE:",u,"NOT VISITED, INSPECTING AS NEW NODE"
            explore(g,u,visited,path)
        else:
            print "--EDGE:",u,"VISITED, SKIPPING"

def vertexs_connectats_aillats(g):
    connex_components=0
    connected={}
    for v in g:
        if len(connected)==0:
            connected[v]=connex_components
            for u in g[v]:
                connected[u]=connex_components
        else:
            if v in connected:
                for u in g[v]:
                    connected[u]=connex_components
            else:
                connex_components+=1
                connected[v]=connex_components
                for u in g[v]:
                    connected[u]=connex_components
    return connected
def canDelete(g,v):
    if len(g[v])>=2:
        for u in g[v]:
            return True
            
    return False
def find_punt_artic(g):
    punts={}
    for v in g:
        punts[v]=canDelete(g,v)
    return punts
def ex1():
    G = nx.Graph()
    V = [1, 2, 3, 4, 5]
    E = [[1, 2], [1, 4], [2, 3], [2, 5], [3, 5]]
    
    for i in V:
        G.add_node(i)
    for j in E:
        G.add_edge(j[0],j[1])
    print "number of edges: ",G.number_of_edges()
    print "number of nodes: ",G.number_of_nodes()
    print "edges: ",G.edges()
    print "nodes: ",G.nodes()   
    nx.draw(G)
    plt.show() 
    #solucio -> te 1 component connexe
def ex2():
    G = nx.Graph()
    V = [1, 2, 3, 4, 5]
    E = [[1,2],[1,3],[1,5],[2,4],[3,4],[3,5],[4,5]]
    for i in V:
        G.add_node(i)
    for j in E:
        G.add_edge(j[0],j[1])
    print "number of edges: ",G.number_of_edges()
    print "number of nodes: ",G.number_of_nodes()
    print "edges: ",G.edges()
    print "nodes: ",G.nodes()   
    print "matriu d'adjacencies: "
    print nx.adjacency_matrix(G)
    print "llista d'adjacencies: "
    print G.adjacency_list()
    nx.draw(G)
    plt.show()
    
def ex3():
    print "L'ordre d'un graf G(V,E) es el nombre de vertexs, |V|"
    print "La mida d'un graf G(V,E) es el nombre d'arestes, |E|"
    print "Per justificar la terminologia es pot utilitzar un graf simple i no dirigit"
    g=nx.Graph()
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(1,6)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(2,5)
    g.add_edge(2,6)
    g.add_edge(3,4)
    g.add_edge(3,5)
    g.add_edge(3,6)
    g.add_edge(3,8)
    g.add_edge(4,5)
    g.add_edge(4,7)   
    g.add_edge(9,10)
    print vertexs_connectats_aillats(g)

def ex4():
    g = nx.Graph()
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(1,6)
    g.add_edge(2,3)
    g.add_edge(2,4)
    g.add_edge(2,5)
    g.add_edge(2,6)
    g.add_edge(3,4)
    g.add_edge(3,5)
    g.add_edge(3,6)
    g.add_edge(3,8)
    g.add_edge(4,5)
    g.add_edge(4,7)
    b =  bfs(g,1)
    d = dfs(g)
    print b
    print d
    
def ex5():
    g = nx.Graph()
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(3,5)
    g.add_edge(4,5)
    print find_punt_artic(g)
     
def main():
    #ex1()
    #ex2()  
    ex3()
    #ex4()
    #ex5()
main()
