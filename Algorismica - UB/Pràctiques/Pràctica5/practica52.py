 
# -*- coding: utf-8 -*-


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                     #PRACTICA5

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                    #Victor Gomez Farrus
                                    #Enginyeria Informatica
                                    #Algorismica
                                    #Grup B


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Importem les llibreries

import time #Importem la llibreria time
import math #Importem la llibreria math
import operator #Importem la llibreria operator

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def era1(n): #Definim la funcio que depen de la variable n
    llistaA=range(2,n) #La llista llistaA tindra els valors de 2 a n
    llistaB=list() #La llista llistaB es una llista buida
    while llistaA[0]<math.sqrt(n): #Mentre es compleixin les condicions establertes en l'exercici proposat
        llistaB.append(llistaA[0]) #Afegirem la primera posicio de llistaA a llistaB
        num=llistaA[0] #la variable num valdra aixo
        del llistaA[0] #Eliminarem la primera posicio de llistaA, pero el valor eliminat seguira existint dins la variable num
        multiples = range(num,n,num) #La variable multiples sera una llista de tots els valors de num fins a n, pero en intervals de num, es a dir, multiples de num
        for i in multiples: #Per cada element de la llista multiples
            if i in llistaA: #Si tenim l'element dins llistaA
                llistaA.remove(i) #Eliminarem l'element de llistaA
    for i in llistaA: #Per cada element de llistaA
        llistaB.append(i) #L'afegiram a llistaB per fer una representacio mes senzilla, ja que els numeros de llistaA son els numeros primers que van despres de llistaB fins arribar a n
    print "Els nombres primers menors o iguals que N son:", llistaB #Imprimirem tots els numeros primers
    return llistaB

n=input("introdueix un nombre")
def factorp(n): #Definirem la funcio que depen de la variable n
    t1=time.clock()
    primers = era1(n) #La variable primers tindra els valors de llistaB, que es una llista de nombres primers. Aquest pas es simplement per aclarir el procediment, ja que ho podriem fer directament amb llistaB
    p = 0 #La variable p valdra 0
    primer = True
    while p < len(primers): #Mentre es compleixi aquesta condicio
        if n%primers[p]==0: #Si es compleix aquesta condicio
            primer=False #La variable booleana primer sera falsa, per tant, el nombre no sera primer, ja que es divisible entre un dels nombres de la llista primers
            print "No es primer" #En consequencia, imprimirem que no es primer
            break #Tallarem el programa perque no necessitem fer mes operacions
        else: #Si no es compleix la condicio anterior
            p = p+1 #La variable p anira augmentant gradualment
            primer=True #La variable primer valdra true, ja que en la condicio anterior deiem que si el nombre era divisible entre un nombre primer, no era primer
                        #En aquest cas, com que de moment el nombre no ha pogut ser dividit, es suposadament primer
    if primer: #Si al final del while la variable booleana primer val true, significa que el nombre no es divisible entre cap numero primer anterior a ell i per tant, es primer
        print "Es primer" #En consequencia, imprimirem que si es primer
    t2=time.clock() #Segon temps
    print "El temps de proces ha estat %0.3f ms" % ((t2-t1)*1000)#Imprimirem el temps que hem trigat en executar la funcio
    lol=xrange(14)
    print lol
factorp(n)

    
