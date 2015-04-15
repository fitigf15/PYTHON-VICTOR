from itertools import permutations 

def solve(n): 
    cols = range(n) 
    for vec in permutations(cols):
        if (n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols))):
            print (map(lambda x:x+1, vec)) 

solve(8) 
