import networkx as nx

def main():
    G = nx.Graph()
    G.add_edge("A","B")
    G.add_edge("A","C")
    G.add_edge("A","D")
    G.add_edge("B","C")
    G.add_edge("B","E")
    G.add_edge("C","D")
    G.add_edge("C","F")
    G.add_edge("E","F")
    G.add_edge("E","G")
    G.add_edge("F","H")
    G.add_edge("F","I")
    G.add_edge("G","H")
    G.add_edge("H","I")
    print shortest_route(G,"A","I")
    print dfs(G)
    
def main2():
    G = nx.Graph()
    G.add_edge("A","B")
    G.add_edge("A","D")
    G.add_edge("A","E")
    G.add_edge("A","F")
    G.add_edge("B","C")
    G.add_edge("C","D")
    G.add_edge("E","F")
    print dfs(G)
    print shortest_route(G,"A","E")
    
def shortest_route(G,u,v):
    nextLevel = [u]
    paths = {u:[u]}
    return shortest_route_r(G,u,v,nextLevel,paths)
def shortest_route_r(G,u,v,nextLevel,paths):
    if nextLevel:
        thisLevel = nextLevel
        nextLevel=[]
        for i in thisLevel:
            for j in G[i]:
                if j not in paths:
                    paths[j]=paths[i]+[j]
                    nextLevel.append(j)
        return shortest_route_r(G,u,v,nextLevel,paths)
    return paths 
def dfs(g):
    visited={}
    path=[]
    for v in g:
        if(v not in visited):
            explore(g,v,visited,path)
    return path, visited
def explore(g,v,visited,path):
    visited[v]=True
    path.append(v)
    for u in g[v]:
        if u not in visited:
            explore(g,u,visited,path)

           
def visit(G,u,v,visited,shortest):
    print "VISITING", u, "VISITED=",visited, "SHORTEST=",shortest
    visited.append(u)
    if(u==v):
        if len(visited)<len(shortest) and len(shortest)!=0:
            return shortest
    else:
        for i in G.neighbors(u):
            if i not in visited:
                visit(G,i,v,visited,shortest)
                
main()