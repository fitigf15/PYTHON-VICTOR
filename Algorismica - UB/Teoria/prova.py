import math
import random
import time
import string

def initpop(n,long):
    pop=[[0]*long for x in range(n)]
    for i in range(n):
        for j in range(long):
            if random.random()>0.5: pop[i][j] +=1
    return pop
def cost(r,interval):
    sum=0.0
    longitud=interval[1]-interval[0]
    for i in range(len(r)):
        sum=sum+r[i]*(interval[1]**i)
    x=interval[0]+sum*(longitud/(2**(len(r))-1.0))
    y= x*math.sin(10*math.pi*(x))+1.0
    return y
def mutacio(r,mutprob):
    for i in range(len(r)):
        if random.random()<mutprob:
            if r[i]==0: r[i]==1
            else: r[i]=0
    return r
def creuament(r1,r2):
    i=random.randint(1,len(r1)-2)
    return r1[:i]+r2[i:],r1[i:]+r2[:i]
        


x=0
fx=x*math.sin(10*(math.pi)*x)+1.0
def cercagenetica():
    
    interval=[-2,1]
    precisio=0.000001
    longitud=interval[1]-interval[0]
    mostreig=int(longitud/precisio)
    binmostreig=bin(mostreig)
    bits=len(binmostreig)-2
    print binmostreig
    print bits
    #xprima=int(2**bits)
    #x=interval[0]+xprima*(longitud/(xprima-1))
    t0=time.clock()
    a=initpop(150,bits)
    t1=time.clock()
    #Agafa el cromosoma mes gran
    for i in range(len(a)):
        b=cost(a[i],interval)
        mut=mutacio(a[i],0.01)
        creu=creuament(a[i],mut)
        if creu[1]>creu[0]:
            maxim=creu[1]
        else:
            maxim= creu[0]

        print maxim
        

        
    
    
cercagenetica()
