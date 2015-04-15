import networkx as nx

def explore(G,v):
    visited = set()
    stack = [v]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print G[vertex]
            print visited
            #stack.extend(G[vertex]-visited)
    return visited
        
def dfs(graph,start,visited=None):
    #graph = {'A': set(['B', 'C']),
    #        'B': set(['A', 'D', 'E']),
    #         'C': set(['A', 'F']),
    #         'D': set(['B']),
    #         'E': set(['B', 'F']),
    #         'F': set(['C', 'E'])}    
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph,next,visited)
    return visited
G = nx.Graph()
V = [1, 2, 3, 4, 5]
E = [[1,2],[1,3],[1,5],[2,4],[3,4],[3,5],[4,5]]
for i in V:
    G.add_node(i)
for j in E:
    G.add_edge(j[0],j[1])
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print dfs(graph,'A')
#print explore(G,1)