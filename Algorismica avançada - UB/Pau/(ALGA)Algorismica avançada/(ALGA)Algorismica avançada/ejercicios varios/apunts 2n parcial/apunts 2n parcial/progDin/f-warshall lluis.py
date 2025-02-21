def adj(g):
    """
    Convert a directed graph to an adjaceny matrix.
    >>> g = {1: {2: 3, 3: 8, 5: -4}, 2: {4: 1, 5: 7}, 3: {2: 4}, 4: {1: 2, 3: -5}, 5: {4: 6}}
    >>> adj(g)
    {1: {1: 0, 2: 3, 3: 8, 4: inf, 5: -4}, 2: {1: inf, 2: 0, 3: inf, 4: 1, 5: 7}, 3: {1: inf, 2: 4, 3: 0, 4: inf, 5: inf}, 4: {1: 2, 2: inf, 3: -5, 4: 0, 5: inf}, 5: {1: inf, 2: inf, 3: inf, 4: 6, 5: 0}}
    """
    global vertices
    vertices = g.keys()
 
    dist = {}
    for i in vertices:
        dist[i] = {}
        for j in vertices:
            try:
                dist[i][j] = g[i][j]
            except KeyError:
                # the distance from a node to itself is 0
                if i == j:
                    dist[i][j] = 0
                # the distance from a node to an unconnected node is infinity
                else:
                    dist[i][j] = float('inf')
    return dist
 
 
def fw(g):

    # Para ejecutar algoritmo hacer en el shell g y h(los de mas abajo) y luego hacer fw(adj(h))
    """
    Run the Floyd Warshall algorithm on an adjacency matrix.
 
    The Floyd Warshall algorithm computes the minimum cost of a simple path between each
    pair of vertices.
     g = {1: {2: 3, 3: 8, 5: -4}, 2: {4: 1, 5: 7}, 3: {2: 4}, 4: {1: 2, 3: -5}, 5: {4: 6}}
    >>> fw(adj(g))
    {1: {1: 0, 2: 1, 3: -3, 4: 2, 5: -4}, 2: {1: 3, 2: 0, 3: -4, 4: 1, 5: -1}, 3: {1: 7, 2: 4, 3: 0, 4: 5, 5: 3}, 4: {1: 2, 2: -1, 3: -5, 4: 0, 5: -2}, 5: {1: 8, 2: 5, 3: 1, 4: 6, 5: 0}}
    >>> h = {1: {2: 1}, 2: {1 : 1, 3: -1}, 3: {2: -1}}
    >>> fw(adj(h))
    """ 
    d = dict(g)  # copy g
    for k in vertices:
        for i in vertices:
            for j in vertices:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
 
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
