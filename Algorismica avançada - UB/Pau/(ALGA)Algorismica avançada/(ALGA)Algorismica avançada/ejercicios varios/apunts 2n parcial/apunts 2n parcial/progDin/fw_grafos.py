INF = 999999999

def printSolution(distGraph):
    string = "inf"
    nodes =distGraph.keys()
    for n in nodes:
        print "\t%6s"%(n),
    print " "

    for i in nodes:
        print"%s"%(i),
        for j in nodes:
            if distGraph[i][j] == INF:
                print "%10s"%(string),
            else:
                print "%10s"%(distGraph[i][j]),
        print" "


def floydWarshall(graph):
    nodes = graph.keys()

    distance = {}

    for n in nodes:
        distance[n] = {}

        for k in nodes:
            distance[n][k] = graph[n][k]

    for k in nodes:
        for i in nodes:
            for j in nodes:
                distance[i][j] = min (distance[i][j], distance[i][k] + distance[k][j])
    printSolution(distance)

if __name__ == '__main__':
    graph = {   u'node_10': {   u'node_10': 0,
                u'node_4': 1,
                u'node_5': 0,
                u'node_6': 0,
                u'node_7': 0,
                u'node_8': 0,
                u'node_9': 0},
u'node_4': {   u'node_10': 0,
               u'node_4': 1,
               u'node_5': 1,
               u'node_6': 0,
               u'node_7': 0,
               u'node_8': 0,
               u'node_9': 0},
u'node_5': {   u'node_10': 0,
               u'node_4': 0,
               u'node_5': 0,
               u'node_6': 1,
               u'node_7': 0,
               u'node_8': 1,
               u'node_9': 0},
u'node_6': {   u'node_10': 0,
               u'node_4': 0,
               u'node_5': 0,
               u'node_6': 1,
               u'node_7': 1,
               u'node_8': 0,
               u'node_9': 0},
u'node_7': {   u'node_10': 0,
               u'node_4': 0,
               u'node_5': 0,
               u'node_6': 0,
               u'node_7': 1,
               u'node_8': 1,
               u'node_9': 0},
u'node_8': {   u'node_10': 0,
               u'node_4': 0,
               u'node_5': 0,
               u'node_6': 0,
               u'node_7': 0,
               u'node_8': 0,
               u'node_9': 1},
u'node_9': {   u'node_10': 1,
               u'node_4': 0,
               u'node_5': 1,
               u'node_6': 0,
               u'node_7': 0,
               u'node_8': 0,
               u'node_9': 0}}

floydwarshall (graph)
