def floyd_warshall(w, n): 
    d = {0: w} 
    for k in range(1,n+1):
        d[k] = {} 
    for i in range(1,n+1):
        for j in range(1,n+1):
            d[k][i,j] = min(d[k-1][i,j],d[k-1][i,k] + d[k-1][k,j]) 
    return d[n]

w = {} 
w[1,2] = 3 
w[1,3] = 8 
w[1,5] = -4 
w[2,4] = 1
n=3
floyd_warshall(w, n)
    
