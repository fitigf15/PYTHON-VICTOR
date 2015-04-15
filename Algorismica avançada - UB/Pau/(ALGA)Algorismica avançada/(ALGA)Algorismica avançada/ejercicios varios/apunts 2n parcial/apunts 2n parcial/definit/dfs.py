def dfs_rec(graph,start,path = []):
    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path = dfs_rec(graph, edge,path)
    return path
graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}
print dfs_rec(graph,1)



def DFS(gr, s, path):
    """ Depth first search 
    Returns a list of nodes "findable" from s """
    if s in path: return False
    path.append(s)
    for each in gr.neighbors(s):
        if each not in path:
            DFS(gr, each, path)
			
			

procedure DFS(Graph,source):
      create a stack S
      push source onto S
      mark source
      while S is not empty:
          pop an item from S into v
          for each edge e incident on v in Graph:
              let w be the other end of e
              if w is not marked:
                 mark w
                 push w onto S