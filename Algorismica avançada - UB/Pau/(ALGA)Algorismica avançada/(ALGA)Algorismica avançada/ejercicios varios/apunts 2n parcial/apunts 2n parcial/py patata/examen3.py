
# Algorismica 1 Prova 5 

def reverse(w):
    if len(w) == 2:
        return (w[1] + w[0]) # es gira el substring
    elif len(w) == 1: return w[0]
    else :
        n = len(w)/2
        return reverse(w[n:])+ reverse(w[:n]) # es va cridan recursivament en meitats


#----------------------------------------------------------------------------

def centre (A,b):
    k =  dicotomica(A,b)
    if len(A)-1 > k:
        while A[k+1] == b: k =k +1
    print k

def dicotomica(A,value): # cerca binaria que sempre retorna la posicio mes exacte del numero buscat
    low = 0
    high = len(A)-1
    while low <=high:
        mid = (low +high) /2
        if A[mid] > value: high = mid-1
        elif A[mid]< value: low = mid+1
        else: return mid
    return mid
