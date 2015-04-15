# exercici 5, Algorismica 1
# tots
#   15/11/09

def mcd():                                  # programa que dona el mcd utilitzant l'algoritme d'euclides
    m, n = input("Entra els dos nombres:")
    while m != 0: n, m=m, n%m
    print n

#---------------------------------------------------------------------------

import math
def eratostenes1():                                     #programa que dona tots els nombres primers fins a n
    n = input("Entra el final dels nombres primers:")
    llist = range (2,n+1)
    resul = []
    count = 0
    while count < len(llist):
        aux = llist.pop(0)
        resul.append(aux)
        for i in range (len(llist)):
            if aux != 0:
                if llist[i] % aux == 0 and i < len(llist): 
                    llist.insert(i,0)
                    k= llist.pop(i+1)
        count = count +1
    for a in range(len(resul)):
        if resul[a] !=0 : print(resul[a]),
    for b in range(len(llist)):
        if llist[b] !=0 : print(llist[b]), 

#-----------------------------------------------------------------------------
import time
def eratostenes2():                                 #programa que dona tots els nombres primers fins a 10000000, triga una miqueta
    n = 10000000
    llist = range (2,n+1)
    resul = []
    count = 0
    count2 = 0
    t1 = time.clock()
    while count < len(llist):
        aux = llist.pop(0)
        resul.append(aux)
        for i in range (len(llist)):
            if aux != 0:
                if llist[i] % aux == 0 and i < len(llist): 
                    llist.insert(i,0)
                    k= llist.pop(i+1)
        count = count +1
    t2 = time.clock()
    for a in range(len(resul)):
        if resul[a] !=0 :
            print(resul[a]),
            count2 = count2 + 1
    for b in range(len(llist)):
        if llist[b] !=0 :
            print(llist[b]), 
            count2 = count2 +1
    print
    print "El temps de proces de " ,n, "numeros ha estat %0.3f ms" %((t2-t1)*1000)
    print "Hi han ",count2, " numeros primers"

#-----------------------------------------------------------------------------
def erafermat():                                        # funcio que crea una llista am tots els nombres primers fins a 1000 i li envia a fermat1
    llist = range (2,1000)
    resul = []
    count = 0
    while count < len(llist):
        aux = llist.pop(0)
        resul.append(aux)
        for i in range (len(llist)):
            if aux != 0:
                if llist[i] % aux == 0 and i < len(llist): 
                    llist.insert(i,0)
                    k= llist.pop(i+1)
        count = count +1
    final=[]
    for a in range(len(resul)):
        if resul[a] !=0 : final.append(resul[a]),
    for b in range(len(llist)):
        if llist[b] !=0 : final.append(llist[b]), 
    return final

import time
def fermat1():                                      #programa que mira si es compleix el teorema petit de fermat per a tots els nombres primers menors de 100
    t0 = time.clock()                               # utilitzant la llista que crida a la funcio anterior
    lli = erafermat()
    for a in range(len(lli)):
        t1 =time.clock()
        print lli[a],
        if( lli[a] ** 1008 % 1009 == 1) :print "cert", ;
        else : print "false",;
        t2 = time.clock()
        print "%0.5f" % ((t2-t1)*1000), "ms"
    t3 = time.clock()
    print "ha trigat %0.5f ms " %((t3-t0)*1000)
    
#-------------------------------------------------------------------------------
def fermat2():
    lli = range(2,1001)
    t1 = time.clock()
    count = 0
    for i in range(len(lli)):
        a = 2
        t3 = time.clock()
        while(a < lli[i]): 
            if lli[i] % a == 0:
                if( lli[i] ** 1008 % 1009 == 1) :print lli[i] ," cert",
                else : print lli[i], " false",
                t4 = time.clock()
                print "%0.3f ms" % ((t4-t3)*1000)
                count = count +1
                break
            a = a +1
    t2 = time.clock()
    print "Numeros compostos entre 2 i 1000:",count
    print "Temps trigat a verificar tots els nombres compostos: %0.3f ms" % ((t2-t1)*1000)

#--------------------------------------------------------------------------------------------------------
def sr(n):                      
    r = n-1
    s=0
    while r%2== 0:
        r >>= 1
        s = s+1

    return s,r

def miller_rabin1():                    # programa que utilitzant l'algoritme de miller rabin diu si un nombres es probable primer o no
    n = input("entra una n:")
    s,r = sr(n)
    k = 100
    import random
    t1 = time.clock()
    for j in range(1,k):
        a = random.randint(2-1,n-2)
        y = (a ** r)%n
        if y!=1 and y!=(n-1):
            j=1
            while j<=(s-1) and y!=(n-1):
                y = (y**2)%n
                if y ==1:
                    print "Compost"
                    t2 = time.clock()
                    print "Ha trigat %0.5f ms" %((t2-t1)*1000) 
                    return
                j = j+1
            if y != (n-1):
                print "Compost"
                t2 = time.clock()
                print "Ha trigat %0.5f ms" %((t2-t1)*1000) 
                return
                
    print "Primer"
    t2 = time.clock()
    print "Ha trigat %0.5f ms" %((t2-t1)*1000)

#----------------------------------------------------------------------------------------------------
import random
def miller_rabin(n):
    r = n-1
    s = 0
    while r%2== 0:
        r >>= 1
        s = s+1
    k = 10
    for j in range(1,k):
        a = random.randint(2-1,n-2)
        y = (a ** r)%n
        if y!=1 and y!=(n-1):
            j=1
            while j<=(s-1) and y!=(n-1):
                y = (y**2)%n
                if y ==1: return 'Compost'
                j = j+1
            if y != (n-1):return 'Compost'
    return 'Primer'
    
def miller_rabin2():                                    #programa que utiltzant l'algosime de miller rabin conta el nombre de probables nombres primers fins a 
    t1 = time.clock()                                   # 10000000. Triga una mica
    count = 0
    for i in range(3,10000000):
        aux = miller_rabin(i)
        if aux =='Primer' : count = count + 1
    t2 = time.clock()
    print "Hi han ", count, " probables nombres primers"
    print "Ha trigat %0.5f ms" %((t2-t1)*1000)
    
