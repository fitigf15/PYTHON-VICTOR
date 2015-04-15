#Nom: Victor Gomez Farrus
#Grup de practiques: B
#                                                       PRACTICA 2
#
#
#------------------------------------------------------------------------------------------------------------------------------------------

import math #Importem la llibreria math
import cmath #Importem la llibreria cmath

#------------------------------------------------------------------------------------------------------------------------------------------
#Modifiqueu la funció futval de manera que el nombre danys que fa servir sigui també una dada que
#entra lusuari (compte amb el concepte dinterès!). Canvieu el missatge final adequadament.
def futval(): #Definim la funcio
        anysinversio = input("Aquest programa calcula el valor futur duna determinada inversio als anys que escriviu a continuació: ")#Fem un input per definir la variable anysinversio
        principal = input("Entra la inversio inicial: ")#Fem un input per definir la variable principal
        apr = input("Entra linteres anual: ")#Fem un input per definir la variable apr
        for i in range(anysinversio): #Amb aquesta funcio repetirem l
                principal = principal * (1 + apr) #Tornem a posar valor a la variable principal
        print " La quantitat al cap de ", anysinversio, "anys es: ", principal, "." #Imprimim el resultat
	
#-------------------------------------------------------------------------------------------------------------------------------------------

#Modifiqueu la funció convert de manera que calculi i imprimeixi una taula de temperatures Celsius i
#dels seus equivalents Fahrenheit cada 10 graus de 0C a 100C.

# Un programa per pasar de graus Celsius a Fahrenheit
def convert(): #Defininm la funcio
        celsius = 0 #Definim la variable celsius
        for i in range(0, 100, 10): #Repetirem els graus celsius de 10 en 10 desde 0 fins a 100
                celsius = celsius + 10 #Tornem a posar valor a la variable celsius
                farenheit = 9.0 / 5.0 * celsius + 32 #Fem la funcio de la variable farenheit
                print "The temperature of", celsius, "degrees Celsius is:", farenheit, "degrees Farenheit." #Imprimim el resultat
                
#-------------------------------------------------------------------------------------------------------------------------------------------

#Escriviu una funció, exp, que calculi i imprimeixi el resultat de cada una daquestes expressions:
#Assegureu-vos que el valor està en el tipus correcte.
#a) 4.0 / 10.0 + 3.5 * 2
#b) 10 % 4 + 6 / 2
#c) abs(4 - 20 / 3) ** 3
#d) sqrt(4.5 - 5.0) + 7 * 3
#e) 3 * 10 / 3 + 10 % 3
#f) 3L ** 3
def exp(): #Definim la funcio
        resultatA = (4.0 / 10.0) + (3.5 * 2) #Definim la funcio del resultat A
        print "El resultat de l'apartat A és", resultatA, "." #Imprimim el resultat A
        resultatB = (10 % 4) + (6 / 2) #Definim la funcio del resultat B
        print "El resultat de l'apartat B és", resultatB, "." #Imprimim el resultat B
        resultatC = abs(4 - 20 / 3) ** 3 #Definim la funcio del resultatC
        print "El resultat de l'apartat C és", resultatC, "." #Imprimim el resultat C
        resultatD = cmath.sqrt(4.5 - 5.0) + 7 * 3 #Definim la funcio del resultat D
        print "El resultat de l'apartat D és", resultatD, "." #Imprimim el resultat D
        resultatE = 3 * 10 / 3 + 10 % 3 #Definim la funcio del resultat E
        print "El resultat de l'apartat E és", resultatE, "." #Imprimim el resultat E
        resultatF = 3L ** 3 #Definim la funcio del resultat F
        print "El resultat de l'apartat F és", resultatF, "." #Imprimim el resultat F

#-------------------------------------------------------------------------------------------------------------------------------------------

#Considereu dos punts en un pla segons les seves coordenades (x1,y1) i (x2,y2). Escriviu
#una funció, punts, que calculi la pendent de la recta que passa per aquests dos punts. m=(y2-y1)/(x2-x1)
def punts(): #Definim la funcio
        x1 = input("Introdueix la coordenada x1 del punt P1: ") #Fem un input per determinar la variable x1
        y1 = input("Introdueix la coordenada y1 del punt P1: ") #Fem un input per determinar la variable y1
        x2 = input("Introdueix la coordenada x2 del punt P2: ") #Fem un input per determinar la variable x2
        y2 = input("Introdueix la coordenada y2 del punt P2: ") #Fem un input per determinar la variable y2
        m = (y2 - y1) / (x2 - x1) #Definim la funcio m
        print "El pendent de la recta que passa per els punts P1 i P2 es: ", m, "." #Imprimim el resultat
        
#-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funció, euclid, que accepti dos punts i calculi la distància euclidiana entre ells.
#d = sqrt([(x2-x1)^2]+[(y2-y1)^2])
def euclid(): #Definim la funcio
        x1 = (input("Introdueix la coordenada x1 del punt P1: ")) #Fem un input per determinar la variable x1
        y1 = (input("Introdueix la coordenada y1 del punt P1: ")) #Fem un input per determinar la variable y1
        x2 = (input("Introdueix la coordenada x2 del punt P2: ")) #Fem un input per determinar la variable x2
        y2 = (input("Introdueix la coordenada y2 del punt P2: ")) #Fem un input per determinar la variable y2
        z1 = ((x2 - x1) ** 2) #Definim la funcio de z1
        z2 = ((y2 - y1) ** 2) #Definim la funcio de z2
        d0 = float(z1 + z2) #Definim la funcio d0
        d = math.sqrt(d0) #Definim la funcio d
        print "La distancia euclidiana entre els punts P1 i P2 es: ", d, "." #Imprimim el resultat

#-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funció, euclid2, que accepti dos punts i calculi el nombre enter que més sapropa a la
#distància euclidiana.
def euclid2(): #Definim la funcio
        x1 = (input("Introdueix la coordenada x1 del punt P1: ")) #Fem un input per determinar la variable x1
        y1 = (input("Introdueix la coordenada y1 del punt P1: ")) #Fem un input per determinar la variable y1
        x2 = (input("Introdueix la coordenada x2 del punt P2: ")) #Fem un input per determinar la variable x2
        y2 = (input("Introdueix la coordenada y2 del punt P2: ")) #Fem un input per determinar la variable y2
        z1 = ((x2 - x1) ** 2) #Definim la funcio de z1
        z2 = ((y2 - y1) ** 2) #Definim la funcio de z2
        d0 = (z1 + z2) #Definim la funcio de d0
        d = math.sqrt(d0) #Definim la funcio de d
        print "El nombre enter que mes s'apropa a la distancia euclidiana es ", int(round(d)), "." #Imprimim el resultat arrodonit amb round

#-------------------------------------------------------------------------------------------------------------------------------------------

#Per les funcions següents necessiteu la comanda if<cond>:<body> de Python:
#Escriu una funció, factmenor, que imprimeixi tots els valors menors que
#6204484017332394393600000 i que són factorials dalgun nombre natural.
def factmenor(): #Definim la funcio
    a = 6204484017332394393600000 #Posem valor a la variable a
    b = 1#Posem valor a la variable b
    c = 1 #Posem valor a la variable c
    print "Els valors menors que 6204484017332394393600000 i que son factorials d'algun nombre natural son:"
    while b < a: #Mentre el valor b sigui mes petit que a
            print b #Imprimim b
            b = 1 #Tornem a posar valor a la variable b
            c = c +1 #Tornem a posar valor a la variable c
            d = 1 #Afegim una nova variable d i li posem un valor
            while c >= d: #Mentre c sigui mes gran o igual que d
                    d = d +1 #Tornem a posar valor a la variable d
                    b = b*d #Tornem a posr valor a la variable b

#-------------------------------------------------------------------------------------------------------------------------------------------

#Fes una funció, suma, que sumi tots els nombres naturals menors que 1000 i que siguin múltiples de
#3 i de 5.
def suma(): #Definim la funcio
        a = 0 #Posem valor a la variable a
        b = 0 #Posem valor a la variable b
        while a < 1000: #Mentre a sigui mes petita que 1000
                a = a+3*5 #Tornem a posar valor a la variable a
                b = b+a #Tornem a posar valor a la variable b
        print "La suma de tots els nombres naturals menors a 1000 i multiples de 3 i 5 es: ", b #Imprimim b      

#-------------------------------------------------------------------------------------------------------------------------------------------

#Escriu una funció, divisible, que calculi quin és el nombre natural més petit que és divisible per
#2,3,4,5,6,7,8,9 i 10.
def divisible(): #Definim la funcio
    a = 1 #Posem valor a la variable a
    while ( a%2 or a%3 or a%4 or a%5 or a%6 or a%7 or a%8 or a%9 or a%10) != 0: #Mentre el residu de la divisio de a entre 2,3,4,5,6,7,8,9,10 sigui diferent de 0
        a = a+1 #Tornem a posar valor a la variable a
    print "El nombre minim divisible per 2, 3, 4, 5, 6, 7, 8, 9 i 10 sera: ", a #Imprimim b        

#Comentari: 
#-------------------------------------------------------------------------------------------------------------------------------------------

futval()
convert()
exp()
punts()
euclid()
euclid2()
factmenor()
suma()
divisible()
