#####################################################################
#Data 26/10/2012     Programa: exercici5.py     Funció: mcd         #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################


#def fib1



def mcd():
    print "Entra 2 nombres sencers per calcular el seu MCD"
    m = input("Entra el primer nombre:")
    n = input("Entra el segon nombre:")
    while m != 0:
        n , m=m , n%m
    print n

#mcd()

def era1():                                    
    n = input("Entra fins a quin nombre vosl calcular els nombres primers:")
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

######era1()


import time
def era2():                           
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

era2()
