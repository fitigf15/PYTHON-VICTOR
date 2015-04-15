 
# -*- coding: utf-8 -*-


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                     #PRACTICA7

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                    #Victor Gomez Farrus
                                    #Enginyeria Informatica
                                    #Algorismica
                                    #Grup B


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Importem les llibreries

import time
import math


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Aquesta es la funcio negatius, es demana que sigui no recursiva, i per tant ha de ser
#iterativa. Utilitzarem la llista donada com a exemple
#La idea d'aquesta funcio es crear una variable que vagi d'esquerra a dreta i una altra que vagi de dreta a esquerra
#La funcio parara quan les variables es creuin

def negatius(llista):
    #print "llista inicial=",llista
    principi=0                                                          #principi anira d'esquerra a dreta
    final=len(llista)-1                                                 #final anira de dreta a esquerra
    #print "PRINCIPI=",principi,"  FINAL=",final
    while principi<=final:
        if llista[principi]>=0:                                         #Si a la posicio de principi trobem un negatiu,
                                                                        #el canviarem per el que esta a la posicio de final
                                                                        #i final avançara cap a l'esquerra
            llista[principi],llista[final]=llista[final],llista[principi]
            final-=1
            #print "PRINCIPI=",principi,"  FINAL-1=",final
        else:                                                           #Si no pasa aixo, llavors principi avançara cap a la dreta
            principi+=1
            #print "PRINCIPI+1=",principi,"  FINAL=",final
           
    print "llista final=",llista                                        #Quan s'hagin trobat, tots els negatius estaran a l'esquerra
                                                                        #i tots els positius a la dreta, imprimirem resultat

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Aquesta es la funcio exponent, es demana que sigui de dividir i vencer i per tant ha de ser recursiva
#Hem considerat que el exponent sempre ha de ser un nombre enter, ja que el que ens interessa es al final tenir
#el numero del resultat elevat a 1, per tant agafarem dues variables, una per l'exponent truncat i l'altra per
#l'exponent arrodonit. No aconseguirem un numero exacte quan es tracti de valors molt grans
#Aquesta es la funcio secundaria en la que es basa la funcio exponent, es la que fa tota la feina
def eleva(num,exp):
    if exp!=1:                                      #Si l'exponent no es 1, fem recursio
        trunc=math.floor(exp/float(2))              #Trunquem exponent              
        arr=math.ceil(exp/float(2))                 #Arrodonim exponent
        return eleva(num,trunc)*eleva(num,arr)      #Aqui utilitzem el consell a^n = a^⌊n/2⌋ · a^⌈n/2⌉
    else:
        return num                                  #Quan l'exponent sigui 1 retornarem el numero


#Aquesta es la funcio principal, que fa el que es demana a l'enunciat
def exponent(num,exp):
    resultat=eleva(num,exp)
    print resultat

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Aquesta es la funcio reversa, es demana que sigui de dividir i vencer i per tant ha de ser recursiva
#Per revertir una frase el que farem sera crear una frase buida i anar afegint en ordre invers tots els caracters
#de la frase introduida.
#Farem aixo fins que les dues frases tinguin la mateixa llargaria, es a dir, que estiguin completament invertides
#Aquesta es la funcio secundaria en la que es basa la funcio reverse, es la que fa tota la feina
def reversa(frase,frasefinal,pos):
    if len(frasefinal)==len(frase):                 #Quan la llargaria de la frase invertida sigui la mateixa que la de la introduida
        return frasefinal                           #significara que hem acabat i retornarem la frase invertida
    else:                                           #Mentre la frase invertida no sigui igual de llarga anirem cridant
                                                    #recursivament aquesta funcio que va afegint al principi el element que esta
                                                    #a la posicio "pos" de la frase
        frasefinal=frase[pos]+frasefinal
        return reversa(frase,frasefinal,pos+1)

#Aquesta es la funcio principal, que fa el que es demana a l'enunciat
def reverse(frase):
    inversa= reversa(frase,"",0)
    print inversa



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Aquesta es la funcio aprop, es demana que sigui de dividir i vencer, per tant ha de ser recursiva
#Per saber quins dos punts estan mes aprop el que farem sera ordenar-los i despres calcular en valor absolut
#el resultat de la seva diferencia. El que tingui el valor absolut mes petit sera el que tingui menys distancia
#Aquesta es la funcio secundaria en la que es basa la funcio aprop, es la que fa la majoria de la feina
def sonaprop(conjunt,parella,pos1,pos2):
    if pos2<=len(conjunt)-1:                                    #Fins es el ultim de la llista
        num1=conjunt[pos1]
        num2=conjunt[pos2]
        if num1==num2:                                          #Considerarem que si els numeros son iguals no tenen distancia,
                                                                #perque sino, aquesta distancia seria la minima al ser 0
            #print "iguals"
            return sonaprop(conjunt,parella,pos1+1,pos2+1)      #Seguirem avançant
        elif abs(num2-num1)<abs(parella[1]-parella[0]):         #Cada cop que trobem una distancia minima, la parella tindra
                                                                #nou valor
            #print "nou minim"
            return sonaprop(conjunt,[num1,num2],pos1+1,pos2+1)  #Seguirem avançant
        else:                                                   #Si no trobem res interessant, seguirem avançant
            #print "res nou"
            return sonaprop(conjunt,parella,pos1+1,pos2+1)
    else:                                                       #Quan el segon element sigui el ultim de la llista
        return parella
#Aquesta es la funcio principal, que fa el que es demana a l'enunciat.
def aprop(conjunt):
    quick_sort(conjunt)                                                     #El quick sort te complexitat nlog(n)
    resultat=sonaprop(conjunt,[conjunt[0],conjunt[len(conjunt)-1]],0,1)     #La distancia maxima entre els dos punts sera la del punt minim
                                                                            #al punt maxim.
                                                                            #La funcio sonaprop te complexitat nlog(n)
    print "La de punts que estan mes aprop es",resultat

#Per tant, la funcio aprop te una complexitat de 2nlog(n), es a dir nlogn
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Aquesta es la funcio elimina, la farem recursiva
#El nostre objectiu es eliminar cada element repetit de la llista amb una complexitat de nlog(n), per fer aixo
#de manera eficient, primer ordenarem els elements.
#Utilitzarem en la nostra funcio secundaria la funcio pop que te complexitat O(1), pero com la utilitzarem n-1 cops, llavors la nostra funcio
#tindra complexitat n.
def popeja(llista,pos):
    if pos<len(llista)-1:                   #Anirem element per element de la llista, si hi ha un element repetit
                                            #l'eliminarem, i si no, avançarem al seguent element fins arribar al final
        if llista[pos]!=llista[pos+1]:
            return popeja(llista,pos+1)
        else:
            #print "pop ", llista[pos]
            llista.pop(pos)
            return popeja(llista,pos)
    else:
        return llista
#Aquesta es la funcio principal, que fa el que es demana a l'enunciat
def elimina(llista):
    quick_sort(llista)                      #El quicksort te complexitat nlog(n)
    resultat= popeja(llista,0)              #La funcio popeja te complexitat n
    print resultat

#Per tant, la funcio elimina te una complexitat de 2nlog(n), es a dir, nlogn

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Cridem les funcions amb uns parametres que ens permetin avaluar-les

llista= [1,-2,3,-4,-3,5,6]
negatius(llista)
num=45.78
exp=45
exponent(num,exp)
frase="hola, com estas?"
reverse(frase)
conjunt=[-2.2,12.21,1.03,-3.42,-15.199,12.21,-24.45,0.04,23.002,12.1,-5.03,-15.2,-15.2011]
aprop(conjunt)
llista=[-1,-5,-23,-1,-5.3,-2,-5.3,-44,-2,1,2,3,4,4,5,5,6,6,1,2,3]
elimina(llista)
llista=["a","b","c","d","e","f","a","a","b","c","f","g","l"]
elimina(llista)
    
    
                                
    


