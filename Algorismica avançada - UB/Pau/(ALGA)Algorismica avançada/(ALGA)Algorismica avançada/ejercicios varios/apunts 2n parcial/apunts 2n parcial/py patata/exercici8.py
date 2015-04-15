import random
import math

# Definim la funcio d'avaluacio.
def puntx(r):
    
# Transformem els bits en un valor real x a l'interval [-1,2]
    sum=0.0
    for i in range(len(r)):
        sum = sum + r[i]*(2**i)
    x = -1.0 + sum * (3.0/(2.0**(len(r))-1.0))
    return x

def cost(r):
    # Avaluem el cromosoma x
    x = puntx(r)
    y = x * math.sin(10*math.pi*(x))+1.0
    return y

# Definim el creuament
def creuament(r1,r2): 
    i=random.randint(1,len(r1)-2)
    return r1[:i]+r2[i:], r2[:i]+r1[i:]

# Definim la mutació amb probabilitat mutprob per cada bit
def mutacio(r,mutprob):
    for i in range(len(r)):
        if random.random()<mutprob: 
            if r[i]==0: r[i]=1
            else: r[i]=0
    return r

# Creem la població inicial
def initpop(n,long):
    # Generem una poblacio de n cromosomes de longitud long. 
    import random
    pop = [[0] * long for x in range(n)]
    for i in range(n):
        for j in range(long):
            if random.random()>0.5: pop[i][j] += 1
    #for a in range(len(pop)): print pop[a]
    return pop

# Definim el proces de seleccio estandard
def seleccio_std(pop,cost,start=0):
    popsize=len(pop)
    # Calculem el valor minim de la funcio d'avaluacio   
    c =[cost(v) for v in pop[start:]]
    minim = min(c)
    # Normalitzem els valors de manera que el pitjor 
    # individu tingui un valor 0.01
    if minim<0.0: 
        for i in range(len(c)): 
            c[i] = c[i] + abs(minim) + 0.01
    else: 
        for i in range(len(c)): 
            c[i] = c[i] - minim + 0.01
    # Calculem la suma de tots els valors de la funcio d'avaluacio
    sum=0.0
    for i in range(len(c)): sum = sum + c[i]
    # Triem l'individu de forma proporcional al seu valor d'adaptacio 
    ran=random.random()*sum
    i = 0
    sum2=c[0]
    while ran > sum2: 
        i += 1
        sum2=sum2+c[i]
    # Retornem l'individu seleccionat
    return i+start

import time
def genetic(cost, cromsize=22, popsize=50, mutprob=0.01, maxiter=150):
    # Generem la població inicial
    t1 = time.clock()
    count = 0
    pop=initpop(popsize, cromsize)
    # Iterem fins al nombre de generacions
    for cont in range(maxiter):
        
        # Avaluem la generacio i l'ordenem
        scores = [(cost(v),v) for v in pop]
        count = count + len(pop)
        scores.sort(reverse=True)
        ranked=[v for (s,v) in scores]
        # Afegim els dos millors cromosomes a la següent generacío
        newpop=[0]*popsize
        newpop[0],newpop[1]=ranked[0],ranked[1]
        # Seleccionem les parelles 
        for i in range(0,popsize,2):        
            ind1=seleccio_std(ranked,cost,i)
            count = count + len(ranked)-i
            ranked[i],ranked[ind1]=ranked[ind1],ranked[i]
            ind2=seleccio_std(ranked,cost,i+1)
            count = count + len(ranked)-i+1
            ranked[i+1],ranked[ind2]=ranked[ind2],ranked[i+1]
        # Creuem les parelles i generem els fills
        new=[0]*popsize
        for i in range(0,popsize,2): 
            new[i],new[i+1] = creuament(ranked[i],ranked[i+1])
        # Mutem
        mut=[0]*popsize
        for i in range(popsize):
            mut[i]=mutacio(new[i],mutprob)
        # Afegim els pares (excepte els dos millors) a la generació
        mut = mut + ranked[2:]
        # Seleccionem la resta d'individus per la següent generació
        for i in range(2,popsize):
            newpop[i]=mut[seleccio_std(mut,cost,i)]
            count = count + len(mut)-i
        pop=newpop
        t2 = time.clock()
        
    print "f(x):", scores[0][0],
    print "x:", puntx(scores[0][1])
    print "temps trigat: %0.5f ms" %((t2-t1) *1000)
    print count, "avaluacions"

#-----------------------------------------------------------------------------

import random
import math

# Definim la funcio d'avaluacio.
def puntxy(r):
    
# Transformem els bits en un valor real x a l'interval [-6,6]
    sum=0.0
    for i in range(len(r)):
        sum = sum + r[i]*(2**i)
    x = -6.0 + sum * (12.0/(2.0**(len(r))-1.0)) # segons la funcio 
    return x

def cost2(r):
    # Avaluem el cromosoma x
    # el cromosoma es divideix en 2 parts, les posicions parells representran la posicio x i les impars la y
    k = 1
    if len(r)%2 == 0 : k =0
    # es crean dos "subcromosomes" de longitud len(r)/2 si len(r) es parell o de len(r)/2 + 1 si es senar
    rx = [-1]*((len(r))/2)
    ry = [-1]*(((len(r))/2)+k)
    countx = 0
    county = 0 
    for i in range(len(r)):
        if i%2 == 0:
            rx[countx] = r[i]
            countx += 1
        else :
            ry[county] = r[i]
            county +=1
            
    x = puntxy(rx)
    y = puntxy(ry)
    return 200 - (((x**2)+y-11)**2) - (x+(y**2)-7)**2

# Definim el creuament
def creuament(r1,r2): 
    i=random.randint(1,len(r1)-2)
    return r1[:i]+r2[i:], r2[:i]+r1[i:]

def mutacio(r,mutprob):
    for i in range(len(r)):
        if random.random()<mutprob: 
            if r[i]==0: r[i]=1
            else: r[i]=0
    return r

# Creem la població inicial
def initpop(n,long):
    # Generem una poblacio de n cromosomes de longitud long. 
    import random
    pop = [[0] * long for x in range(n)]
    for i in range(n):
        for j in range(long):
            if random.random()>0.5: pop[i][j] += 1
    #for a in range(len(pop)): print pop[a]
    return pop

# Definim el proces de seleccio estandard
def seleccio_std2(pop,cost2,start=0):
    popsize=len(pop)
    # Calculem el valor minim de la funcio d'avaluacio   
    c =[cost2(v) for v in pop[start:]]
    minim = min(c)
    # Normalitzem els valors de manera que el pitjor 
    # individu tingui un valor 0.01
    if minim<0.0: 
        for i in range(len(c)): 
            c[i] = c[i] + abs(minim) + 0.01
    else: 
        for i in range(len(c)): 
            c[i] = c[i] - minim + 0.01
    # Calculem la suma de tots els valors de la funcio d'avaluacio
    sum=0.0
    for i in range(len(c)): sum = sum + c[i]
    # Triem l'individu de forma proporcional al seu valor d'adaptacio 
    ran=random.random()*sum
    i = 0
    sum2=c[0]
    while ran > sum2: 
        i += 1
        sum2=sum2+c[i]
    # Retornem l'individu seleccionat
    return i+start

import time
def genetic2(cost2, cromsize=22, popsize=50, mutprob=0.01, maxiter=150):
    # Generem la població inicial
    t1 = time.clock()
    count = 0
    pop=initpop(popsize, cromsize)
    # Iterem fins al nombre de generacions
    for cont in range(maxiter):
        
        # Avaluem la generacio i l'ordenem
        scores = [(cost2(v),v) for v in pop]
        count = count + len(pop)
        scores.sort(reverse=True)
        ranked=[v for (s,v) in scores]
        # Afegim els dos millors cromosomes a la següent generacío
        newpop=[0]*popsize
        newpop[0],newpop[1]=ranked[0],ranked[1]
        # Seleccionem les parelles 
        for i in range(0,popsize,2):        
            ind1=seleccio_std2(ranked,cost2,i)
            count = count + len(ranked)-i
            ranked[i],ranked[ind1]=ranked[ind1],ranked[i]
            ind2=seleccio_std2(ranked,cost2,i+1)
            count = count + len(ranked)-i+1
            ranked[i+1],ranked[ind2]=ranked[ind2],ranked[i+1]
        # Creuem les parelles i generem els fills
        new=[0]*popsize
        for i in range(0,popsize,2): 
            new[i],new[i+1] = creuament(ranked[i],ranked[i+1])
        # Mutem
        mut=[0]*popsize
        for i in range(popsize):
            mut[i]=mutacio(new[i],mutprob)
        # Afegim els pares (excepte els dos millors) a la generació
        mut = mut + ranked[2:]
        # Seleccionem la resta d'individus per la següent generació
        for i in range(2,popsize):
            newpop[i]=mut[seleccio_std2(mut,cost2,i)]
            count = count + len(mut)-i
        pop=newpop
        t2 = time.clock()
    # es divideix el millor cromosoma en dos, per la representacio de les x i les y
    r = scores[0][1]
    k = 1
    if len(r)%2 == 0 : k =0
    rx = [-1]*((len(r))/2)
    ry = [-1]*(((len(r))/2)+k)
    countx = 0
    county = 0 
    for i in range(len(r)):
        if i%2 == 0:
            rx[countx] = r[i]
            countx += 1
        else :
            ry[county] = r[i]
            county +=1
        
    print "f(x):", scores[0][0]
    print "x: ", puntxy(rx),
    print " y: ", puntxy(ry)
    print "temps trigat: %0.5f ms" %((t2-t1) *1000)
    print count, "avaluacions"
    
#----------------------------------------------------------------------------------------------------------------------------------------------

def selectionsort(llista):
  n = len(llista)
  for i in range(0,n-1):
    k = i
    t = llista[i][0]
    t2 = llista[i]
    for j in range(i,n):
      if llista[j][0]> t:
        k = j
        t = llista[j][0]
        t2 = llista[j]
    llista[k] = llista[i]
    llista[i] = t2
  return llista

import time
def genetic3(cost2, cromsize=22, popsize=50, mutprob=0.01, maxiter=150):
    # Generem la població inicial
    t1 = time.clock()
    count = 0
    pop=initpop(popsize, cromsize)
    # Iterem fins al nombre de generacions
    for cont in range(maxiter):
        
        # Avaluem la generacio i l'ordenem
        scores = [(cost2(v),v) for v in pop]
        count = count + len(pop)
        scores = selectionsort(scores) # utilitza la funcio selectionsort per ordenar-se de major a menor
        ranked=[v for (s,v) in scores]
        # Afegim els dos millors cromosomes a la següent generacío
        newpop=[0]*popsize
        newpop[0],newpop[1]=ranked[0],ranked[1]
        # Seleccionem les parelles 
        for i in range(0,popsize,2):        
            ind1=seleccio_std2(ranked,cost2,i)
            count = count + len(ranked)-i
            ranked[i],ranked[ind1]=ranked[ind1],ranked[i]
            ind2=seleccio_std2(ranked,cost2,i+1)
            count = count + len(ranked)-i+1
            ranked[i+1],ranked[ind2]=ranked[ind2],ranked[i+1]
        # Creuem les parelles i generem els fills
        new=[0]*popsize
        for i in range(0,popsize,2): 
            new[i],new[i+1] = creuament(ranked[i],ranked[i+1])
        # Mutem
        mut=[0]*popsize
        for i in range(popsize):
            mut[i]=mutacio(new[i],mutprob)
        # Afegim els pares (excepte els dos millors) a la generació
        mut = mut + ranked[2:]
        # Seleccionem la resta d'individus per la següent generació
        for i in range(2,popsize):
            newpop[i]=mut[seleccio_std2(mut,cost2,i)]
            count = count + len(mut)-i
        pop=newpop
        t2 = time.clock()

    r = scores[0][1]
    k = 1
    if len(r)%2 == 0 : k =0
    rx = [-1]*((len(r))/2)
    ry = [-1]*(((len(r))/2)+k)
    countx = 0
    county = 0 
    for i in range(len(r)):
        if i%2 == 0:
            rx[countx] = r[i]
            countx += 1
        else :
            ry[county] = r[i]
            county +=1
        
    print "f(x):", scores[0][0]
    print "x: ", puntx(rx),
    print "   y: ", puntx(ry)
    print "temps trigat: %0.5f ms" %((t2-t1) *1000)
    print count, "avaluacions"
