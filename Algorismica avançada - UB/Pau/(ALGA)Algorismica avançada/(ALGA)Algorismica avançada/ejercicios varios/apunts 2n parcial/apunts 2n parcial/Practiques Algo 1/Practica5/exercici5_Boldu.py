#importem llibreries
import time
import math
import random

#####################################################################
#Data 26/10/2012     Programa: exercici5.py     Funció: fib1        #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def fib1(n):
    if n==1:
        return 1
    if n==0:
        return 0
    return fib1(n-1) + fib1(n-2)
       
def entrada():
    n=input("entra el numero n: ")
    t1 = time.clock()
    print "el resultat es:" , fib1(n)
    t2 = time.clock()
    print "El temps de proces ha estat %0.3f ms" % ((t2-t1)*1000)


#####################################################################
#Data 26/10/2012     Programa: exercici5.py     Funció: mcd         #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################

def mcd():
    print "Entra 2 nombres sencers per calcular el seu MCD"
    m = input("Entra el primer nombre:")
    n = input("Entra el segon nombre:")
    while m != 0:
        n , m=m , n%m
    print "El MCD dels 2 nombres es:" , n


#####################################################################
#Data 26/10/2012     Programa: exercici5.py     Funció: era1        #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
def era1():                                    
    n = input("Entra fins a quin nombre vols calcular els nombres primers:")
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


#####################################################################
#Data 26/10/2012     Programa: exercici5.py     Funció: era2        #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
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


#####################################################################
#Data 26/10/2012     Programa: exercici5.py     Funció: factorp     #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
def factorp():                           

    n = input('Entra n per saber si és un nombre primer: ')
    t1 = time.clock()
    primo = True
    for i in xrange(2,n):
        if n%i == 0:
            print '%s no es un nombre primer' %n
            primo = False
            break
    if primo:
        print '%s es un nombre primer' %n
    t2 = time.clock()
    print "El temps de proces ha estat %0.3f ms" %((t2-t1)*1000)



#####################################################################
#Data 26/10/2012     Programa: exercici5.py     Funció: fermatp     #
#                                                                   #
#Nom: Josep Boldú Quirós                Grup:B                      #
#####################################################################
import operator
def fermatp():
    n = input('Entra n per saber si és un nombre primer mitjançant la tècnica de Fermat: ')
    t1 = time.clock()
    a = [2,3,5]
    x=0
    for i in range(len(a)):
        if operator.mod(a[i]**(n-1),n) == 1:
            x=x+1
        else:
            x=x-1
    if x>0:
        print "El nombre es Primer"
    else:
         print "El nombre es Compost"
    t2 = time.clock()
    print "El temps de proces ha estat %0.3f ms" %((t2-t1)*1000)    




##Crida de funcions
##############################
##entrada()
##mcd()
##era1()
##era2()
##factorp()
##fermatp()












