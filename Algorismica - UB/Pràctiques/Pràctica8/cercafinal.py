import math
import random
import time
import string

#Tot aquest bloc es el quicksort que hem vist a la teoria.
#Aquesta funcio la utilitzarem en varies funcions de la practica

#Aquesta funcio estableix un pivot per poder fer el quicksort
def partition(A, first, last): 
    sred = (first + last)/2
    if A[first] > A [sred]: A[first], A[sred] = A[sred], A[first]
    if A[first] > A [last]: A[first], A[last] = A[last], A[first]
    if A[sred] > A[last]: A[sred], A[last] = A[last], A[sred]
    A [sred], A [first] = A[first], A[sred]
    pivot = first
    i = first + 1
    j = last

    while True:
        while i<= last and A[i] <=A[pivot]: i += 1
        while j>= first and A[j] >A[pivot]: j -= 1
        if i >= j: break
        else:
            A[i], A[j] = A[j], A[i]
    A[j], A[pivot] = A[pivot], A[j]
    return j
#Aquesta funcio recursiva es la base del quicksort
def quick_sort_r(A , first, last):
    if last > first:
        pivot = partition(A, first, last)
        quick_sort_r(A, first, pivot - 1)
        quick_sort_r(A, pivot + 1, last)
#Aquesta es la funcio principal del quicksort
def quick_sort(A):
    quick_sort_r(A, 0, len(A) - 1) 

#Les funcions recursives que he fet tenen l'estructura establerta a la teoria

def initpop(n,long):
    pop=[[0]*long for x in range(n)]
    for i in range(n):
        for j in range(long):
            if random.random()>0.5: pop[i][j] +=1
    return pop
def funcio(x):
    y= x*math.sin(10*math.pi*(x))+1.0
    return y
def func1d(x):
    y= x*math.sin(10*math.pi*(x))+1.0
    return y
def cost(r,interval):
    sum=0.0
    longitud=interval[1]-interval[0]
    for i in range(len(r)):
        sum=sum+r[i]*(interval[1]**i)
    x=interval[0]+sum*(longitud/(2**(len(r))-1.0))
    y=funcio(x)
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

def returnposicio1d(r,interval):
    sum=0.0
    longitud=interval[1]-interval[0]
    for i in range(len(r)):
        sum=sum+r[i]*(interval[1]**i)
    x=interval[0]+sum*(longitud/(2**(len(r))-1.0))
    return x
def cost1d(r,interval):
    
##    sumx=0.0
    
##    for i in range(len(r)):
##        sumx=sumx+r[i]*(interval[1]**i)
    longitud=interval[1]-interval[0]
    binari=''
    for i in range(len(r)):
        binari=binari+str(r[i])
    sumx=int(binari,2)
    x=interval[0]+sumx*(longitud/(2**(len(r))-1.0))
    y=func1d(x)
    return y
def cercafinal(interval,precisio,generacions,mutprob):
    t0=time.clock()
    xmax=0
    longitud=interval[1]-interval[0]
    mostreig=int(longitud/precisio)
    binmostreig=bin(mostreig)
    bits=len(binmostreig)-2
    #print "bits=",bits
    maxtotal=[0]*bits
    costmaxtotal=cost1d(maxtotal,interval)
    supervivent=[0]*bits
    for i in range(generacions):
##        print
##        print "-----------------------------------------------------"
##        print
##        print "                     GENERACIO ",i
##        print
##        print "-----------------------------------------------------"
##        print
        
        a=initpop(50,bits)
        progenit1=[0]*bits
        progenit2=[0]*bits
        costprogenit=[cost1d(progenit1,interval),cost1d(progenit2,interval)]
        for j in range(len(a)):
            individu=a[j]
            costindividu=cost1d(individu,interval)
            if costindividu>costprogenit[0]:
                progenit1=individu
                costprogenit[0]=costindividu
                #print "NOU progenit2=",progenit1
            if costindividu>costprogenit[1] and costindividu<costprogenit[0]:
                progenit2=individu
                costprogenit[1]=costindividu
                #print "NOU progenit2=",progenit2
        fill=creuament(progenit1,progenit2)
        taulafill=[fill[0],fill[1]]
        taulafill[0]=mutacio(taulafill[0],mutprob)
        taulafill[1]=mutacio(taulafill[1],mutprob)
        if cost(taulafill[0],interval)>cost1d(taulafill[1],interval):
            supervivent=taulafill[0]
##            supervivents.append(taulafill[0])
        else:
            supervivent=taulafill[1]
##            supervivents.append(taulafill[1])

        costsupervivent=cost1d(supervivent,interval)
        print "supervivent=",costsupervivent,", pos=",returnposicio1d(supervivent,interval)
        if costsupervivent>costmaxtotal:
            maxtotal=supervivent
            costmaxtotal=cost1d(maxtotal,interval)
            print
            print "maxim ",cost1d(maxtotal,interval), ", pos=",returnposicio1d(maxtotal,interval)
            print
    xmax=returnposicio1d(maxtotal,interval)
    t1=time.clock()

    print "El valor maxim de la funcio mostrejada cada ",precisio," es ",costmaxtotal,", a la posicio ",xmax, "."
    print "Hem fet ",generacions*len(a)," avaluacions i hem trigat ", t1-t0, " segons."
    
    return cost(maxtotal,interval)
    


def cercagenetica(interval,precisio,generacions,mutprob):
    maxim=cercafinal(interval,precisio,generacions,mutprob)
    print maxim
cercagenetica([-1,2],0.000001,150,0.01)
            
            
    
    
