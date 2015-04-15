#Shortest path!!
'''
Example of Floyd-Warshall Algorithm for http://csalgorithm.wordpress.com/
@language: Python 3.1
@author: Wonjohn Choi
'''
hugeNumber = 999999999; #a really huge number for disconnected cities
 
#distance map
dist = (
            [0, 50, 200, 300, hugeNumber],
            [50, 0, 300, hugeNumber, 100],
            [200, 300, 0, 80, 500],
            [300, hugeNumber, 80, 0, 100],
            [hugeNumber, 100, 500, 100, 0]
    );
 
numNodo = len(dist)
 
def perform_Floyd_Warshall():
    '''
    The algorithm
    '''
    for i in range(numNodo):
        for j in range(numNodo):
            for k in range(numNodo):
                dist[i][k] = min(dist[i][k],dist[i][j]+dist[j][k])
 
print('Antes Distancia AE: %d'%dist[0][4])
 
perform_Floyd_Warshall()
for i in dist: print i
print('Despues Distanca AE: %d'%dist[0][4])
